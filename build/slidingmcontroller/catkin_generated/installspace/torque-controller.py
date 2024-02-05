#!/usr/bin/env python2
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64

publisherPhi = rospy.Publisher('robot/joint1_position_controller/command',Float64,queue_size=10)
publisherTheta = rospy.Publisher('robot/joint2_position_controller/command',Float64,queue_size=10)

def anglePublisher():
    msg = Float64()
    rate = rospy.Rate(25) 
    with open("../phi.txt","r") as txtfile:
        for line in txtfile.readlines():
            msg.data = float(line)
            publisherPhi.publish(msg)
            rate.sleep()

def anglePublisherPhiTheta():
    msgPhi = Float64()
    msgTheta = Float64()
    rate = rospy.Rate(25)
    with open("../phi.txt","r") as txtPhiFile, open("../Theta.txt","r") as txtThetaFile:
        for phi,theta in zip(txtPhiFile.readlines(),txtThetaFile.readlines()):
            msgPhi.data = float(phi)
            msgTheta.data = float(theta)
            publisherPhi.publish(msgPhi)
            publisherTheta.publish(msgTheta)
            rate.sleep()
        

def callback(data):
    phi = data.position[0]
    theta = data.position[1]
    print("phi:{}, theta:{}".format(phi, theta))


if __name__ == '__main__':
  
    rospy.init_node('sliding_mode_controller', anonymous=False)
    anglePublisherPhiTheta()
    #anglePublisher()
    #rospy.Subscriber('robot/joint_states', JointState,callback)
    #rospy.spin()