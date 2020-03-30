#!/usr/bin/env python


from __future__ import absolute_import
import rospy
import sys
from gazebo_msgs.srv import SetModelState, GetModelState
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from gazebo_msgs.msg import ModelState
from ML.test import model_test
from os import walk
import os


class controlQuadrotor(object):
    def __init__(self, mode=u'teleport', lowHight=2, highHight=7):
        self.mode = mode
        self.lowHight = lowHight
        self.highHight = highHight
        self.x, self.y, self.z = 0, 0, 0
        rospy.init_node(u'controller', anonymous=True)
        # TAKEOFF Command - Ask The Other Dvir How To Do It...

    def moveDroneToNewLocation(self, newLocation):
        x, y, z = newLocation
        if self.mode == u"teleport":
            self.setPosition(x, y, z)
        else:
            self.flyToPos(x, y, z)
        self.x = x
        self.y = y
        self.z = z

    def moveDroneLower(self):
        # move random image from PreTesting to InTesting
        path_to_PreTesting = u"./photos_taken_by_quadrotor/PreTesting"
        path_to_InTesting = u"./photos_taken_by_quadrotor/InTesting"
        image_path = u""
        image_new_path = u""
        for (root, _, filename) in walk(path_to_PreTesting):
            if filename.endswith(u'.png'):
                image_path = os.path.join(root, filename)
                image_new_path = os.path.join(path_to_InTesting, filename)
                os.rename(image_path, image_new_path)
                rospy.loginfo(u'Moved Image -> '+filename)
                break
        if image_path == u"":
            rospy.loginfo(u"Couldn't get the image from the folder")

        if self.mode == u"teleport":
            self.setPosition(self.x, self.y, self.lowHight)
        else:
            self.flyToPos(self.x, self.y, self.lowHight)
        self.z = self.lowHight

    def evaluateImage(self):
        # evaluate image in InTesting folder
        image_class = model_test()
        if image_class == u"EMPLTY":
            rospy.loginfo(u"Couldn't evaluate the image - Problem")
        else:
            rospy.loginfo(u"The image has classified as: "+image_class)

    def moveDroneHigher(self):
         # move image from InTesting to Done
        path_to_InTesting = u"./photos_taken_by_quadrotor/InTesting"
        path_to_Done = u"./photos_taken_by_quadrotor/Done"
        image_path, image_new_path = u"", u""
        for (root, _, filename) in walk(path_to_InTesting):
            if filename.endswith(u'.png'):
                image_path = os.path.join(root, filename)
                image_new_path = os.path.join(path_to_Done, filename)
                os.rename(image_path, image_new_path)
                rospy.loginfo(u"Moved Image -> "+filename)
        if image_path == u"":
            rospy.loginfo(u"Don't have any image inside the InTesting")

        if self.mode == u"teleport":
            self.setPosition(self.x, self.y, self.highHight)
        else:
            self.flyToPos(self.x, self.y, self.highHight)
        self.z = self.highHight

    def speed(self, dst, curr):
        if abs(dst-curr) < 0.1:
            return 0
        elif dst > curr:
            return 0.2
        else:
            return -0.2

    def init_twist(self, x, y, z):
        rospy.wait_for_service(u'/gazebo/set_model_state')
        rospy.loginfo(u'Service is ready')
        res = rospy.ServiceProxy(u'/gazebo/get_model_state', GetModelState)
        curr_pos = res(u"quadrotor", u"")
        rospy.loginfo(u'dest_x is %f and curr_x %f',
                      x, curr_pos.pose.position.x)
        rospy.loginfo(u'dest_y is %f and curr_y %f',
                      y, curr_pos.pose.position.y)
        rospy.loginfo(u'dest_z is %f and curr_z %f',
                      z, curr_pos.pose.position.z)

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
        model_name = u"quadrotor"
        pose = self.init_pose(x, y, z)

        twist = Twist()
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0

        ref_frame = u""

        model_state = ModelState()
        model_state.model_name = model_name
        model_state.pose = pose
        model_state.twist = twist
        model_state.reference_frame = ref_frame

        return model_state

    def setPosition(self, x, y, z):
        rospy.loginfo(u'A request for position set has been received ')
        # # Create handle to the reset service
        rospy.loginfo(u'Waiting for set_model_state service')
        rospy.wait_for_service(u'/gazebo/set_model_state')
        rospy.loginfo(u'Service is ready')
        try:
            res = rospy.ServiceProxy(u'/gazebo/set_model_state', SetModelState)
            model_state = self.init_model_state(x, y, z)
            res(model_state)
            rospy.loginfo(u'Quadrotor position changed successfully')

        except rospy.ServiceException:
            rospy.loginfo(u'position set failed')

    def flyToPos(self, x, y, z):
        rospy.loginfo(u'A request for position set has been received ')
        rospy.loginfo(u'quadrotor taking off ')
        # take_off
        # wait
        rospy.loginfo(u'quadrotor is headed for destination')
        pub = rospy.Publisher(u'cmd_vel', Twist, queue_size=10)
        while not rospy.is_shutdown():
            twist = self.init_twist(x, y, z)
            rospy.sleep(0.5)
            pub.publish(twist)

            if twist.linear.x == 0 and twist.linear.y == 0 and twist.linear.z == 0:
                rospy.loginfo(u'quadrotor has reached the destination')
                break
            # break
        # land
