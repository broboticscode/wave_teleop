#!/usr/bin/env python
import rospy
#from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from std_msgs.msg import Bool

# Author: Andrew Dai
# This ROS Node converts Joystick inputs from the joy node
# into commands for turtlesim

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed

def callback(data):
    pid = Bool()
    pid.data = data.buttons[2]
    print("The PID disable is {}".format(pid.data))
    pub.publish(pid)

# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    pub = rospy.Publisher('teleop/cmd', Bool, queue_size=10)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('joy_manager')
    #while not rospy.is_shutdown():
    global r
    r = rospy.Rate(10) # 10hz


    rospy.spin()

if __name__ == '__main__':
    start()
