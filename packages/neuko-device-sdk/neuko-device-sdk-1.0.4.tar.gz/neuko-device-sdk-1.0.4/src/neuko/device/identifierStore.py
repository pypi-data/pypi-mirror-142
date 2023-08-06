import configparser
from abc import ABC, abstractmethod
from ..utility.logger import Logger
from .model import DeviceIdentifier

logger = Logger("DeviceIdentifierStore").set()
config = configparser.ConfigParser()

# const
ACCOUNT_ID  = 'accountId'
PROJECT_ID  = 'projectId'
SCHEMA_ID   = 'schemaId'
DEVICE_ID   = 'deviceId'

class DeviceIdentifierStore(ABC):

    def __init__(self) -> None:
        self._deviceConfig = None

    def getAccountId(self) -> str:
        val = self._readConfigDevice(ACCOUNT_ID)
        if val != None: return val
        else: raise Exception("Please override the getAccountId method to and return the value")

    def getProjectId(self) -> str:
        val = self._readConfigDevice(PROJECT_ID)
        if val != None: return val
        else: raise Exception("Please override the getAccountId method to and return the value")

    def getDeviceSchemaId(self) -> str:
        val = self._readConfigDevice(SCHEMA_ID)
        if val != None: return val
        else: raise Exception("Please override the getAccountId method to and return the value")
        

    def getDeviceId(self) -> str:
        val = self._readConfigDevice(DEVICE_ID)
        if val != None: return val
        else: raise Exception("Please override the getAccountId method to and return the value")

    def _readConfigDevice(self, keyname: str) -> None:
        try:
            return self._deviceConfig[keyname]
        except KeyError:
            return None
        except Exception as ex:
            logger.error(ex)
            return None

    def resolveDeviceIdentifier(self, configFilePathName: str = 'config.ini') -> DeviceIdentifier:
        try:
            
            accid = None
            proid = None
            schid = None
            devid = None

            if self._deviceConfig == None: 
                try:
                    config.read(configFilePathName)
                    if 'device' in config:
                        self._deviceConfig = config['device']
                        accid = self._readConfigDevice(ACCOUNT_ID)
                        proid = self._readConfigDevice(PROJECT_ID)
                        schid = self._readConfigDevice(SCHEMA_ID)
                        devid = self._readConfigDevice(DEVICE_ID)
                except:
                   self._deviceConfig = {} 
                   
            # if none, maybe some of them coming for overriden method
            if accid == None:
                logger.debug(f'resolveDeviceIdentifier: accountId cannot be located in config file')
                accid = self.getAccountId()

            if proid == None:
                logger.debug(f'resolveDeviceIdentifier: projectId cannot be located in config file')
                proid = self.getProjectId()

            if schid == None:
                logger.debug(f'resolveDeviceIdentifier: schemaId cannot be located in config file')
                schid = self.getDeviceSchemaId()

            if devid == None:
                logger.debug(f'resolveDeviceIdentifier: deviceId cannot be located in config file')
                devid = self.getDeviceId()

            logger.debug(f'resolveDeviceIdentifier: accountId: {accid}')
            logger.debug(f'resolveDeviceIdentifier: projectId: {proid}')
            logger.debug(f'resolveDeviceIdentifier: schemaId:  {schid}')
            logger.debug(f'resolveDeviceIdentifier: deviceId:  {devid}')

            return DeviceIdentifier(accid, proid, schid, devid)

        except Exception as ex:
            logger.error(ex)
            raise Exception(ex)