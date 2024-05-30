import paho.mqtt.client as mqtt
from models.observablemodel import ObservableModel
from models.mainModel import ErrorMessageModel
#from models.errorMessageModel import ErrorMessageModel
import time 
import threading
import json

# ERRORMESSAGE EXAMPLE b'{"id":[37,53]}'

class ErrorMessage:
    errorNr = None
    errorName = None
    errorDescription = None

    def __init__(self, errorNr):
        self.errorNr = errorNr
        if(errorNr == 37):
            self.errorName = "IO Disconnected"
            self.errorDescription = "Lost connection with IO"
        elif (errorNr == 152):
            self.errorName = "Power supply error"
            self.errorDescription = "Something is wrong with the power Supply to the operator"




class ReceiveHandler(ErrorMessageModel, threading.Thread): 
    modedict = {
        0 : "Closed",
        1: "Exit only",
        2: "Automatic", 
        3: "Auto partial", 
        4: "Hold open"
    }
    lastErrorList = []
    def on_connect(self, mqttc, obj, flags, rc, properties):
        print("Connected receiver with resultcode {0}", format(str(rc)))

    def __init__(self):
        threading.Thread.__init__(self)
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Receiver")
        self.client.on_connect=self.on_connect
        self.client.on_message=self.on_message
        self.client.connect('127.0.0.1',1883)
        self.client.subscribe('e/testdevice/slidingDoor/OpMo')
        self.client.subscribe('e/testdevice/slidingDoor/ErIn_v2')
        self.client.publish('Receiver is connected','')

    def on_connect_fail(self, mqttc, obj):
        print("Connect failed")

    def on_message(self, mqttc, obj, msg):
        if msg.topic == "e/testdevice/slidingDoor/ErIn_v2":
            print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
            integers_list = json.loads(msg.payload)
            errorList = integers_list["id"]
            if not errorList == self.lastErrorList:
                self.newErrorList(errorList)
            self.lastErrorList = errorList
        if msg.topic == "e/testdevice/slidingDoor/OpMo":
            modemsg = json.loads(msg.payload)
            modeid = modemsg["mode"]
            if self.modedict.__contains__(modeid):
                mode = self.modedict.get(modeid)
                with open('settings.txt','w') as file: 
                    file.write(mode) 
                print("mode wrote to file:" + mode)
                self.trigger()


    
            
             

    

     
    def run(self):

        rc = 0
        while rc == 0:
            rc = self.client.loop()
