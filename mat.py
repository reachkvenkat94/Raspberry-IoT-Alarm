'''
Updated on April 14, 2019

@author: Jaydeep Shah
@author: Venkat Prasad Krishnamurthy
'''

from threading import Thread 
import RPi.GPIO as GPIO
from time import sleep
import paho.mqtt.client as mqtt

class mat(Thread):

	def __init__(self):
                self.matPin = 8
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(self.matPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
                print("MAT Activated")
                self.time2stand = 4  #in seconds
                self.flag_readMaT = True
                self.clientPub = mqtt.Client()
                self.payload_1 = "off"
                self.payload_2 = "done"
                Thread.__init__(self)

	def run(self):
                
                while(self.flag_readMaT):
                        print("Entering While 1 loop")
                        while(GPIO.input(self.matPin)):
                                #Basically do nothing and wait till someone stands on the MAT.
                                #When a person stands on maat, "0" would be read on matPin (because matPin is pulled up)
                                pass
                        print("Whena user stands for 4 seconds it will stop alarm")
                        sleep(self.time2stand)
                        if(GPIO.input(self.matPin) == False):
                                self.flag_readMaT = False
                                print("User completed the task")
                                self.clientPub.connect("iot.eclipse.org", 1883, 60)
                                self.clientPub.publish("matsensor", self.payload_1, 1, retain=False)
                                print("matsensor")
                                self.clientPub.publish("useractivity", self.payload_2, 1, retain=False)
                                print("useractivity")
                                self.clientPub.disconnect()
                
