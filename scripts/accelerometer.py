#!/usr/bin/env python3
import rospy
import math
from mpu6050 import mpu6050
from std_msgs.msg import Float32MultiArray

rospy.init_node('accelerometer')
pub = rospy.Publisher('accelgyro', Float32MultiArray, queue_size=1)
rate = rospy.Rate(1000)
Xdeg = 0
Ydeg = 0
#Zdeg = 0   #When want to use the Z-axis Stabillizer
mpu = mpu6050(0x68)
degrees = [0,0,0]
dt = 0.001

def accel_threshold(x,y,z):

    if 0 < z and z < 0.001:
        accel_data['z'] = 0.001


    if 0 > z and z > -0.001:
        accel_data['z'] = -0.001


    if 0 < y and y < 0.001:
        accel_data['y'] = 0.001


    if 0 > y and y > -0.001:
        accel_data['y'] = -0.001


while not rospy.is_shutdown():

    gyro_data = mpu.get_gyro_data()

    accel_data = mpu.get_accel_data()

    accel_threshold(gyro_data['x'],gyro_data['y'],gyro_data['z'])


    Xdeg = 0.93 * (Xdeg + gyro_data['x'] * dt) + 0.07 * (math.atan2(accel_data['y'] , accel_data['z']) * 180 / math.pi)

    if Xdeg > 90:
        Xdeg = 90

    if Xdeg < -90:
        Xdeg = -90

    Ydeg = 0.91 * (Ydeg + gyro_data['y'] * dt) + 0.09 * (math.atan2(accel_data['x'] , math.sqrt(accel_data['z'] **2 + accel_data['y'] ** 2)) * 180 / math.pi)
    
    if Ydeg > 90:
        Ydeg = 90

    if Ydeg < -90:
        Ydeg = -90

    degrees[0] = Xdeg
    degrees[1] = Ydeg
    #degrees[2] = Zdeg 

    degrees_pub = Float32MultiArray(data = degrees)

    pub.publish(degrees_pub)
    rate.sleep()
