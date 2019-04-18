'''
Updated on April 14, 2019

@author: Jaydeep Shah
@author: Venkat Prasad Krishnamurthy
'''


from mqttSubClient import mqttSubClient

from weather import Display


sub = mqttSubClient()
disp = Display()


sub.start()


disp.start()
