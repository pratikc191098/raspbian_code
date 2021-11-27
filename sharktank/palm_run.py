
import time

#Motor Imports
from time import sleep

import threading
from adafruit_servokit import ServoKit 
import adafruit_motor.servo

kit = ServoKit(channels=16)


def palm_open():

    kit.servo[12].angle = 110        
    kit.servo[13].angle = 110

    kit.servo[12].angle = 70       
    kit.servo[13].angle = 70
        
    sleep(1)

    kit.servo[12].angle = 110        
    kit.servo[13].angle = 110

    kit.servo[12].angle = 130        
    kit.servo[13].angle = 130
    
    sleep(1)

    kit.servo[12].angle = 110        
    kit.servo[13].angle = 110
    