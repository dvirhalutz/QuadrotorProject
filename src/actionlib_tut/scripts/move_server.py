#! /usr/bin/env python

import rospy

import actionlib

import actionlib_tut.msg

class moveAction(object):
    # create messages that are used to publish feedback/result
    _feedback = actionlib_tut.msg.moveFeedback()
    _result = actionlib_tut.msg.moveResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, actionlib_tut.msg.moveAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
      
    def execute_cb(self, goal):
        # helper variables
        r = rospy.Rate(1)
        success = True
        
        # append the seeds for the fibonacci sequence
        self._feedback.feedback_num=0

        # publish info to the console for the user
        rospy.loginfo('%s: Executing, start looping to %i with inital value of %i' % (self._action_name, goal.goal_num, self._feedback.feedback_num))
        
        # start executing the action
        for i in range(1, goal.goal_num):
            # check that preempt has not been requested by the client
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted' % self._action_name)
                self._as.set_preempted()
                success = False
                break
            self._feedback.feedback_num = self._feedback.feedback_num + 1
            # publish the feedback
            self._as.publish_feedback(self._feedback)
            rospy.loginfo('A feedback with value %i was published' % self._feedback.feedback_num )
            # this step is not necessary, the sequence is computed at 1 Hz for demonstration purposes
            rospy.sleep(5)
          
        if success:
            self._result.res_num = self._feedback.feedback_num
            rospy.loginfo('%s: Succeeded python' % self._action_name)
            self._as.set_succeeded(self._result)
        
if __name__ == '__main__':
    rospy.init_node('move')
    server = moveAction(rospy.get_name())
    rospy.spin()
