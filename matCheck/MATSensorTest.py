#!/usr/bin/env python

'''
Created on April 14, 2019


@author: Jaydeep Shah
'''

import RPi.GPIO as GPIO
from time import sleep

matPin = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(matPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print("MAT Activated")
flag_readMaT = True

while(flag_readMaT):
    print("Entering While 1 loop")
    while(GPIO.input(matPin)):
        pass
    print("If you stand for 12 seconds it will stop alarm")
    sleep(12)
    if(GPIO.input(matPin) == False):
        flag_readMaT = False
        print("User completed the task")

