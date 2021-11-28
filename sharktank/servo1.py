from time import sleep
import threading
from adafruit_servokit import ServoKit
import adafruit_motor.servo
# from hand_servo_check import runhand
#servo = adafruit_motor.servo.Servo(1)


# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
#pca.frequency = 60



def test3():

  
    
    kit.servo[7].angle = 110
    kit.servo[6].angle = 110
    sleep(1)
    kit.servo[7].angle = 85
    kit.servo[6].angle = 85
    sleep(1)
    kit.servo[7].angle = 100
    kit.servo[6].angle = 100
    sleep(1)
    
    
    '''for x in range(180,0,-1):
        
        kit.servo[0].angle = x
        sleep(0.01)
        print(x)
    sleep(2) 
    for x in range(0,180,1):
         
         
        kit.servo[0].angle = x
        sleep(0.01)
        print(x)'''
        
def test4():
    
    '''for x in range(0,180,1):
        
        kit.servo[12].angle = x
        sleep(0.00001)
        print(x)
    sleep(1)  
    for x in range(180, 0,-1):
        kit.servo[12].angle = x
        sleep(0.00001)
        print(x)'''
    
        
def run_motor():
    y = threading.Thread(target= test4, args=())
    z = threading.Thread(target= test3, args=())
    y.start()
    z.start()
        
        
if __name__ == "__main__":
    run_motor()
    
    
    '''while True:
        
        test3()
        sleep(5)
        test4()
        sleep(5)'''
    
    
  

