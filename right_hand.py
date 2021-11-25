import time

#Motor Imports
from time import sleep

import threading
from adafruit_servokit import ServoKit 
import adafruit_motor.servo

kit = ServoKit(channels=16)

def shake_hand_right():

    import time

    #Motor Imports
    from time import sleep

    import threading
    from adafruit_servokit import ServoKit 
    import adafruit_motor.servo

    kit = ServoKit(channels=16)

    right_shoulder_down = 180
    right_shoulder_up = 130
    
    right_elbow_down = 0
    right_elbow_up = 50

    right_elbow_center =90
    right_elbow_left = 0
    right_elbow_right = 180
    
    right_wrist_center = 115
    right_wrist_right = 180
    right_wrist_left = 0
    
    kit.servo[9].angle = right_elbow_center
    kit.servo[11].angle = right_wrist_center

    for x in range(right_shoulder_down,right_shoulder_up,-1):
        print(" right SHOULDER UP")
        kit.servo[8].angle = x
        sleep(0.018)

    for x in range(right_elbow_down,right_elbow_up,1):
        print(" right elbow UP")
        kit.servo[10].angle = x
        sleep(0.018)
        
    def palm_close():
        
        kit.servo[12].angle = 110        
        kit.servo[13].angle = 110

        kit.servo[12].angle = 130        
        kit.servo[13].angle = 130
        
        sleep(1)

        kit.servo[12].angle = 110        
        kit.servo[13].angle = 110

        
    def  palm_open():

        kit.servo[12].angle = 110        
        kit.servo[13].angle = 110

        kit.servo[12].angle = 90        
        kit.servo[13].angle = 90
        
        sleep(1)

        kit.servo[12].angle = 110        
        kit.servo[13].angle = 110

    palm_close()
    sleep(2)
    palm_open()
    
    for x in range(right_elbow_up,right_elbow_down,-1):
        print(" right elbow down")
        kit.servo[10].angle = x
        sleep(0.018)


    for x in range(right_shoulder_up,right_shoulder_down,1):
        print(" right SHOULDER down")
        kit.servo[8].angle  = x
        sleep(0.018)


def wave_hand_right():

    import time

    #Motor Imports
    from time import sleep

    import threading
    from adafruit_servokit import ServoKit 
    import adafruit_motor.servo

    kit = ServoKit(channels=16)

    right_shoulder_down = 180
    right_shoulder_up = 100
    
    right_elbow_down = 0
    right_elbow_up = 90

    right_elbow_center =90
    right_elbow_left = 0
    right_elbow_right = 180
    
    right_wrist_center = 115
    right_wrist_right = 180
    right_wrist_left = 0
    
    #kit.servo[9].angle = right_elbow_center
    #kit.servo[11].angle = right_wrist_center

    for x in range(right_shoulder_down,right_shoulder_up,-1):
        print(" right SHOULDER UP")
        kit.servo[8].angle = x
        sleep(0.018)

    for x in range(right_elbow_down,right_elbow_up,1):
        print(" right elbow UP")
        kit.servo[10].angle = x
        sleep(0.018)
    
    for x in range(right_wrist_center,right_wrist_left,-1):
        print(" right wrist left")
        kit.servo[11].angle = x
        sleep(0.018)

    for x in range(right_elbow_center,right_elbow_left,-1):
        print(" right elbow left")
        kit.servo[9].angle = x
        sleep(0.018)

    for x in range(right_elbow_left,right_elbow_right,1):
        print(" right elbow right")
        kit.servo[9].angle = x
        sleep(0.018)

    for x in range(right_elbow_right,right_elbow_center,-1):
        print(" right elbow center")
        kit.servo[9].angle = x
        sleep(0.018)

    for x in range(right_wrist_left,right_wrist_center,1):
        print(" right wrist center")
        kit.servo[11].angle = x
        sleep(0.018)
        
    for x in range(right_elbow_up,right_elbow_down,-1):
        print(" right elbow down")
        kit.servo[10].angle = x
        sleep(0.018)
        
    for x in range(right_elbow_up,right_elbow_down,-1):
        print(" right elbow down")
        kit.servo[10].angle = x
        sleep(0.018)

    for x in range(right_shoulder_up,right_shoulder_down,1):
        print(" right shoulder down")
        kit.servo[8].angle = x
        sleep(0.018)

if __name__ == "__main__":
    
    wave_hand_right()
    