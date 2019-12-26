#include "rosplan_action_interface/rotor_actions.h"
#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <gazebo_msgs/SetModelState.h>
#include <gazebo_msgs/GetModelState.h>
#include <geometry_msgs/Pose.h>
#include <gazebo_msgs/ModelState.h>
#include "std_msgs/String.h"

bool g_msgRecievedFlag = false;
int counter = 0;
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
	void temp(std_msgs::String str){
	g_msgRecievedFlag = true;
	ROS_INFO("massage recieved___________________________________________________________________________________________________________%s, %d",str.data.c_str(),counter++);	
	//ros::shutdown();
	};
	
	/* action dispatch callback */
	bool RPTutorialInterface::concreteCallback(const rosplan_dispatch_msgs::ActionDispatch::ConstPtr& msg) {
		
		ROS_INFO("rotor concrete callback with action %s +++++++++++++++++++++++++++++++++++++++++++++++++++",msg->name.c_str());
		//ros::Publisher pub = this->nh.advertise<rosplan_dispatch_msgs::ActionDispatch::ConstPtr>("jobReq", 1000);
		ros::Publisher pub = (this->nh)->advertise<std_msgs::String>("jobReq", 1000);
		//pub.publish(msg);
		//ros::spinOnce();
 		std_msgs::String rotor_action;
     		std::stringstream ss;
      		ss << "hello world ";
  		rotor_action.data = ss.str();
		pub.publish(rotor_action);
		ROS_INFO("rotor publish was successful");
		//ros::Duration(5).sleep();
		boost::shared_ptr<std_msgs::String const> recived_msg;
		ros::Rate loop_rate(5);
		ros::Subscriber sub =(this->nh)->subscribe("jobDone", 1000, temp);
		while (!g_msgRecievedFlag && ros::ok()){
		  ros::spinOnce();
		  loop_rate.sleep();
		}

		g_msgRecievedFlag=false;
		
		//recived_msg = ros::topic::waitForMessage<std_msgs::String>("jobDone",*(this->nh));
		//ros::spinOnce();
		
		ROS_INFO("exit conceretecallback");
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
