import os
import asyncio
import json
import threading
import time
from typing import Union
from transitions.extensions.asyncio import EventData
from paho.mqtt.client import MQTTMessage
from .telemetricState import TelemetricState
from .telemetricWorker import TelemetricWorker
from ..utility.utils import get_project_root
from ..utility.logger import Logger
from ..lifecycle.connectionStateMachine import ConnectionStateMachine, ConnectionStateNachineLifecycle
from ..device.model import DeviceIdentifier, Features
from ..device.identifierStore import DeviceIdentifierStore
from ..device.deviceManagement import DeviceManagement
from ..connection.connectionStore import ConnectionStore
from ..connection.connectionManagement import ConnectionManagement
from ..connection.model import Certificate, Configuration
from ..connection.certificateStore import CertificateStore
from ..connection.certificateManagement import CertificateManagement
from ..iot.model import UpdateDelta, Provider
from ..iot.iot import IoT
from ..iot.bootstrap import BootstrapClient
from ..iot.neuko import NeukoClient

logger = Logger("Device").set()

INTERNAL_CONFIGURATION = 'internal_configuration'

class InternalConnectionStore(ConnectionStore):
    async def getPerpetualConnectionSettings(self, deviceIdentifier: DeviceIdentifier) -> str:
        fd = open(os.path.join(get_project_root(), 'auto-generated-settings.json'), mode='r')
        data = json.load(fd)
        fd.close()
        return data

    async def savePerpetualConnectionSettings(self, deviceIdentifier: DeviceIdentifier, settings: str) -> bool:
        fd = open(os.path.join(get_project_root(), 'auto-generated-settings.json'), mode="w")
        json.dump(settings, fd)
        fd.close()
        return True

    async def deletePerpetualConnectionSettings(self, deviceIdentifier: DeviceIdentifier) -> None:
        return True

    async def isPerpetualConnectionSettingsExists(self, deviceIdentifier: DeviceIdentifier) -> bool:
        return os.path.exists(os.path.join(get_project_root(), 'auto-generated-settings.json'))

class InternalCertificateStore(CertificateStore):

    async def getBootstrapCertificateAuthority(self, deviceIdentifier: DeviceIdentifier) -> str:
        filePath = f'{deviceIdentifier.deviceSchemaId}-bootstrap-root_ca.pem'
        logger.debug(f'getBootstrapCertificateAuthority: {os.path.join(get_project_root(), filePath)}')
        if os.path.exists(os.path.join(get_project_root(), filePath)): return os.path.join(get_project_root(), filePath)
        else: raise Exception('CertificateNotFound')

    async def getBootstrapChainCertificate(self, deviceIdentifier: DeviceIdentifier) -> str:
        filePath = f'{deviceIdentifier.deviceSchemaId}-bootstrap-certificate.pem'
        logger.debug(f'getBootstrapChainCertificate: {os.path.join(get_project_root(), filePath)}')
        if os.path.exists(os.path.join(get_project_root(), filePath)): return os.path.join(get_project_root(), filePath)
        else: raise Exception('CertificateNotFound')

    async def getBootstrapPrivateKey(self, deviceIdentifier: DeviceIdentifier) -> str:
        filePath = f'{deviceIdentifier.deviceSchemaId}-bootstrap-private_key.pem'
        logger.debug(f'getBootstrapPrivateKey: {os.path.join(get_project_root(), filePath)}')
        if os.path.exists(os.path.join(get_project_root(), filePath)): return os.path.join(get_project_root(), filePath)
        else: raise Exception('CertificateNotFound')

    async def getPerpetualCertificateAuthority(self, deviceIdentifier: DeviceIdentifier) -> str:
        if os.path.exists(os.path.join(get_project_root(), 'cert.ca.pem')): return os.path.join(get_project_root(), 'cert.ca.pem')
        else: raise Exception('CertificateNotFound')

    async def getPerpetualChainCertificate(self, deviceIdentifier: DeviceIdentifier) -> str:
        filePath = f'{deviceIdentifier.accountId}-{deviceIdentifier.projectId}-{deviceIdentifier.deviceSchemaId}-{deviceIdentifier.deviceId}-public.pem.key'
        if os.path.exists(os.path.join(get_project_root(), filePath)): return os.path.join(get_project_root(), filePath)
        else: raise Exception('CertificateNotFound')

    async def getPerpetualPrivateKey(self, deviceIdentifier: DeviceIdentifier) -> str:
        filePath = f'{deviceIdentifier.accountId}-{deviceIdentifier.projectId}-{deviceIdentifier.deviceSchemaId}-{deviceIdentifier.deviceId}-private.pem.key'
        if os.path.exists(os.path.join(get_project_root(), filePath)): return os.path.join(get_project_root(), filePath)
        else: raise Exception('CertificateNotFound')

    async def savePerpetualCertificateAuthority(self, deviceIdentifier: DeviceIdentifier, certificate: str) -> None:
        fd = open(os.path.join(get_project_root(), 'cert.ca.pem'), mode="w")
        fd.write(certificate)
        fd.close()

    async def savePerpetualChainCertificate(self, deviceIdentifier: DeviceIdentifier, certificate: str) -> None:
        fd = open(os.path.join(get_project_root(), f'{deviceIdentifier.accountId}-{deviceIdentifier.projectId}-{deviceIdentifier.deviceSchemaId}-{deviceIdentifier.deviceId}-public.pem.key'), mode="w")
        fd.write(certificate)
        fd.close()

    async def savePerpetualPrivateKey(self, deviceIdentifier: DeviceIdentifier, certificate: str) -> None:
        fd = open(os.path.join(get_project_root(), f'{deviceIdentifier.accountId}-{deviceIdentifier.projectId}-{deviceIdentifier.deviceSchemaId}-{deviceIdentifier.deviceId}-private.pem.key'), mode="w")
        fd.write(certificate)
        fd.close()

