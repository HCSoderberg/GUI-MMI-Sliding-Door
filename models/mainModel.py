from .logginModel import LogginModel
from .settingsModel import SettingsModel
from .errorMessageModel import ErrorMessageModel
from .modeSelectorModel import ModeSelectorModel
from servercom.publishHandler import PublishHandler
from servercom.receiveHandler import ReceiveHandler
import paho.mqtt.client as mqtt
class Model:
    def __init__(self):
        self.publisher = PublishHandler()
        self.logginmodel= LogginModel()
        self.settingmodel = SettingsModel()
        self.receiverThread = ReceiveHandler()
        self.receiverThread.start()
        self.publisher.start()
        self.errormessagemodel = ErrorMessageModel()
        self.modeselectormodel = ModeSelectorModel()
        #print("Model initiated")