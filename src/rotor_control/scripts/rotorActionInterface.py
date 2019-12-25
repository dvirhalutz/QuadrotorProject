#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import sys
from gazebo_msgs.srv import SetModelState, GetModelState
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from gazebo_msgs.msg import ModelState

def callback(data):
    # a message was heard
    doAction()

def doAction(data):
    #do something
    rospy.loginfo("recieved action$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4"); 
    pub.publish("done")
    rospy.loginfo("done and published"); 

if __name__ == '__main__':

	       
	rospy.init_node('rotorActionInterface', anonymous=True)
	pub = rospy.Publisher('rosplan_interface_undock/jobDone', String, queue_size=10)
	rospy.Subscriber("rosplan_interface_undock/jobReq", String, doAction)
	rospy.loginfo("initiating rotorActionInterface"); 
	rospy.spin()
	rospy.loginfo("NOT SUPPOSE TO BE HERERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRr"); 

