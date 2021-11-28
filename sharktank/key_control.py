import RPi.GPIO as GPIO
from time import sleep
import time
#import keyboard
import readchar

motorpin_left = 12 #32
motorpin_right = 13 #33

#Motor1 pins
relay_1 = 5 #29 
relay_2 =  6 #31
relay_3 = 17 #11
relay_4 = 26 #37

#Motor2 pins
relay_5 =  18 #12
relay_6 = 16 # 36
relay_7 = 24 #18 
relay_8 = 21 #40

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






import time

#Motor Imports
from time import sleep

import threading
from adafruit_servokit import ServoKit 
import adafruit_motor.servo

kit = ServoKit(channels=16)


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

    left_elbow_center =100
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
    
    '''for x in range(left_thumb_open,left_thumb_close,1):
        print("THUMB CLOSE")
        kit.servo[7].angle = x
        sleep(0.0001)

    for x in range(left_fingers_open,left_fingers_close,1):
        print("FINGERS CLOSE")
        kit.servo[6].angle = x
        sleep(0.0001)'''
    
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

def shake_hand_right():
    import time

    #Motor Imports
    from time import sleep

    import threading
    from adafruit_servokit import ServoKit 
    import adafruit_motor.servo

    kit = ServoKit(channels=16)

    right_shoulder_down = 180
    right_shoulder_up = 80
    
    right_elbow_down = 180
    right_elbow_up = 50

    right_elbow_center =90
    right_elbow_left = 30
    right_elbow_right = 140

    right_wrist_center =170 
    right_wrist_right =0
    right_wrist_left =180

    kit.servo[9].angle = right_elbow_center
    	

    for x in range(right_shoulder_down,right_shoulder_up,-1):
        print(" right SHOULDER UP")
        kit.servo[8].angle = x
        sleep(0.018)

    for x in range(right_elbow_down,right_elbow_up,-1):
        print(" right elbow UP")
        kit.servo[14].angle = x
        sleep(0.018)


    sleep(5)

    for x in range(right_elbow_up,right_elbow_down,1):
        print(" right elbow down")
        kit.servo[14].angle = x
        sleep(0.018)


    for x in range(right_shoulder_up,right_shoulder_down,1):
        print(" right SHOULDER down")
        kit.servo[8].angle  = x
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



def reverse():
    print("reverse")

    
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    
    time.sleep(0.5)
    GPIO.output(relay_1, GPIO.LOW) 
    GPIO.output(relay_2, GPIO.LOW)
    GPIO.output(relay_3, GPIO.LOW) 
    GPIO.output(relay_4, GPIO.LOW)
    
    
    GPIO.output(relay_5, GPIO.HIGH) 
    GPIO.output(relay_6, GPIO.HIGH)
    GPIO.output(relay_7, GPIO.HIGH) 
    GPIO.output(relay_8, GPIO.HIGH)
    
    time.sleep(0.5)
    
    #pwm_left.ChangeDutyCycle(speed_value)
    #pwm_right.ChangeDutyCycle(speed_value_right)
    #pwm_left.ChangeDutyCycle(speed_value_left)

def right():
    print("right")
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    
    time.sleep(0.2)
    
    GPIO.output(relay_1, GPIO.LOW) 
    GPIO.output(relay_2, GPIO.LOW)
    GPIO.output(relay_3, GPIO.LOW) 
    GPIO.output(relay_4, GPIO.LOW)
    
    
    
    GPIO.output(relay_5, GPIO.LOW) 
    GPIO.output(relay_6, GPIO.LOW)
    GPIO.output(relay_7, GPIO.LOW) 
    GPIO.output(relay_8, GPIO.LOW)
    
    time.sleep(0.2)
    
    pwm_left.ChangeDutyCycle(speed_value_left)
    #pwm_right.ChangeDutyCycle(speed_value_right)
    
    

def forward():
    print("forward")
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    
    time.sleep(0.2)
    
    GPIO.output(relay_1, GPIO.HIGH) 
    GPIO.output(relay_2, GPIO.HIGH)
    GPIO.output(relay_3, GPIO.HIGH)
    GPIO.output(relay_4, GPIO.HIGH)

    
    GPIO.output(relay_5, GPIO.LOW) 
    GPIO.output(relay_6, GPIO.LOW)
    GPIO.output(relay_7, GPIO.LOW) 
    GPIO.output(relay_8, GPIO.LOW)
    
    time.sleep(0.2)
    
    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)

def left():
    print("left")

    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    
    time.sleep(0.2)
    
    GPIO.output(relay_1, GPIO.HIGH) 
    GPIO.output(relay_2, GPIO.HIGH)
    GPIO.output(relay_3, GPIO.HIGH)
    GPIO.output(relay_4, GPIO.HIGH)

    
    GPIO.output(relay_5, GPIO.HIGH) 
    GPIO.output(relay_6, GPIO.HIGH)
    GPIO.output(relay_7, GPIO.HIGH) 
    GPIO.output(relay_8, GPIO.HIGH)
    
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
    



if __name__ == "__main__":
    try:
        while True:
            print("you can enter: up, down, left, right, 1,2,3")
            key = readchar.readkey()
                    
                    
            if(key == None):
                print('stopped')
                continue
                    
            if (key == '\x1b\x5b\x41'): #forward
                print("forward")
                forward()
            if (key == '\x1b\x5b\x42'):#backward
                print("backward")
                reverse()
            if (key == '\x1b\x5b\x44'): #left
                print("left")
                left()
            if (key == '\x1b\x5b\x43'): #right
                print("right")
                right()
            if (key == '1'): #right
                print("breaked")
                quit()
            if (key == '2'): #right
                print("breaked")
                stop()

            if (key == 'r'): #right
                print("shake hand right")
                shake_hand_right()


            if (key == 'l'): #right
                print("shake hand left")
                shake_hand_left()

            if (key == 'w'): #right
                print("shake hand left")
                wave_hand_left()


            if (key == 'y'): #right
                print("yes head")
                head_yes()


            if (key == 'n'): #right
                print("head no")
                head_no()




                
            if (key == '3'): #right
                print("testing relay")
                for i in range(1,8):
                    print("testing relay", i)
                    #GPIO.output(int("relay_"+str(i)), GPIO.HIGH)
                    time.sleep(2)
                    #GPIO.output(int("relay_"+str(i)), GPIO.LOW)
 
    except KeyboardInterrupt:
        print("*************************ended***************************")
            





    



