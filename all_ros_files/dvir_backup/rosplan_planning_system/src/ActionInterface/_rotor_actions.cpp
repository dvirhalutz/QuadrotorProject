#include "rosplan_action_interface/rotor_actions.h"
#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <gazebo_msgs/SetModelState.h>
#include <gazebo_msgs/GetModelState.h>
#include <geometry_msgs/Pose.h>
#include <gazebo_msgs/ModelState.h>

/* The implementation of rotor_actions.h */
namespace KCL_rosplan {

	/* constructor */
	RPTutorialInterface::RPTutorialInterface(ros::NodeHandle &nh) {
		// perform setup

        // create a node handle to manage communication with ROS network
        this->nh = &nh;

        // get waypoints reference frame from param server
        //nh.param<std::string>("waypoint_frameid", waypoint_frameid_, "map");

        // setup a move base clear costmap client (to be able to send clear costmap requests later on)
        //clear_costmaps_client_ = nh.serviceClient<std_srvs::Empty>("/move_base/clear_costmaps");
	}

/*
	geometry_msgs::Twist init_twist(double x,double y,double z){
	    //rospy.wait_for_service('/gazebo/set_model_state')
	    //rospy.loginfo('Service is ready')
	    ros::ServiceClient res=nh.serviceClient<gazebo_msgs::GetModelState>("/gazebo/get_model_state");
	    //res = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
	    gazebo_msgs::GetModelState curr_pos;
	    curr_pos.request.model_name="quadrotor";

	    //rospy.loginfo('dest_x is %f and curr_x %f',x, curr_pos.pose.position.x)
	    //rospy.loginfo('dest_y is %f and curr_y %f',y, curr_pos.pose.position.y)
	    //rospy.loginfo('dest_z is %f and curr_z %f',z, curr_pos.pose.position.z)

	    geometry_msgs::Twist twist;
	    if (client.call(res)){
	   	    //twist.linear.x = speed (x,curr_pos.pose.position.x)
		    //twist.linear.y = speed (y,curr_pos.pose.position.y)
		    //twist.linear.z = speed (z,curr_pos.pose.position.z)
    		    twist.linear.x = 10;
		    twist.linear.y = 10;
		    twist.linear.z = 10;

		    twist.angular.x = 0.0
		    twist.angular.y = 0.0
		    twist.angular.z = 0.0
	     }
	

	    return twist
	}
*/
	/* action dispatch callback */
	bool RPTutorialInterface::concreteCallback(const rosplan_dispatch_msgs::ActionDispatch::ConstPtr& msg) {

		// The action implementation goes here.
		ros::Publisher pub = nh->advertise<geometry_msgs::Twist>("/cmd_vel",1);
 		geometry_msgs::Twist twist;
 		ros::Rate loop_rate(10);
		
		while (ros::ok())
		{
			//twist = init_twist(x,y,z)
			twist.linear.x = 10;
			twist.linear.y = 10;
			twist.linear.z = 10;

			twist.angular.x = 0.0;
			twist.angular.y = 0.0;
			twist.angular.z = 0.0;


			loop_rate.sleep();
			pub.publish(twist);
			//        if twist.linear.x == 0 and twist.linear.y == 0 and twist.linear.z == 0 :
			//            rospy.loginfo('quadrotor has reached the destination')
			//            break
			//        #break

   			 // land
			ros::spinOnce();
		}
		
		// complete the action
		ROS_INFO("Quadrotor (%s) movment completing.", msg->name.c_str());
		return true;
	}
} // close namespace

	/*-------------*/
	/* Main method */
	/*-------------*/

	int main(int argc, char **argv) {

		ros::init(argc, argv, "rosplan_tutorial_action", ros::init_options::AnonymousName);
		ros::NodeHandle nh("~");

		// create PDDL action subscriber
		KCL_rosplan::RPTutorialInterface rpti(nh);

		rpti.runActionInterface();

		return 0;
	}
