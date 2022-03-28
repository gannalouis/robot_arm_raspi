#! /usr/bin/env python
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
kit.servo[0].actuation_range = 180
import time

# initalizing all the servo position encoder global variables
# this allow us to keep track of what is the encoder value at all times
servo_position_arr = [0, 0, 0, 0, 0,]

# every time the robot starts all the servo move to the rest position
# by starting off with a known position we can use the encoders on the motors to use the motion smoothening algorythm 
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
    for x in range (0,5):
       servo_position_arr[x] = 90

# just a regular move function used to compare the motion of the robot arm 
def basic_move():
    angles = [0, 180, 0]
    for x in angles:
        kit.servo[0].angle = x
        time.sleep(1)



# motion smoothening function that increments or decrements the value from the current encoder value to new value, then updates the encoder value with final value
def extra_smooth(final_position0, final_position1, final_position2, final_position3, final_position4): 
    Done = False
    colors = [False, False, False, False, False]
    final_position = [final_position0, final_position1, final_position2, final_position3, final_position4] 
    inc = 1
    sleep = 0.0009
    #servo_number = [2, 3, 4, 5, 6]
    while Done is False:
        for x in range(0,5):
            #print("this is the ", x ,"itteration")
            if servo_position_arr[x] < final_position[x]:
                servo_position_arr[x] += inc 
                kit.servo[x].angle = servo_position_arr[x] 
                time.sleep(sleep)
                #print(servo_position_arr)
            elif servo_position_arr[x] > final_position[x]:  
                servo_position_arr[x] -= inc 
                kit.servo[x].angle = servo_position_arr[x] 
                time.sleep(sleep) 
            else:
                colors[x] = True

        
        if colors[0] and colors[1] and colors[2] and colors[3] and colors[4]:
            Done = True
            print(colors)
            print("Final position saved: ", servo_position_arr)




def smoothening(final_position, servo_motor_num): 
    servo_position = servo_position_arr[servo_motor_num]
    if servo_position < final_position:
        while(servo_position < final_position):
            kit.servo[servo_motor_num].angle = servo_position 
            servo_position += 1.5 
            time.sleep(0.01)
        servo_position_arr[servo_motor_num] = final_position
        print("Final position saved: in inc", servo_position_arr)
    else:
        while(servo_position > final_position):
            kit.servo[servo_motor_num].angle = servo_position 
            servo_position -= 1.5 
            time.sleep(0.01)
        servo_position_arr[servo_motor_num] = final_position
        print("Final position saved: in inc", servo_position_arr)

def main():
    initalization()
    print("this is the initalized array ", servo_position_arr)
    time.sleep(1)
    extra_smooth(180,180,180,180,180)   
    time.sleep(1)
    extra_smooth(0, 40, 40, 0, 180) 
    time.sleep(1)
    extra_smooth(180,60,160,180,0)

if __name__=="__main__":
    main()
