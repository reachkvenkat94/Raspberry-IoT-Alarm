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
		self.topic_sen = "IoT Mat"
		self.host = "test.mosquitto.org"
		self.alarm = Alarm(1,False,False)
		self.mat = Mat()
		
	def run(self):
		mqt = MqttClientConnector(self.topic_sen)
		mqt.subscribe(host)                  # Connecting to MQTT Broker
		msg = mqt.message()                  # Subscribing to specefied Topic
		self.alarm = self.alarm.toAlarmfromJson(msg)
		if self.alarm.sense_flag == True:
			self.mat.checkStatus()
			if self.alarm.act_flag == True:
				mqt.publish(self.topic,self.alarm.toJsonFromAlarm(),self.host)
				self.alarm.act_flag = False
		
			
