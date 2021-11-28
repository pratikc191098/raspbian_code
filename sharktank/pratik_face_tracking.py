import cv2
import numpy as np
#Motor Imports
from time import sleep
import threading
from adafruit_servokit import ServoKit
import adafruit_motor.servo

kit = ServoKit(channels=16)

x_center = 320
y_center = 230

nose_cascade = cv2.CascadeClassifier('./face.xml')

if nose_cascade.empty():
  raise IOError('Unable to load the face cascade classifier xml file')

cap = cv2.VideoCapture(0)
cap.set(3,640) #3 stands for width
cap.set(4,460) #4 stands for hight

ds_factor = 0.5
x_position = 90
y_position = 110
kit.servo[3].angle = x_position
kit.servo[4].angle = y_position

x_motor_last_position = 0
y_motor_last_position = 0

if x_motor_last_position > x_position:
    print("move x_motor to x_position by -1 steps ")
if x_motor_last_position < x_position:
    print("move x_motor to x_position by 1 steps ")
if y_motor_last_position > y_position:
    print("move y_motor to y_position by -1 steps ")
if y_motor_last_position > y_position:
    print("move x_motor to x_position by 1 steps ")


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    image_height, image_width, _ = frame.shape
    nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in nose_rects:
        nosex = x+w/2
        nosey = y+h/2
        center_coordinates = (int(nosex), int(nosey))
        radius = 10
        color = (255, 0, 0)
        thickness = 2
        frame = cv2.circle(frame, center_coordinates, radius, color, thickness)
 

        if nosex < x_center -90:
            x_position -= 2
            if x_position <= 1:
                x_position = 0  
                print("reached to last position")


        if nosex > x_center +90:
            x_position +=2
            if x_position >= 175:
                x_position = 175 
                print("reached to last position") 



        if nosey < y_center -60:
            y_position += 2
            if y_position >= 175:
                y_position = 175 
                print("reached to last position") 

        

        if nosey > y_center +60:
            y_position -=2
            if y_position <= 1:
                y_position = 1 
                print("reached to last position") 

        
    
    print(x_position,"is x_position and",y_position,"is y_position")
    kit.servo[3].angle = x_position
    kit.servo[4].angle = y_position
    
    x_motor_last_position = x_position
    y_motor_last_position = y_position

    cv2.imshow('Nose Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()