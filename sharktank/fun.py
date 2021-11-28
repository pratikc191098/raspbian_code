from time import sleep
import threading
from adafruit_servokit import ServoKit
import adafruit_motor.servo
kit = ServoKit(channels=16)


def run_servo(pos1,pos2,servo_pin):
    speed = 0.018
    if pos1 > pos2:
        for x in range (pos1,pos2,1):
            kit.servo[servo_pin].angle = x
            sleep(speed)
    if pos1 == pos2:
        for x in range (pos1,pos2,1):
            kit.servo[servo_pin].angle = x
            sleep(speed)                
    else:
        for x in range (pos1,pos2,-1):
            kit.servo[servo_pin].angle = x
            sleep(speed)
            
def servo1():
    run_servo(100,0,15)
    
if __name__ == "__main__":
    servo1()
    
    