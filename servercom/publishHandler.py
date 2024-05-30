import paho.mqtt.client as mqtt

import time 
import threading

class PublishHandler(threading.Thread): 
    
    def on_connect(self, mqttc, obj, flags, rc, properties):
        print("Connected receiver with resultcode {0}", format(str(rc)))


    def __init__(self):
        threading.Thread.__init__(self)
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Transmitter")
        self.client.on_connect=self.on_connect
        self.client.connect('127.0.0.1',1883)
        self.client.publish('Transmitter is connected','')

    def publish(self, msg, payload):
        self.client.publish(msg,payload)
    
    def run(self):
        
        rc = 0
        while rc == 0:
            rc = self.client.loop()
            time.sleep(5)
                # USED TO ASK FOR FOR ERROR AND OPERATING MODE
            #self.publish('c/testdevice/slidingDoor/ErIn', '')
            #self.publish('c/testdevice/slidingDoor/OpMo','')
                # USED TO SIMULATE INCOMING ERRORS FROM DOOR
            self.publish('e/testdevice/slidingDoor/ErIn_v2', '{"id":[1,2]}')
            
            