'''
Created on Feb 25, 2019
This Class is used to connect to a MQTT broker for publishing and subscription

@author: Venkat Prasad Krishnamurthy
'''


class Alarm():
	id = 0
	sense_flag = False
	act_flag = False
	
	def __init__(self,id,sense,act):
        self.id = id
		self.sense_flag = sense
		self.act_flag = act
		
	def enableNotifiFlag(self):
		self.sense_flag = True
	
	def disableNotifiFlag(self):
		self.sense_flag = False
		
	def enableActFlag(self):
		self.act_flag = True
		
	def disableActFlag(self):
		self.act_flag = False
	
	def toJsonFromAlarm(self,alarm):
		return json
	
	def toAlarmfromJson(self,js):
		return alarm