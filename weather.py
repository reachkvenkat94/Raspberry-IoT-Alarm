'''
Created on Apr 16, 2019

@author: Venkat Prasad Krishnamurthy
@author: Jaydeep Shah
'''
from threading import Thread
import pyowm
import datetime
from time import sleep 
import serial


class Display(Thread):
    '''
    classdocs
    '''


    def _init_(self):
        '''
        Constructor
        '''
        Thread._init_(self);
        self.enableEmulator = True;
        self.ser = serial.Serial('/dev/ttyACM0',9600)
        
    def run(self):
        while self.enableEmulator == True:
            owm = pyowm.OWM('270e9c1fe2c20c42dc7857efedc17320')
            boston = owm.weather_at_place('Boston,US')
            weather = boston.get_weather()
            temp = weather.get_temperature('fahrenheit')['temp']
            #print(temp)
            now = datetime.datetime.now()
            time = now.strftime("%H:%M")
            stri = str(time)+"w"+str(temp);
            #print(time)
            seri = str.encode(stri)
            self.ser.write(seri)
            
            sleep(5)