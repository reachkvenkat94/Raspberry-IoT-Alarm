'''
Updated on April 14, 2019

@author: Jaydeep Shah
@author: Venkat Prasad Krishnamurthy
'''


#Topic 1: matsensor = on / off
#Topic 2: useractivity = done/undone

import paho.mqtt.client as mqtt
import mqttSubConnector as cbF
import time
from threading import Thread

'''
This class provides methods for subscriber.
It assigns customized callbacks that we have created to its original callbacks
'''
class mqttSubClient(Thread):
    
    clientSub = mqtt.Client()
    
    '''
    This is the default constructor
    It assigns the customized callbacks to its original callbacks
    '''
    def __init__(self):        
        self.clientSub.on_connect = cbF.on_connect_sub
        self.clientSub.on_message = cbF.on_message
        self.clientSub.on_disconnect = cbF.on_disconnect
        self.clientSub.on_subscribe = cbF.on_subscribe
        Thread.__init__(self)
        print("This is a Subscriber Client running.") 
    
    '''
    This function subscribes to a topic on the MQTT broker after connecting to a
    broke. It also starts the forever loop.
    '''
    def mySubscribe(self):
        self.clientSub.connect("iot.eclipse.org", 1883, 60)
        self.clientSub.loop_forever()
        time.sleep(65)
        
    
    '''
    This is called when thread is started. It calls for the subscription.
    '''     
    def run(self):
        Thread.run(self)
        self.mySubscribe()		
	