class Device:

    def __init__(
        self, 
        deviceIdentifierStore: DeviceIdentifierStore = None,
        connectionStore: ConnectionStore = None,
        certificateStore: CertificateStore = None
    ) -> None:
        self._connectionStateMachine = ConnectionStateMachine(self._connectionStateChanged)

        if deviceIdentifierStore != None: self._deviceManager = DeviceManagement(deviceIdentifierStore)
        else: self._deviceManager = DeviceManagement(DeviceIdentifierStore())

        if connectionStore != None: self._connectionManager = ConnectionManagement(connectionStore)
        else: self._connectionManager = ConnectionManagement(InternalConnectionStore())

        if certificateStore != None: self._certificateManager = CertificateManagement(certificateStore)
        else: self._certificateManager = CertificateManagement(InternalCertificateStore())
        
        
        self._deviceClient: Union[IoT, BootstrapClient, NeukoClient] = None
        self._contextCertificates: Certificate = None
        self._contextConfiguration: Configuration = None
        self._bootstrapProvRespStatus: bool = False
        self._bootstrapCompleteFlag: bool = False
        self._deviceConfiguration: Configuration = None
        self._localTelemetricState: TelemetricState = TelemetricState()
        self._telemetricWorkers: TelemetricWorker = TelemetricWorker()
        self._features: Features = None

    def _initiateDeviceClientByProvider(self, clientProvider: Provider) -> Union[IoT, BootstrapClient, NeukoClient]:
        """
        The function is called by the DeviceManager to initiate a DeviceClient
        
        :param clientProvider: Provider
        :type clientProvider: Provider
        :return: A client object
        """
        if clientProvider == Provider.BOOTSTRAP:
            return BootstrapClient(self._deviceManager.getDeviceIdentifier(), self._connectionManager, self._certificateManager)
        elif clientProvider == Provider.NEUKO:
            return NeukoClient(self._deviceManager.getDeviceIdentifier(), self._connectionManager, self._certificateManager)
        else:
            logger.error('Unknown')

    async def _bootstrapProvisioningSuccess(self, client, userdata, message: MQTTMessage) -> None:
        """
        The bootstrapProvisioningSuccess function is called when the device receives a message from the
        cloud that the bootstrap provisioning process has been successful
        
        :param client: the client instance for this callback
        :param userdata: The user data that was passed to the client’s constructor
        :param message: MQTTMessage
        :type message: MQTTMessage
        """
        logger.debug(f'_bootstrapProvisioningSuccess: message = {message.payload}')
        self._bootstrapProvRespStatus = True
        await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.START_PROV_BOOT_SUCC)

    async def _bootstrapProvisioningError(self, client, userdata, message: MQTTMessage) -> None:
        """
        The bootstrapProvisioningSuccess function is called when the device receives a message from the
        cloud that the bootstrap provisioning process has been errornous
        
        :param client: the client instance for this callback
        :param userdata: The user data that was passed to the client’s constructor
        :param message: MQTTMessage
        :type message: MQTTMessage
        """
        logger.debug(f'_bootstrapProvisioningError: message = {message.payload}')
        self._bootstrapProvRespStatus = True
        # await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.GOODBYE)
        await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.START_PROV_BOOT_SUCC)

    async def _bootstrapReceivePerpetualCerts(self, client, userdata, message: MQTTMessage) -> None:
        """
        The bootstrap server sends us a message containing the certificate authority, chain certificate,
        and private key. We save these to the certificate manager
        
        :param client: the client instance for this callback
        :param userdata: The user data that was passed to the client when it was created
        :param message: MQTTMessage
        :type message: MQTTMessage
        """
        logger.debug(f'_bootstrapReceivePerpetualCerts: Received perpetual certificates')
        data = json.loads(message.payload)
        await self._certificateManager.savePerpetualCertificates(
            self._deviceManager.getDeviceIdentifier(),
            Certificate(
                data['certificates']['certificateAuthority'],
                data['certificates']['chainCertificate'],
                data['certificates']['privateKey']
            )
        )

    async def _bootstrapReceivePerpetualConfig(self, client, userdata, message: MQTTMessage) -> None:
        """
        The function receives a message from the MQTT broker and then saves the configuration to the
        database
        
        :param client: The MQTT client object
        :param userdata: The user data is a user space variable that can be used to store data with the
        client instance
        :param message: MQTTMessage
        :type message: MQTTMessage
        """
        logger.debug(f'_bootstrapReceivePerpetualConfig: Received perpetual configurations')
        data = json.loads(message.payload)
        await self._connectionManager.savePerpetualConnectionConfiguration(
            self._deviceManager.getDeviceIdentifier(),
            Configuration(**data['configuration'])
        )

    async def _bootstrapCompleted(self, client, userdata, message: MQTTMessage) -> None:
        """
        When the bootstrap is completed, the _bootstrapCompleteFlag is set to True
        
        :param client: the client instance for this callback
        :param userdata: The user data that was passed to the client when it was created
        :param message: MQTTMessage
        :type message: MQTTMessage
        """
        logger.debug(f'_bootstrapCompleted: Bootstrap Done!')
        self._bootstrapCompleteFlag = True
        await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.BOOTSTRAP_COMPLETED)

    async def _resolveClientProviderType(self) -> Provider:
        if self._deviceConfiguration == None:
            self._deviceConfiguration = await self._connectionManager.getPerpetualConnectionConfiguration(self._deviceManager.getDeviceIdentifier())

        logger.debug(f'_resolveClientProviderType: Provider = {self._deviceConfiguration["connection"]["provider"]}')
        return self._deviceConfiguration["connection"]["provider"]
    
    async def _onTelemetricStateChangedRequest(self, context, data: UpdateDelta) -> None:
        """
        The function is called when a telemetric state is changed. 
        
        The function loops through all the attributes in the delta and updates the local desire and
        reports the local telemetric state. 
        
        The function then updates the virtual twin telemetric state.
        
        :param context: The context associated with the message
        :param data: The data that was sent to the method
        :type data: UpdateDelta
        """
        try:
            flatDelta = TelemetricState.flattening(data.delta)

            # loop each delta
            for attributeTree in flatDelta:
                logger.debug(f'_onTelemetricStateChangedRequest: State {data.stateName} has request changed for attribute {attributeTree}')
                self._localTelemetricState.desire(data.stateName, attributeTree, flatDelta[attributeTree], int(time.time())) # update local desire
                result = await self._telemetricWorkers.execute(data.deviceIdentifier, data.stateName, attributeTree, flatDelta[attributeTree]) # execute
                if result: self._localTelemetricState.report(data.stateName, attributeTree, flatDelta[attributeTree], int(time.time())) # report local if nessecary

            # update twin virtual
            await self._deviceClient.pushTelemetricState(data.stateName, self._localTelemetricState.snapshot(data.stateName))
        except Exception as ex:
            logger.warn(ex)
            # TODO - should we do anything here. JS is doing nothing right now

    async def _initializeTelemetricState(self) -> None:
        """
        The function is responsible for initializing the local telemetric state. 
        It does this by pulling all the telemetric state names from the device client. 
        It then processes each state by pulling the telemetric state and metadata. 
        The metadata is used to determine the timestamp of the telemetric state. 
        The telemetric state is then processed by flattening it and then adding it to the local
        telemetric state
        """
        try:
            allStateNames = await self._deviceClient.fetchAllTelemetricStateNames()
            logger.info(f'_initializeTelemetricState: States = {allStateNames}')

            # process each state
            for eachState in allStateNames:
                logger.debug(f'_initializeTelemetricState: Processing {eachState}')
                data = await self._deviceClient.pullTelemetricState(eachState)
                logger.debug(f'_initializeTelemetricState: {eachState} = {json.dumps(data)}')

                # process reported
                if 'reported' in data['state']:
                    if eachState == INTERNAL_CONFIGURATION:
                        self._features = Features(**data['state']['reported']['features'])
                    
                    flatReport = TelemetricState.flattening(data['state']['reported'])
                    flatMetadata = TelemetricState.flattening(data['metadata']['reported'])
                    logger.debug(f'_initializeTelemetricState: flatMetadata = {flatMetadata}')
                    for attributeTree in flatReport:
                        logger.debug(f'_initializeTelemetricState: Update local report {eachState} attribute {attributeTree}::{flatReport[attributeTree]}::{flatMetadata[attributeTree + ".timestamp"]}')
                        self._localTelemetricState.report(eachState, attributeTree, flatReport[attributeTree], flatMetadata[attributeTree + '.timestamp'])

                # process desired
                if 'desired' in data['state']:
                    flatDesired = TelemetricState.flattening(data['state']['desired'])
                    flatMetadata = TelemetricState.flattening(data['metadata']['desired'])
                    for attributeTree in flatDesired:
                        logger.debug(f'_initializeTelemetricState: Update local desire {eachState} attribute {attributeTree} and {attributeTree + ".timestamp"}')
                        self._localTelemetricState.report(eachState, attributeTree, flatDesired[attributeTree], flatMetadata[attributeTree + '.timestamp'])

        except Exception as ex:
            logger.error(ex)
            # TODO - should we do anything here. JS is raising an exception
    
    async def _synchronizeTelemetricState(self) -> None:
        """
        The function is responsible for synchronizing the local telemetric state with the remote
        telemetric state. 
        It does this by first iterating through all the telemetric states and then for each state, it
        iterates through all the pending desires. 
        If the pending desire is not None, it means that there is a pending desire to be sent to the
        remote telemetric state. 
        The function then calls the telemetric worker to execute the desired operation. 
        If the operation is successful, the function reports the desire to the local telemetric state. 
        Otherwise, it ignores the desire and deletes it from the local telemetric state. 
        Finally, the function updates the twin virtual telemetric state
        """
        for stateName in self._localTelemetricState.allStates:
            if stateName != INTERNAL_CONFIGURATION:
                logger.info(f'_synchronizeTelemetricState: Sync {stateName}')
                pendingDesired = self._localTelemetricState.getPendingDesire(stateName)
                while pendingDesired != None:
                    logger.debug(f'_synchronizeTelemetricState: Sync {stateName}/{pendingDesired["attributeTree"]}')
                    result = await self._telemetricWorkers.execute(
                        self._deviceManager.getDeviceIdentifier(),
                        stateName,
                        pendingDesired['attributeTree'],
                        pendingDesired['value']
                    )
                    if result:
                        logger.debug(f'_synchronizeTelemetricState: Success synced {stateName}/{pendingDesired["attributeTree"]}')
                        self._localTelemetricState.report(stateName, pendingDesired['attributeTree'], pendingDesired['value'], int(time.time()))
                    else:
                        logger.debug(f'_synchronizeTelemetricState: Failed synced {stateName}/{pendingDesired["attributeTree"]}')
                        # TODO - what to do. Should we ignore and delete local desire
                    
                    pendingDesired = self._localTelemetricState.getPendingDesire(stateName)

                # update twin virtual
                await self._deviceClient.pushTelemetricState(stateName, self._localTelemetricState.snapshot(stateName))
                logger.debug(f'_synchronizeTelemetricState: Updated twin virtual for state {stateName}')
    
    async def _tick(self) -> None:
        try:
            logger.debug('_tick')
            self._localTelemetricState.updateNewTime()

            for stateName in self._localTelemetricState.allStates:
                if stateName in self._features['timestreamStorage']['value'] or '*' in self._features['timestreamStorage']['value']:
                   logger.debug(f'_tick: Timestream storage enabled for {stateName}') 
                   snap = self._localTelemetricState.snapshot(stateName, True)
                   await self._deviceClient.timestreamStorage(stateName, snap)

        except Exception as ex:
            logger.warn(ex)
    
    async def _connectionStateChanged(self, event: EventData):
        logger.debug(f'connectionStateChanged: events = {event.state.name}')

        if event.state.name == 'idle':
            await asyncio.sleep(1)
            await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.TEST_INTERNET)

        elif event.state.name == 'test_internet_connection':
            res = await self._connectionManager.checkIfConnectedToInternet()
            if res:
                await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.INTERNET_CONNECTED)
            else:
                await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.TEST_INTERNET, 5)

        elif event.state.name == 'bootstrap_junction':
            res = await self._connectionManager.checkIfConfigurationSaved(deviceIdentifier=self._deviceManager.getDeviceIdentifier())
            if res:
                # TODO - Go to perpetual state
                await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.FOUND_SAVED_SETTINGS)
            else:
                await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.NO_SAVED_SETTINGS)

        elif event.state.name == 'prepare_bootstrap':
            try:
                self._deviceClient = self._initiateDeviceClientByProvider(Provider.BOOTSTRAP)
                logger.debug("prepare_bootstrap: deviceClient initialized")
                await self._deviceClient.loadContextCertificate(Provider.BOOTSTRAP)
                logger.debug("prepare_bootstrap: Bootstrap certificates loaded")
                await self._deviceClient.loadContextConfiguration(Provider.BOOTSTRAP)
                logger.debug(f"prepare_bootstrap: Bootstrap settings loaded {self._contextConfiguration}")
                res = await self._deviceClient.connect()
                # TODO - do if res = false and keep waiting reconnection
                await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.BOOTSTRAP_CONNECTED)
            except Exception as ex:
                logger.warn(ex)
                await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.TEST_INTERNET, 5)

        elif event.state.name == 'prepare_provisioning':
            self._bootstrapProvRespStatus = False
            self._bootstrapCompleteFlag = False

            # subscribe to provisioning START success
            await self._deviceClient.subscribe(
                f'neuko/{self._deviceManager.getDeviceIdentifier().accountId}/device/{DeviceManagement.resolveDeviceUniqueId(self._deviceManager.getDeviceIdentifier())}/provision/start/success',
                self._bootstrapProvisioningSuccess
            )

            # subscribe to provisioning START error
            await self._deviceClient.subscribe(
                f'neuko/{self._deviceManager.getDeviceIdentifier().accountId}/device/{DeviceManagement.resolveDeviceUniqueId(self._deviceManager.getDeviceIdentifier())}/provision/start/error',
                self._bootstrapProvisioningError
            )

            # subscribe to provisioning perpetual CERTS topic
            await self._deviceClient.subscribe(
                f'neuko/{self._deviceManager.getDeviceIdentifier().accountId}/device/{DeviceManagement.resolveDeviceUniqueId(self._deviceManager.getDeviceIdentifier())}/provision/perpetual/certificates',
                self._bootstrapReceivePerpetualCerts
            )

            # subscribe to provisioning perpetual CONFIG topic
            await self._deviceClient.subscribe(
                f'neuko/{self._deviceManager.getDeviceIdentifier().accountId}/device/{DeviceManagement.resolveDeviceUniqueId(self._deviceManager.getDeviceIdentifier())}/provision/perpetual/configuration',
                self._bootstrapReceivePerpetualConfig
            )

            # subscribe to provisioning COMPLETED topic
            await self._deviceClient.subscribe(
                f'neuko/{self._deviceManager.getDeviceIdentifier().accountId}/device/{DeviceManagement.resolveDeviceUniqueId(self._deviceManager.getDeviceIdentifier())}/provision/completed',
                self._bootstrapCompleted
            )

            # publish a message to START provisioning
            await self._deviceClient.publish(
                "neuko/device/provision/start",
                json.dumps({
                    'version': 1,
                    'requestor': 'device',
                    'executor': 'bootstrap',
                    'data': {
                        'state': "DEVICE_PROVISIONING_START",
                        'deviceIdentifier': self._deviceManager.getDeviceIdentifier(),
                        'clientId': DeviceManagement.resolveClientId(self._deviceManager.getDeviceIdentifier()),
                        'schemaId': self._deviceManager.getDeviceSchemaId()
                    }
                }, default=vars)
            )
            waitTime = 0
            while waitTime < 30:
                if self._bootstrapProvRespStatus: waitTime = 100
                else: waitTime += 100e-3
                await asyncio.sleep(0.1)

        elif event.state.name == 'wait_for_claim':
            waitTime = 0
            while waitTime < 5 * 60:
                if self._bootstrapCompleteFlag: 
                    waitTime = 12 * 100
                else: waitTime += 100e-3
                await asyncio.sleep(0.1)

            if waitTime != 12 * 100: await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.BOOTSTRAP_IN_PROGRESS, 1)

        elif event.state.name == 'tear_down_bootstrap':
            await self._deviceClient.unsubscribe(f'neuko/{self._deviceManager.getDeviceIdentifier().accountId}/device/{DeviceManagement.resolveDeviceUniqueId(self._deviceManager.getDeviceIdentifier())}/provision/start/success')
            await self._deviceClient.unsubscribe(f'neuko/{self._deviceManager.getDeviceIdentifier().accountId}/device/{DeviceManagement.resolveDeviceUniqueId(self._deviceManager.getDeviceIdentifier())}/provision/start/error')
            await self._deviceClient.unsubscribe(f'neuko/{self._deviceManager.getDeviceIdentifier().accountId}/device/{DeviceManagement.resolveDeviceUniqueId(self._deviceManager.getDeviceIdentifier())}/provision/perpetual/certificates')
            await self._deviceClient.unsubscribe(f'neuko/{self._deviceManager.getDeviceIdentifier().accountId}/device/{DeviceManagement.resolveDeviceUniqueId(self._deviceManager.getDeviceIdentifier())}/provision/perpetual/configuration')
            await self._deviceClient.unsubscribe(f'neuko/{self._deviceManager.getDeviceIdentifier().accountId}/device/{DeviceManagement.resolveDeviceUniqueId(self._deviceManager.getDeviceIdentifier())}/provision/completed')
            await self._deviceClient.disconnect()
            self._deviceClient = None
            await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.BOOTSTRAP_DISCONNECTED, 5)

        elif event.state.name == 'prepare_perpetual':
            try:
                self._deviceClient = self._initiateDeviceClientByProvider(await self._resolveClientProviderType())
                logger.debug(f"prepare_perpetual: deviceClient initialized {self._deviceClient}")
                await self._deviceClient.loadContextCertificate(await self._resolveClientProviderType())
                logger.debug("prepare_perpetual: Perpetual certificates loaded")
                await self._deviceClient.loadContextConfiguration(await self._resolveClientProviderType())
                logger.debug(f"prepare_perpetual: Perpetual settings loaded {self._contextConfiguration}")
                res = await self._deviceClient.connect()
                # # TODO - do if res = false and keep waiting reconnection
                await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.PERPETUAL_CONNECTED)
            except Exception as ex:
                logger.warn(ex)
                await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.TEST_INTERNET, 5)

        elif event.state.name == 'initialize_telemetric_state':
            try:
                await self._deviceClient.onTelemetricStateChangedRequest(self, self._onTelemetricStateChangedRequest)
                await self._initializeTelemetricState()
                await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.TELEMETRIC_STATE_INITED)
            except Exception as ex:
                logger.warn(ex)
                # TODO - where to go when this failed

        elif event.state.name == 'sync_telemetric_state':
            try:
                await self._synchronizeTelemetricState()
                await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.TELEMETRIC_STATE_SYNCED)
            except Exception as ex:
                logger.warn(ex)
                # TODO - where to go when this failed

        elif event.state.name == 'work':
            now = int(time.time() * 1000)

            # handler being invoked in a new thread. Need this to run async
            def runTick():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(self._tick())
                loop.close()

            if now - self._localTelemetricState.getLastTime() >= self._features['interval']['value']:
                threading.Thread(target=runTick, daemon=True).start()

            await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.TOCK, 1)

        elif event.state.name == 'off':
            if self._deviceClient != None: await self._deviceClient.disconnect()
            logger.debug(f'_connectionStateChanged: Bye2')

        else:
            logger.warn(f'_connectionStateChanged: Unknown state name')

    async def start_async(self):
        """
        This function is called when the device is started. It starts the connection state machine
        """
        logger.debug(f'start_async: Device is starting asynchronously')
        self._stopFlag = False
        await self._connectionStateMachine.start()

    def start_threadsafe(self):
        """
        It starts the async function in a new thread
        """
        logger.debug(f'start_threadsafe: Device is starting in new thread')

        def startasyncthreadsafe():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.start_async())
            loop.close()

        threading.Thread(target=startasyncthreadsafe, daemon=True).start()

    async def stop(self) -> None:
        try:
            logger.debug(f'stop: Device is stoping')
            await self._connectionStateMachine.triggerLifecycle(ConnectionStateNachineLifecycle.GOODBYE)
            return None
        except AttributeError:
            return None
        except Exception as ex:
            logger.warn(ex)
            return None


    def useEffect(self, context, listener, stateName: str, attributeTree: str = "*") -> None:
        """
        This function adds a listener to the telemetric worker for the given state
        
        :param context: The context of the event
        :param listener: The function that will be called when the state changes
        :param stateName: The name of the state to listen to
        :type stateName: str
        :param attributeTree: The attribute tree to listen to, defaults to *
        :type attributeTree: str (optional)
        """
        try:
            self._telemetricWorkers.add(context, self._deviceManager.getDeviceIdentifier(), stateName, attributeTree, listener)
            logger.debug(f'useEffect: Added worker for state {stateName}/{attributeTree}')
        except Exception as ex:
            logger.error(ex)
            raise Exception(ex)

    def updateTelemetricState(self, stateName: str, value: object) -> None:
        """
        It takes a state name and a value, and flattens the value, and then reports the flattened value
        to the telemetric state
        
        :param stateName: The name of the state to report
        :type stateName: str
        :param value: object
        :type value: object
        """
        try:
            flatValue = TelemetricState.flattening(value)
            for attributeTree in flatValue:
                self._localTelemetricState.report(stateName, attributeTree, flatValue[attributeTree])
                logger.debug(f'updateTelemetricState: Reported state {stateName}/{attributeTree}')
        except Exception as ex:
            logger.error(ex)
            raise Exception(ex)


