
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
        kit.servo[14].angle = x
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
        kit.servo[14].angle = x
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
        kit.servo[14].angle = x
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
        kit.servo[14].angle = x
        sleep(0.018)
        
    for x in range(right_elbow_up,right_elbow_down,-1):
        print(" right elbow down")
        kit.servo[14].angle = x
        sleep(0.018)

    for x in range(right_shoulder_up,right_shoulder_down,1):
        print(" right shoulder down")
        kit.servo[8].angle = x
        sleep(0.018)




def shake_hand_left():


    import time

    #Motor Imports
    from time import sleep

    import threading
    from adafruit_servokit import ServoKit 
    import adafruit_motor.servo

    kit = ServoKit(channels=16)


    left_shoulder_down = 0
    left_shoulder_up = 50

    left_elbow_down = 20
    left_elbow_up = 170

    left_elbow_center =90
    left_elbow_left = 30 
    left_elbow_right = 150

    left_wrist_center = 65
    left_wrist_right = 180
    left_wrist_left = 0


    left_thumb_open = 0
    left_thumb_close = 0

    left_fingers_open = 0
    left_fingers_close = 0




    kit.servo[1].angle  = left_elbow_center

    kit.servo[5].angle  = left_wrist_center
           

    for x in range(left_shoulder_down,left_shoulder_up,1):
        print("SHOULDER UP")
        kit.servo[0].angle = x
        sleep(0.018)

    for x in range(left_elbow_down,left_elbow_up,1):
        print("ELBOW UP")
        kit.servo[2].angle = x
        sleep(0.018)
    
    for x in range(left_thumb_open,left_thumb_close,1):
        print("THUMB CLOSE")
        kit.servo[7].angle = x
        sleep(0.0001)

    for x in range(left_fingers_open,left_fingers_close,1):
        print("FINGERS CLOSE")
        kit.servo[6].angle = x
        sleep(0.0001)
    
    #if "__name__" == "__main__":
	
    kit.servo[6].angle = 110
    kit.servo[7].angle = 110
    print("bbb")
    kit.servo[6].angle = 120
    kit.servo[7].angle = 120
    print("bbb")
    sleep(1)

    kit.servo[6].angle = 110
    kit.servo[7].angle = 110

    sleep(2)

    kit.servo[6].angle = 90
    kit.servo[7].angle = 90
	
    sleep(1)

    kit.servo[6].angle = 110
    kit.servo[7].angle = 110

    sleep(1)
    
    '''for x in range(left_thumb_close,left_thumb_open,1):
        print("THUMB OPEN")
        kit.servo[7].angle = x
        sleep(0.0001)

    for x in range(left_fingers_close,left_fingers_open,1):
        print("FINGERS open")
        kit.servo[6].angle = x
        sleep(0.0001)'''


    for x in range(left_elbow_up,left_elbow_down,-1):
        print("ELBOW DOWN")
        kit.servo[2].angle = x
        sleep(0.018)
    
    for x in range(left_shoulder_up,left_shoulder_down,-1):
        print("SHOULDER DOWN")
        kit.servo[0].angle = x
        sleep(0.018)


def wave_hand_left():



    import time

    #Motor Imports
    from time import sleep

    import threading
    from adafruit_servokit import ServoKit 
    import adafruit_motor.servo

    kit = ServoKit(channels=16)


    left_shoulder_down = 0
    left_shoulder_up = 120

    left_elbow_down = 40
    left_elbow_up = 150

    left_elbow_center =90
    left_elbow_left = 30 
    left_elbow_right = 150

    left_wrist_center = 65
    left_wrist_right = 180
    left_wrist_left = 0


    left_thumb_open = 0
    left_thumb_close = 0

    left_fingers_open = 0
    left_fingers_close = 0


    kit.servo[1].angle  = left_elbow_center

    kit.servo[5].angle  = left_wrist_center





    for x in range(left_shoulder_down,left_shoulder_up,1):
        print("SHOULDER UP")
        kit.servo[0].angle = x
        sleep(0.010)

    for x in range(left_elbow_down,left_elbow_up,1):
        print("ELBOW UP")
        kit.servo[2].angle = x
        sleep(0.010)

    for x in range(left_wrist_center,left_wrist_right,1):
        print("ELBOW UP")
        kit.servo[5].angle = x
        sleep(0.010)


    for x in range(left_elbow_center,left_elbow_right,1):
        print("left elbow right")
        kit.servo[1].angle = x
        sleep(0.010)

    for x in range(left_elbow_right,left_elbow_left,-1):
        print("left elbow left")
        kit.servo[1].angle = x
        sleep(0.010)


    for x in range(left_elbow_left,left_elbow_center,1):
        print("left elbow left")
        kit.servo[1].angle = x
        sleep(0.010)


    for x in range(left_wrist_right,left_wrist_center,-1):
        print("ELBOW UP")
        kit.servo[5].angle = x
        sleep(0.010)


    
    for x in range(left_elbow_up,left_elbow_down,-1):
        print("ELBOW DOWN")
        kit.servo[2].angle = x
        sleep(0.010)
    ##################################################################

    
    for x in range(left_shoulder_up,left_shoulder_down,-1):
        print("SHOULDER DOWN")
        kit.servo[0].angle = x
        sleep(0.010)



def head_yes():


    import time

    #Motor Imports
    from time import sleep

    import threading
    from adafruit_servokit import ServoKit 
    import adafruit_motor.servo

    kit = ServoKit(channels=16)


    head_down = 50
    head_up = 90

    head_left = 120
    head_right= 60
    head_center= 90
    
    kit.servo[3].angle = head_center
    for x in range(head_up,head_down,1):
        print("HEAD DOWN")
        kit.servo[4].angle = x
        sleep(0.018)
    
    for x in range(head_down,head_up,-1):
        print("HEAD UP")
        kit.servo[4].angle = x
        sleep(0.018)
    

def head_no():


    import time

    #Motor Imports
    from time import sleep

    import threading
    from adafruit_servokit import ServoKit 
    import adafruit_motor.servo

    kit = ServoKit(channels=16)


    head_down = 50
    head_up = 90

    head_left = 120
    head_right= 60
    head_center= 90
    
    for x in range(head_center,head_left1,1):
        print("HEAD right")
        kit.servo[3].angle = x
        sleep(0.018)
    for x in range(head_left1,head_center,-1):
        print("HEAD center")
        kit.servo[3].angle = x
        sleep(0.018)
    for x in range(head_center,head_right1,-1):
        print("HEAD left")
        kit.servo[3].angle = x
        sleep(0.018)
    for x in range(head_right1,head_center,1):
        print("HEAD center")
        kit.servo[3].angle = x
        sleep(0.018)


def motor_test():


    import time

    #Motor Imports
    from time import sleep

    import threading
    from adafruit_servokit import ServoKit 
    import adafruit_motor.servo

    kit = ServoKit(channels=16)


    left_shoulder_down = 0
    left_shoulder_up = 50


    left_elbow_down = 170
    left_elbow_up = 20

    left_elbow_center =50
    left_elbow_left = 70     
    left_elbow_right = 130




    #kit.servo[8].angle = left_elbow_center        
    for x in range(left_elbow_center,left_elbow_left,-1):
        
        kit.servo[8].angle = x
        sleep(0.018)

    for x in range(left_elbow_left,left_elbow_center,1):
        
        kit.servo[8].angle = x
        sleep(0.018)


    
if __name__ == "__main__":
    
    #shake_hand_left()
    #wave_hand_left()
    shake_hand_right()
    #wave_hand_right()
    #head_yes()
    #head_no()
    
