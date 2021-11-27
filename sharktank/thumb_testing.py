


import time

    #Motor Imports
from time import sleep

import threading
from adafruit_servokit import ServoKit 
import adafruit_motor.servo

kit = ServoKit(channels=16)



#kit.servo[7].angle  = 110


kit.servo[7].angle  = 120
kit.servo[6].angle  = 120

sleep(1)

kit.servo[7].angle  = 90
kit.servo[6].angle  = 90

sleep(1)

kit.servo[7].angle  = 110
kit.servo[6].angle  = 110

