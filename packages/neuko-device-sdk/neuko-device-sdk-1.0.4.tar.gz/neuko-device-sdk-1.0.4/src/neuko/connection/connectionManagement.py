import json
import os
import configparser
from ..utility.logger import Logger
from .connectionStore import ConnectionStore
from ..device.model import DeviceIdentifier
from .model import Configuration
from ..iot.model import Provider

logger = Logger("ConnectionManagement").set()
config = configparser.ConfigParser()
CONFIG_PATHNAME = 'config.ini'

class ConnectionManagement:

    def __init__(self, store: ConnectionStore) -> None:
        self._store = store
        self._defaultConfig = {}
        
        try:
            config.read(CONFIG_PATHNAME)
            if 'default' in config:
                self._defaultConfig =  config['default']
        except:
            self._defaultConfig = {}

        self._endpoint = self._readConfigDefault('endpoint', 'neuko.io')
        self._port = self._readConfigDefault('port', 443)
        self._region = self._readConfigDefault('region', 'apse-1')

    def _readConfigDefault(self, keyname: str, default = None) -> None:
        try:
            return self._defaultConfig[keyname]
        except KeyError:
            return default
        except Exception as ex:
            logger.error(ex)
            return default

    @property
    def store(self):
        """Internal property - store"""
        return self._store

    @store.setter
    def store(self, store: ConnectionStore):
        self._store = store

    @store.getter
    def store(self):
        return self._store

    def getBootstrapConnectionConfiguration(self):
        j = {
            "tier": None,
            "localConnection": {
                "ownershipToken": None,
            },
            "connection": {
                "provider": Provider.BOOTSTRAP,
                "protocols": {
                    "mqtt": {
                        "endpoint": f"bootstrap.{self._region}.{self._endpoint}",
                        "port": int(self._port),
                        "options": {
                            "rejectUnauthorized": False,
                            "ALPNProtocols": ["x-amzn-mqtt-ca"]
                        }
                    },
                    "http": {
                        "endpoint": f"bootstrap.{self._region}.{self._endpoint}",
                        "port": int(self._port),
                        "options": {
                            "keepAlive": True,
                            "rejectUnauthorized": False,
                            "ALPNProtocols": ["x-amzn-http-ca"]
                        }
                    }
                }
            }
        }
        return Configuration(**j)

    async def getPerpetualConnectionConfiguration(self, deviceIdentifier: DeviceIdentifier) -> Configuration:
        try:
            raw = await self._store.getPerpetualConnectionSettings(deviceIdentifier)
            j = json.loads(raw)
            # logger.debug(Configuration(**j))
            return Configuration(**j)
        except:
            logger.error("Error fetching perpetual configuration file")
            raise Exception("OperationError")

    async def savePerpetualConnectionConfiguration(self, deviceIdentifier: DeviceIdentifier, settings: Configuration) -> bool:
        try:
            res = await self._store.savePerpetualConnectionSettings(deviceIdentifier, json.dumps(settings, indent=4))
            if res:
                return True
            else:
                raise Exception("OperationError")
        except:
            logger.error("Error saving perpetual configuration file")
            raise Exception("OperationError")

    async def checkIfConfigurationSaved(self, deviceIdentifier: DeviceIdentifier) -> bool:
        try:
            res = await self._store.isPerpetualConnectionSettingsExists(deviceIdentifier)
            if res:
                logger.debug(f'checkIfConfigurationSaved: Perpetual settings found')
                return True
            else:
                logger.debug(f'checkIfConfigurationSaved: Perpetual settings doesnt exits')
                return False
        except:
            logger.error("Error saving perpetual configuration file")
            raise Exception("OperationError")

    async def checkIfConnectedToInternet(self) -> bool:
        try:
            res = await self._store.isConnectedToInternet()
            if res:
                return True
            else:
                return False
        except:
            logger.error("Error saving perpetual configuration file")
            raise Exception("OperationError")