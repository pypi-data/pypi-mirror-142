
import json
import time
from pydash import get, set_, unset
from ..utility.logger import Logger

logger = Logger("TelemetricState").set()
REPORTED = 'reported'
DESIRED  = 'desired'
DELTA    = 'delta'

class TelemetricState:
    def __init__(self) -> None:
        self.version = 1
        self.lastPushTime = -1
        self.allStates: list = []
        self.states = {
            DESIRED: {},
            REPORTED: {},
            DELTA: {}
        }
        self.metadata = {
            DESIRED: {},
            REPORTED: {},
            DELTA: {}
        }

    def _isStateExists(self, stateName: str) -> bool:
        """
        Check if a state exists in the state machine
        
        :param stateName: The name of the state to check for
        :type stateName: str
        :return: The index of the state in the list of all states.
        """
        try:
            index = self.allStates.index(stateName)
            if index > -1: 
                logger.debug(f'_isStateExists: {stateName} exists')
                return True
            else: 
                logger.warn(f'_isStateExists: {stateName} does not exists')
                return False
        except ValueError:
            logger.warn(f'_isStateExists: {stateName} does not exists')
            return False

    def _createNewState(self, stateName: str) -> None:
        """
        If the state doesn't exist, create it
        
        :param stateName: The name of the state to create
        :type stateName: str
        """
        if self._isStateExists(stateName) == False:
            self.allStates.append(stateName)

        self.states[REPORTED][stateName] = {}
        self.states[DESIRED][stateName] = {}
        self.states[DELTA][stateName] = {}
        self.metadata[REPORTED][stateName] = {}
        self.metadata[DESIRED][stateName] = {}
        self.metadata[DELTA][stateName] = {}

    def _isVirtualAheadOfLocal(self, stateName: str, attributeTree: str, vTimestamp, dataType: str = REPORTED) -> bool:
        """
        If the virtual time is less than or equal to the local time, return False. Otherwise, return
        True
        
        :param stateName: the name of the state
        :type stateName: str
        :param attributeTree: The attribute tree of the attribute that is being compared
        :type attributeTree: str
        :param vTimestamp: The timestamp of the virtual state
        :param dataType: The type of data to check. Can be either REPORTED or ADMIN
        :type dataType: str
        :return: The return value is a boolean that indicates whether the virtual time is ahead of the
        local time.
        """
        if get(self.metadata[dataType][stateName], attributeTree) and vTimestamp <= get(self.metadata[dataType][stateName], attributeTree):
            logger.debug(f'_isVirtualAheadOfLocal: {stateName}/{attributeTree}: The virtual time < local time')
            return False
        else:
            logger.debug(f'_isVirtualAheadOfLocal: {stateName}/{attributeTree}: The virtual time > local time')
            return True

    def report(self, stateName: str, attributeTree: str, value, vTimestamp) -> bool:
        try:
            logger.debug(f'report: {stateName} / {attributeTree} / {value} / {vTimestamp}')
            # now
            now = int(time.time())

            # check and create
            if self._isStateExists(stateName) == False: self._createNewState(stateName)

            # only update if virtual timestamp ahead of local
            if self._isVirtualAheadOfLocal(stateName, attributeTree, vTimestamp, REPORTED):
                if get(self.states[REPORTED][stateName], attributeTree) == None:
                    set_(self.states[REPORTED][stateName], attributeTree, value)
                    set_(self.metadata[REPORTED][stateName], attributeTree, now)
                    logger.debug(f'report: Created new reported state {stateName} attributes {attributeTree}')
                else:
                    # check against desired
                    if get(self.states[REPORTED][stateName], attributeTree) == get(self.states[DESIRED][stateName], attributeTree):
                        logger.debug(f'report: The new state {stateName} attribute {attributeTree} value is equal to desired state')
                    else:
                        set_(self.states[REPORTED][stateName], attributeTree, value)
                        set_(self.metadata[REPORTED][stateName], attributeTree, now)
                        logger.debug(f'report: Updated new reported state {stateName} attributes {attributeTree}')

                # remove desired
                unset(self.states[DESIRED][stateName], attributeTree)
                unset(self.metadata[DESIRED][stateName], attributeTree)
                logger.debug(f'report: Removed desired state {stateName} attributes {attributeTree}')
                return True
            else:
                logger.debug(f'report: Timestamp in local for state {stateName} attributes {attributeTree} is ahead of its Virtual Twin')
                return False
        except Exception as ex:
            logger.warn(ex)
            return False

    def desire(self, stateName: str, attributeTree: str, value, vTimestamp) -> bool:
        """
        Create a new desired state
        
        :param stateName: The name of the state to be created
        :type stateName: str
        :param attributeTree: The name of the attribute tree
        :type attributeTree: str
        :param value: The value of the attribute
        :param vTimestamp: The time the desired state was set
        :return: The return value is a boolean.
        """
        try:
            # now
            now = int(time.time())

            # check and create
            if self._isStateExists(stateName) == False: self._createNewState(stateName)

            set_(self.states[DESIRED][stateName], attributeTree, value)
            set_(self.metadata[DESIRED][stateName], attributeTree, now)
            logger.debug(f'report: Created new desired state {stateName} attributes {attributeTree}')
            return True
        except Exception as ex:
            logger.warn(ex)
            return False

    def getPendingDesire(self, stateName: str):
        """
        Get the pending desire for a given state
        
        :param stateName: The name of the state to get the pending desire for
        :type stateName: str
        :return: A dictionary with the attributeTree and value.
        """
        flat = TelemetricState.flattening(self.states[DESIRED][stateName])
        for key in flat:
            logger.debug(f'getPendingDesire: Pending {key}')
            return {
                'attributeTree': key,
                'value': get(self.states[DESIRED][stateName], key)
            }

    def snapshot(self, stateName: str, attributesOnly: bool = False) -> object:
        """
        This function returns the latest value for a given state
        
        :param stateName: The name of the state to be retrieved
        :type stateName: str
        :param attributesOnly: If true, only the attributes of the state are returned, defaults to False
        :type attributesOnly: bool (optional)
        :return: The latest value for the state.
        """
        latest = get(self.states[REPORTED], stateName)
        logger.debug(f'snapshot: Value for {stateName} = {json.dumps(latest)}')
        if attributesOnly == False:
            return {
                'state': {
                    'reported': latest
                }
            }
        else:
            return latest

    def getLastTime(self):
        """
        Return the last time the push button was pressed
        :return: The last time the button was pushed.
        """
        return self.lastPushTime

    def updateNewTime(self):
        """
        This function updates the lastPushTime variable to the current time
        """
        self.lastPushTime = int(time.time() * 1000)

    @staticmethod
    def flattening(objectTree: object):
        """
        Flattens a nested dictionary into a single level dictionary
        
        :param objectTree: object
        :type objectTree: object
        :return: A dictionary of key-value pairs.
        """
        out = {}

        def flat(x, name =''):
            
            # If the Nested key-value 
            # pair is of dict type
            if type(x) is dict:
                
                for a in x:
                    flat(x[a], name + a + '.')
                    
            # If the Nested key-value
            # pair is of list type
            elif type(x) is list:
                
                i = 0
                
                for a in x:                
                    flat(a, name + str(i) + '.')
                    i += 1
            else:
                out[name[:-1]] = x
    
        flat(objectTree)
        return out