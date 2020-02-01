#! /usr/bin/env python


import rospy
import sys
from gazebo_msgs.srv import SetModelState, GetModelState
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from gazebo_msgs.msg import ModelState


class controlQuadrotor():
    def __init__(self,locationDict, mode='teleport',lowHight=2,highHight=7):
        self.mode = mode
        self.locationDict = locationDict
        self.lowHight = lowHight
        self.highHight = highHight
        self.x ,self.y, self.z= 0,0,0
        rospy.init_node('controller', anonymous=True)
        # TAKEOFF Command - Ask The Other Dvir How To Do It...
    
    def moveDroneToNewLocation(self,newLocation):
        x,y,z = self.locationDict[newLocation]
        if self.mode == "teleport":
            self.setPosition(x, y, z)
        else:
            self.flyToPos(x, y, z)
        self.x=x
        self.y=y
        self.z=z
    
    def moveDroneLower(self):
        if self.mode == "teleport":
            self.setPosition(self.x, self.y, self.lowHight)
        else:
            self.flyToPos(self.x, self.y, self.lowHight)
        self.z=self.lowHight
    
    def moveDroneHigher(self):
        if self.mode == "teleport":
            self.setPosition(self.x, self.y, self.highHight)
        else:
            self.flyToPos(self.x, self.y, self.highHight)
        self.z=self.highHight

    def speed(self, dst, curr):
        if abs(dst-curr) < 0.1:
            return 0
        elif dst > curr:
            return 0.2
        else:
            return -0.2


    def init_twist(self, x, y, z):
        rospy.wait_for_service('/gazebo/set_model_state')
        rospy.loginfo('Service is ready')
        res = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        curr_pos = res("quadrotor", "")
        rospy.loginfo('dest_x is %f and curr_x %f', x, curr_pos.pose.position.x)
        rospy.loginfo('dest_y is %f and curr_y %f', y, curr_pos.pose.position.y)
        rospy.loginfo('dest_z is %f and curr_z %f', z, curr_pos.pose.position.z)

        twist = Twist()
        twist.linear.x = self.speed(x, curr_pos.pose.position.x)
        twist.linear.y = self.speed(y, curr_pos.pose.position.y)
        twist.linear.z = self.speed(z, curr_pos.pose.position.z)

        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0

        return twist


    def init_pose(self, x, y, z):
        pose = Pose()
        pose.position.x = x
        pose.position.y = y
        pose.position.z = z
        pose.orientation.x = 0.0
        pose.orientation.y = 0.0
        pose.orientation.z = 0.0
        pose.orientation.w = 0.0
        return pose


    def init_model_state(self, x, y, z):
        model_name = "quadrotor"
        pose = self.init_pose(x, y, z)

        twist = Twist()
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0

        ref_frame = ""

        model_state = ModelState()
        model_state.model_name = model_name
        model_state.pose = pose
        model_state.twist = twist
        model_state.reference_frame = ref_frame

        return model_state


    def setPosition(self, x, y, z):
        rospy.loginfo('A request for position set has been received ')
        # # Create handle to the reset service
        rospy.loginfo('Waiting for set_model_state service')
        rospy.wait_for_service('/gazebo/set_model_state')
        rospy.loginfo('Service is ready')
        try:
            res = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
            model_state = self.init_model_state(x, y, z)
            res(model_state)
            rospy.loginfo('Quadrotor position changed successfully')

        except rospy.ServiceException:
            rospy.loginfo('position set failed')


    def flyToPos(self, x, y, z):
        rospy.loginfo('A request for position set has been received ')
        rospy.loginfo('quadrotor taking off ')
        # take_off
        # wait
        rospy.loginfo('quadrotor is headed for destination')
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

        while not rospy.is_shutdown():
            twist = self.init_twist(x, y, z)
            rospy.sleep(0.5)
            pub.publish(twist)

            if twist.linear.x == 0 and twist.linear.y == 0 and twist.linear.z == 0:
                rospy.loginfo('quadrotor has reached the destination')
                break
            # break

        # land

