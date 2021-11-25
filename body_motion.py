import time

#Motor Imports
from time import sleep

import threading
from adafruit_servokit import ServoKit 
import adafruit_motor.servo

kit = ServoKit(channels=16)

def all_motor():
    
    import time

    #Motor Imports
    from time import sleep

    import threading
    from adafruit_servokit import ServoKit 
    import adafruit_motor.servo

    kit = ServoKit(channels=16)


    left_shoulder_down = 0
    left_shoulder_up = 90

    left_elbow_down = 20
    left_elbow_up = 170

    left_elbow_center =0
    left_elbow_left = 0
    left_elbow_right = 130

    kit.servo[1].angle = left_elbow_center       

    for x in range(left_shoulder_down,left_shoulder_up,1):
        print("SHOULDER UP")
        kit.servo[0].angle = x
        sleep(0.018)

    for x in range(left_elbow_down,left_elbow_up,1):
        print("ELBOW UP")
        kit.servo[2].angle = x
        sleep(0.018)
    
    def motor_3():
        
        for x in range(left_elbow_down,left_elbow_up,1):
            print("m3")
            kit.servo[3].angle = x
            sleep(0.018)
        for x in range(left_elbow_up,left_elbow_down,-1):
            print("m3")
            kit.servo[3].angle = x
            sleep(0.018)

        
        
    def motor_4():
        
        for x in range(left_elbow_down,left_elbow_up,1):
            print("m4")
            kit.servo[4].angle = x
            sleep(0.018)
        for x in range(left_elbow_up,left_elbow_down,-1):
            print("m4")
            kit.servo[4].angle = x
            sleep(0.018)

        
        
    def motor_5():

        for x in range(left_elbow_down,left_elbow_up,1):
            print("m5")
            kit.servo[5].angle = x
            sleep(0.018)
        for x in range(left_elbow_up,left_elbow_down,-1):
            print("m5")
            kit.servo[5].angle = x
            sleep(0.018)
        
    x = threading.Thread(target=motor_3, args=())
    y = threading.Thread(target=motor_4, args=())
    z = threading.Thread(target=motor_5, args=())
    
    x.start()
    y.start()
    z.start()
    
    sleep(3)
    
    
    for x in range(left_elbow_up,left_elbow_down,-1):
        print("ELBOW DOWN")
        kit.servo[2].angle = x
        sleep(0.018)
    
    for x in range(left_shoulder_up,left_shoulder_down,-1):
        print("SHOULDER DOWN")
        kit.servo[0].angle = x
        sleep(0.018)

    
    
#    if __name__ == "__main__":
        
        
    
    


def shake_hand_left():


    import time

    #Motor Imports
    from time import sleep

    import threading
    from adafruit_servokit import ServoKit 
    import adafruit_motor.servo

    kit = ServoKit(channels=16)


    left_shoulder_down = 0
    left_shoulder_up = 90

    left_elbow_down = 20
    left_elbow_up = 170

    left_elbow_center =0
    left_elbow_left = 0
    left_elbow_right = 130




    kit.servo[1].angle = left_elbow_center       

    for x in range(left_shoulder_down,left_shoulder_up,1):
        print("SHOULDER UP")
        kit.servo[0].angle = x
        sleep(0.018)

    for x in range(left_elbow_down,left_elbow_up,1):
        print("ELBOW UP")
        kit.servo[2].angle = x
        sleep(0.018)
###########################################################
    for x in range(left_elbow_down,left_elbow_up,1):
        print("m3")
        kit.servo[3].angle = x
        sleep(0.018)

    for x in range(left_elbow_down,left_elbow_up,1):
        print("m4")
        kit.servo[4].angle = x
        sleep(0.018)


    for x in range(left_elbow_down,left_elbow_up,1):
        print("m5")
        kit.servo[5].angle = x
        sleep(0.018)



    sleep(2)

    for x in range(left_elbow_up,left_elbow_down,-1):
        print("m3")
        kit.servo[3].angle = x
        sleep(0.018)
        
    for x in range(left_elbow_up,left_elbow_down,-1):
        print("m4")
        kit.servo[4].angle = x
        sleep(0.018)

    for x in range(left_elbow_up,left_elbow_down,-1):
        print("m5")
        kit.servo[5].angle = x
        sleep(0.018)
########################################################################

    for x in range(left_elbow_up,left_elbow_down,-1):
        print("ELBOW DOWN")
        kit.servo[2].angle = x
        sleep(0.018)
    
    for x in range(left_shoulder_up,left_shoulder_down,-1):
        print("SHOULDER DOWN")
        kit.servo[0].angle = x
        sleep(0.018)

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
    
    right_elbow_down = 80
    right_elbow_up = 180

    right_elbow_center =145
    right_elbow_left = 0
    right_elbow_right = 180
    
    kit.servo[6].angle = right_elbow_center
    	

    for x in range(right_shoulder_down,right_shoulder_up,-1):
        print(" right SHOULDER UP")
        kit.servo[5].angle = x
        sleep(0.018)

    for x in range(right_elbow_down,right_elbow_up,1):
        print(" right elbow UP")
        kit.servo[7].angle = x
        sleep(0.018)


    sleep(5)

    for x in range(right_elbow_up,right_elbow_down,-1):
        print(" right elbow down")
        kit.servo[7].angle = x
        sleep(0.018)


    for x in range(right_shoulder_up,right_shoulder_down,1):
        print(" right SHOULDER down")
        kit.servo[5].angle  = x
        sleep(0.018)


def head_yes():


    import time

    #Motor Imports
    from time import sleep

    import threading
    from adafruit_servokit import ServoKit 
    import adafruit_motor.servo

    kit = ServoKit(channels=16)


    head_down = 70
    head_up = 110

    head_left1 = 120
    head_right1= 60
    head_center= 90

    for x in range(head_up,head_down,-1):
        print("HEAD DOWN")
        kit.servo[4].angle = x
        sleep(0.018)
    
    for x in range(head_down,head_up,1):
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


    head_down = 70
    head_up = 110

    head_left1 = 140
    head_right1= 60
    head_center= 100

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
    '''head_yes()
    sleep(1)
    head_no()
    sleep(1)
    shake_hand_left()
    sleep(1)'''
    #shake_hand_left()
    all_motor()
    #shake_hand_right()
    