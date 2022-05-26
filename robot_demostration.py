#! /usr/bin/env python3
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
kit.servo[0].actuation_range = 180
import time


# initalizing all the servo position encoder global variables
# this allow us to keep track of what is the encoder value at all times
servo_position_arr = [0 ,0 ,0 ,0 ,0 ,0]

# every time the robot starts all the servo move to the rest position
# by starting off with a known position we can use the encoders on the motors to use the motion smoothening algorithm 
def initalization():
    kit.servo[0].angle = 90
    time.sleep(0.5)
    kit.servo[1].angle = 90
    time.sleep(0.5)
    kit.servo[2].angle = 90 
    time.sleep(0.5)
    kit.servo[3].angle = 90
    time.sleep(0.5)
    kit.servo[4].angle = 90
    time.sleep(0.5)
    kit.servo[5].angle = 90
    time.sleep(0.5)
    for x in range(0,6):
       servo_position_arr[x] = 90
    print("All the servos have been initilized to 90 degrees: ", servo_position_arr)


# Video of jerky motion (cycling through the motions )
def jerky_motion():

    #pose 1
    for y in range(0,6):
        kit.servo[y].angle = 180
        time.sleep(0.5)

    time.sleep(1)
    
    #pose 2
    kit.servo[0].angle = 0
    time.sleep(0.5)
    kit.servo[1].angle = 40
    time.sleep(0.5)
    kit.servo[2].angle = 40 
    time.sleep(0.5)
    kit.servo[3].angle = 0
    time.sleep(0.5)
    kit.servo[4].angle = 180
    time.sleep(0.5)
    kit.servo[5].angle = 0
    time.sleep(1)
    
    #pose 3
    kit.servo[0].angle = 180
    time.sleep(0.5)
    kit.servo[1].angle = 40
    time.sleep(0.5)
    kit.servo[2].angle = 160
    time.sleep(0.5)
    kit.servo[3].angle = 180
    time.sleep(0.5)
    kit.servo[4].angle = 0
    time.sleep(0.5)
    kit.servo[5].angle = 180
    time.sleep(1)

def no_jerky_motion():
    extra_smooth(180,180,180,180,180,180)
    time.sleep(1)
    extra_smooth(0,40,40,0,180,0)
    time.sleep(1)
    extra_smooth(180,40,160,0,180,180)
    time.sleep(1)


# Collision demo
def collision():
    kit.servo[1].angle = 155 
    time.sleep(0.2)
    kit.servo[2].angle = 0
    time.sleep(0.2)
    kit.servo[0].angle = 0
    time.sleep(0.2)
    kit.servo[3].angle = 0
    time.sleep(0.2)
    kit.servo[4].angle = 180
    time.sleep(0.2)
    kit.servo[5].angle = 0
    time.sleep(1)
# no collision 
def no_collision():
    extra_smooth(0,155,0,0,180,0)
    time.sleep(1)
    


# Encoder values changing in real time demo (cycling throught the encoder values)
    #I think All I need to do is to uncomment "print(servo_position_arr)"

# motion smoothening function that increments or decrements the value from the current encoder value to new value, then updates the encoder value with final value
def extra_smooth(final_position0, final_position1, final_position2, final_position3, final_position4, final_position5): 
    Done = False
    colors = [False, False, False, False, False, False]
    final_position = [final_position0, final_position1, final_position2, final_position3, final_position4, final_position5] 
    inc = 1
    sleep = 0.0008
    while Done is False:
        for x in range(6):
            #print("this is the ", x ,"itteration")
            if servo_position_arr[x] < final_position[x]:
                servo_position_arr[x] += inc 
                kit.servo[x].angle = servo_position_arr[x] 
                time.sleep(sleep)
                print(servo_position_arr)
            elif servo_position_arr[x] > final_position[x]:  
                servo_position_arr[x] -= inc 
                kit.servo[x].angle = servo_position_arr[x] 
                time.sleep(sleep) 
                print(servo_position_arr)
            else:
                colors[x] = True

        
        if colors[0] and colors[1] and colors[2] and colors[3] and colors[4] and colors[5]:
            Done = True
            print(colors)
            print("Final position saved: ", servo_position_arr)

def main():
    initalization()
    #jerky_motion()
    #initalization()
    no_jerky_motion()
    
    #collision()
    #initalization()
    #no_collision()
    
if __name__=="__main__":
    main()

