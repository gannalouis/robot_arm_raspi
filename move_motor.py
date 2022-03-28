from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
kit.servo[0].actuation_range = 180
import time

#while(True):
kit.servo[2].angle = 180 
time.sleep(0.2)
kit.servo[3].angle = 40
time.sleep(0.2)
kit.servo[4].angle = 160 
time.sleep(0.2)
kit.servo[5].angle = 180
time.sleep(0.2)
kit.servo[6].angle = 0
time.sleep(3)
print("At postion 1")

kit.servo[2].angle = 90
time.sleep(0.2)
kit.servo[3].angle = 140
time.sleep(0.2)
kit.servo[4].angle = 90 
time.sleep(0.2)
kit.servo[5].angle = 90
time.sleep(0.2)
kit.servo[6].angle = 90
time.sleep(2)
print("At postion 2 | the neutral position")


kit.servo[2].angle = 90
time.sleep(0.2)
kit.servo[3].angle = 90
time.sleep(0.2)
kit.servo[4].angle = 180 
time.sleep(0.2)
kit.servo[5].angle = 90
time.sleep(0.2)
kit.servo[6].angle = 0
time.sleep(3)
print("At postion 3 | the neutral position")


kit.servo[4].angle = 0 
kit.servo[6].angle = 180
kit.servo[2].angle = 0
time.sleep(0.2)
kit.servo[3].angle = 0
time.sleep(0.2)
kit.servo[5].angle = 0
time.sleep(0.2)
time.sleep(2)
kit.servo[5].angle = 180
time.sleep(0.2)
kit.servo[6].angle = 180

kit.servo[5].angle = 0
time.sleep(0.2)
kit.servo[6].angle = 0


kit.servo[5].angle = 180
time.sleep(0.2)
kit.servo[6].angle = 180

print("At postion 3 | the neutral position")

    # kit.servo[5].angle = 180
    # kit.servo[6].angle = 180
    # kit.servo[7].angle = 180
    # kit.servo[8].angle = 180
    # kit.servo[9].angle = 180
    # kit.servo[10].angle = 180
    # kit.servo[11].angle = 180
    # kit.servo[12].angle = 180
    # kit.servo[13].angle = 180
    # kit.servo[14].angle = 180
    # kit.servo[5].angle = 180
    # kit.servo[6].angle = 180
    # kit.servo[7].angle = 180
    # kit.servo[8].angle = 180
    # kit.servo[9].angle = 180
    # kit.servo[10].angle = 180
    # kit.servo[11].angle = 180
    # kit.servo[12].angle = 180
    # kit.servo[13].angle = 180
    # kit.servo[14].angle = 180
print('at angle 90')
    #time.sleep(2)
    #print('at angle 0')
    #kit.servo[0].angle = 0
    # kit.servo[1].angle = 0
    # kit.servo[2].angle = 0
    # kit.servo[3].angle = 0
    # kit.servo[5].angle = 0
    # kit.servo[6].angle = 0
    # kit.servo[7].angle = 0
    # kit.servo[8].angle = 0
    # kit.servo[9].angle = 0
    # kit.servo[10].angle = 0
    # kit.servo[11].angle = 0
    # kit.servo[12].angle = 0
    # kit.servo[13].angle = 0
    # kit.servo[14].angle = 0
    #time.sleep(2)
    #kit.servo[0].angle = 180
    #print('at angle 180')
    #time.sleep(2)
    #print("at end of program")

    #kit.continuous_servo[1].throttle = 1
    #kit.servo[0].set_pulse_width_range(1000, 2000)


