'''
Created on Feb 25, 2019
Program is used to subscribe to a topic from a MQTT broker

@author: Venkat Prasad Krishnamurthy
'''
from labbenchstudios.common import ConfigConst
from labbenchstudios.common.ConfigUtil import ConfigUtil
from labs.module06.MqttClientConnector import MqttClientConnector
from labs.common.DataUtil import DataUtil
import logging

'''
Setting values for Topic and address for MQTT broker
'''
topic = "Temperature Sensor"

subscribe = MqttClientConnector(topic)
subscribe.subscribe(host)                  # Connecting to MQTT Broker
msg = subscribe.message()                  # Subscribing to specefied Topic
logging.debug('JSon Data Received:')
print("Json Data Received:\n "+str(msg)+"\n")

data = DataUtil();
sensor = data.toSensorfromJson(msg)        # Converting Json data to Sensor Data
logging.debug('Json data converted into SensorData')
print("Received message in SensorData format"+str(sensor))

json = data.toJsonfromSensor(sensor)
logging.debug('SensorData converted into Json Data: ')
print('SensorData converted to Json Data again: \n'+str(json))
