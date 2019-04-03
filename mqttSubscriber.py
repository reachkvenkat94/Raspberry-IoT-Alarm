'''
Created on Feb 25, 2019
Program is used to subscribe to a topic from a MQTT broker

@author: Venkat Prasad Krishnamurthy
'''


'''
Setting values for Topic and address for MQTT broker
'''

class MqttSubscriber(Thread):

	def __init__(self, name):
		'''
		Constructor
		'''
		Thread.__init__(self);
		self.enableEmulator = True; # flag to enable emulator function
		self.topic_sen = "Activate Mat"
		
	def run(self):
		subscribe = MqttClientConnector(self.topic_sen)
		subscribe.subscribe(host)                  # Connecting to MQTT Broker
		msg = subscribe.message()                  # Subscribing to specefied Topic
		print("Json Data Received:\n "+str(msg)+"\n")
		json = data.toJsonfromSensor(sensor)
		print('SensorData converted to Json Data again: \n'+str(json))
