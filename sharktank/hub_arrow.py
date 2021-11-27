#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from time import sleep
import RPi.GPIO as GPIO       ## Import GPIO library
from getkey import key
#import keyboard
import readchar




motorpin_left = 12 #board 32
motorpin_right = 13 #board 33        

# motor 1 (left)
relay_1 = 5 #board 29 
relay_2 = 6 #board 31
relay_3 = 17 #board 11
relay_4 = 26 #board 37

# motor 2 (right)
relay_5 = 18 #board 12 
relay_6 = 16 #board 36
relay_7 = 24 #board 18
relay_8 = 21 #board 40


GPIO.setwarnings(False)         #disable warnings
GPIO.setmode(GPIO.BCM)        #set pin numbering system
GPIO.setup(motorpin_left,GPIO.OUT)
GPIO.setup(motorpin_right,GPIO.OUT)

#Motor 1
GPIO.setup(relay_1,GPIO.OUT)
GPIO.setup(relay_2,GPIO.OUT)
GPIO.setup(relay_3,GPIO.OUT)
GPIO.setup(relay_4,GPIO.OUT)

#Motor 2
GPIO.setup(relay_5,GPIO.OUT)
GPIO.setup(relay_6,GPIO.OUT)
GPIO.setup(relay_7,GPIO.OUT)
GPIO.setup(relay_8,GPIO.OUT)


pwm_left = GPIO.PWM(motorpin_left,4000)
pwm_right = GPIO.PWM(motorpin_right,4000)#create PWM instance with frequency
pwm_left.start(0)#start PWM of required Duty Cycle 
pwm_right.start(0)#pi_pwm.ChangeDutyCycle(70)
speed_value_right= 45
speed_value_left= 45
speed_value = 40

stop_speed=0

def reverse():
    print("reverse")

    
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    
    '''time.sleep(0.5)
    GPIO.output(relay_1, GPIO.LOW) 
    GPIO.output(relay_2, GPIO.LOW)
    GPIO.output(relay_3, GPIO.LOW) 
    GPIO.output(relay_4, GPIO.LOW)
    
    
    GPIO.output(relay_5, GPIO.HIGH) 
    GPIO.output(relay_6, GPIO.HIGH)
    GPIO.output(relay_7, GPIO.HIGH) 
    GPIO.output(relay_8, GPIO.HIGH)
    
    time.sleep(0.5)'''
    
    #pwm_left.ChangeDutyCycle(speed_value)
    #pwm_right.ChangeDutyCycle(speed_value_right)
    #pwm_left.ChangeDutyCycle(speed_value_left)

def right():
    print("right")
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    
    '''time.sleep(0.2)
    
    GPIO.output(relay_1, GPIO.LOW) 
    GPIO.output(relay_2, GPIO.LOW)
    GPIO.output(relay_3, GPIO.LOW) 
    GPIO.output(relay_4, GPIO.LOW)
    
    
    
    GPIO.output(relay_5, GPIO.LOW) 
    GPIO.output(relay_6, GPIO.LOW)
    GPIO.output(relay_7, GPIO.LOW) 
    GPIO.output(relay_8, GPIO.LOW)'''
    
    time.sleep(0.2)
    
    pwm_left.ChangeDutyCycle(speed_value_left)
    #pwm_right.ChangeDutyCycle(speed_value_right)
    
    

def forward():
    print("forward")
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    
    '''time.sleep(0.2)
    
    GPIO.output(relay_1, GPIO.HIGH) 
    GPIO.output(relay_2, GPIO.HIGH)
    GPIO.output(relay_3, GPIO.HIGH)
    GPIO.output(relay_4, GPIO.HIGH)

    
    GPIO.output(relay_5, GPIO.LOW) 
    GPIO.output(relay_6, GPIO.LOW)
    GPIO.output(relay_7, GPIO.LOW) 
    GPIO.output(relay_8, GPIO.LOW)'''
    
    time.sleep(0.2)
    
    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)

def left():
    print("left")

    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    
    '''time.sleep(0.2)
    
    GPIO.output(relay_1, GPIO.HIGH) 
    GPIO.output(relay_2, GPIO.HIGH)
    GPIO.output(relay_3, GPIO.HIGH)
    GPIO.output(relay_4, GPIO.HIGH)

    
    GPIO.output(relay_5, GPIO.HIGH) 
    GPIO.output(relay_6, GPIO.HIGH)
    GPIO.output(relay_7, GPIO.HIGH) 
    GPIO.output(relay_8, GPIO.HIGH)'''
    
    time.sleep(0.2)
    
    #pwm_left.ChangeDutyCycle(speed_value_right)
    pwm_right.ChangeDutyCycle(speed_value_right)


def stop():
    print("stop")
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    #GPIO.cleanup()
    #GPIO.output(relay_1, GPIO.LOW) #Active le contrôle du GPIO
    #GPIO.output(relay_2, GPIO.LOW)
 




def drive(data):
   # unbrake()
    if data.data == 'w':
        forward()
    elif data.data == 'a' :
        left()
    elif data.data == 's':
        reverse()
    elif data.data == 'd':
        right()
    '''
    elif data.data == ' ':
        brake()
    '''
    sleep(0.04)
    stop()
    

def driveMotor():
    rospy.init_node('driveMotor',anonymous=True)
    rospy.Subscriber('keys', String, drive)
    rospy.spin()

if __name__ == '__main__':
    try:
        driveMotor()
    finally:
        GPIO.cleanup()
