import RPi.GPIO as GPIO                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
from time import sleep
import time
#import keyboard
import readchar

vr_motorpin_left = 32
vr_motorpin_right = 33 ################################

hallpin = 36

#Motor1 pins
relay_1 = 29
enable_high_low = 31
#right_enable_high_low = 11 

right_zf_direction_high_low = 13
relay_4 = 37
left_zf_direction_high_low = 40#############################################

GPIO.setwarnings(False)         #disable warnings
GPIO.setmode(GPIO.BOARD)        #set pin numbering system
GPIO.setup(vr_motorpin_left,GPIO.OUT)
GPIO.setup(vr_motorpin_right,GPIO.OUT)
GPIO.setup(hallpin,GPIO.IN)
GPIO.setup(relay_1,GPIO.OUT)
GPIO.setup(enable_high_low,GPIO.OUT)
#GPIO.setup(right_enable_high_low,GPIO.OUT)
GPIO.setup(right_zf_direction_high_low,GPIO.OUT)
GPIO.setup(left_zf_direction_high_low,GPIO.OUT)
GPIO.setup(relay_4,GPIO.OUT)


pwm_left = GPIO.PWM(vr_motorpin_left,800)#450
pwm_right = GPIO.PWM(vr_motorpin_right,800)

pwm_left.start(0)#start PWM of required Duty Cycle 
pwm_right.start(0)#start PWM of required Duty Cycle 


speed_value= 80
stop_speed=0



def forward():
    print("reverse")

    if(GPIO.input(hallpin) == True):
        #gpio.output(ledpin, True)
        print("magnet detected")
    else:
        #gpio.output(ledpin, False)
        print("magnetic field not detected")
    
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)

    #GPIO.output(relay_1, GPIO.LOW) 
    GPIO.output(enable_high_low, GPIO.LOW)
    #GPIO.output(right_enable_high_low, GPIO.LOW)

    
    time.sleep(0.5)
    GPIO.output(right_zf_direction_high_low,GPIO.LOW) 
    GPIO.output(left_zf_direction_high_low,GPIO.HIGH) 
    
    GPIO.output(enable_high_low, GPIO.HIGH)
    #GPIO.output(right_enable_high_low, GPIO.HIGH)
      
    
    time.sleep(1)
    
    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)




def reverse():
    print("forward")

    

    if(GPIO.input(hallpin) == True):
        #gpio.output(ledpin, True)
        print("magnet detected")
    else:
        #gpio.output(ledpin, False)
        print("magnetic field not detected")
    
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)

    GPIO.output(relay_1, GPIO.LOW) 
    GPIO.output(enable_high_low, GPIO.LOW)
    #GPIO.output(right_enable_high_low, GPIO.LOW)

    time.sleep(0.5)
    GPIO.output(left_zf_direction_high_low,GPIO.LOW) 
    GPIO.output(right_zf_direction_high_low,GPIO.HIGH) 
    
    GPIO.output(enable_high_low, GPIO.HIGH)
    #GPIO.output(right_enable_high_low, GPIO.HIGH)
      
    
    time.sleep(1)
    
    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)


def right():
    print("right")

    

    if(GPIO.input(hallpin) == True):
        #gpio.output(ledpin, True)
        print("magnet detected")
    else:
        #gpio.output(ledpin, False)
        print("magnetic field not detected")
    
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)

    GPIO.output(relay_1, GPIO.LOW) 
    GPIO.output(enable_high_low, GPIO.LOW)
    #GPIO.output(right_enable_high_low, GPIO.LOW)

    time.sleep(0.5)
    GPIO.output(left_zf_direction_high_low,GPIO.HIGH) 
    GPIO.output(right_zf_direction_high_low,GPIO.HIGH) 
    
    GPIO.output(enable_high_low, GPIO.HIGH)
    #GPIO.output(right_enable_high_low, GPIO.HIGH)
      
    
    time.sleep(1)
    
    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)



def left():
    print("left")

    

    if(GPIO.input(hallpin) == True):
        #gpio.output(ledpin, True)
        print("magnet detected")
    else:
        #gpio.output(ledpin, False)
        print("magnetic field not detected")
    
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)

    GPIO.output(relay_1, GPIO.LOW) 
    GPIO.output(enable_high_low, GPIO.LOW)
    #GPIO.output(right_enable_high_low, GPIO.LOW)

    time.sleep(0.5)
    GPIO.output(left_zf_direction_high_low,GPIO.LOW) 
    GPIO.output(right_zf_direction_high_low,GPIO.LOW) 
    
    GPIO.output(enable_high_low, GPIO.HIGH)
    #GPIO.output(right_enable_high_low, GPIO.HIGH)
   
    
    time.sleep(1)
    
    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)



def stop():
    print("stop")

    #GPIO.output(right_enable_high_low, GPIO.LOW)
    GPIO.output(enable_high_low, GPIO.LOW)
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
    
    




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
                
            if (key == '3'): #right
                print("testing relay")
                for i in range(1,8):
                    print("testing relay", i)
                    #GPIO.output(int("relay_"+str(i)), GPIO.HIGH)
                    time.sleep(2)
                    #GPIO.output(int("relay_"+str(i)), GPIO.LOW)
 
    except KeyboardInterrupt:
        print("*************************ended***************************")
            
