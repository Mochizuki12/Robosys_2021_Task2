#!/usr/bin/env python3
import rospy
import pigpio
from std_msgs.msg import Float32MultiArray

pi = pigpio.pi()

def cb(messege):

    degrees = messege.data
    
    Servo_pinX = 18
    Servo_pinY = 12

    pulseX = degrees[0] * 925 / 90 + 1425

    if pulseX > 2400:
        pulseX = 2400
    
    elif pulseX < 550:
        pulseX = 550


    pulseY = degrees[1] * 925 / 90 + 1425

    if pulseY > 2400:
        pulseY = 2400
    
    elif pulseY < 550:
        pulseY = 550


    pi.set_servo_pulsewidth(Servo_pinX, pulseX)
    pi.set_servo_pulsewidth(Servo_pinY, pulseY)

if __name__ == '__main__':
    rospy.init_node('servo')
    sub = rospy.Subscriber('accelgyro', Float32MultiArray, cb)
    rospy.spin()
