#include <ros/ros.h>
#include <vector>

#include "rosplan_action_interface/RPActionInterface.h"
#include "std_msgs/String.h"
#ifndef KCL_tutorial_10
#define KCL_tutorial_10

/**
 * This file defines an action interface created in tutorial 10.
 */
namespace KCL_rosplan {

	class RPTutorialInterface: public RPActionInterface
	{

	
	
	public:
	//ros::Subscriber sub;
	//void temp(std_msgs::String str);
	//geometry_msgs::Twist init_twist(double x,double y,double z);
	ros::NodeHandle* nh;
		/* constructor */
		RPTutorialInterface(ros::NodeHandle &nh);

		/* listen to and process action_dispatch topic */
		bool concreteCallback(const rosplan_dispatch_msgs::ActionDispatch::ConstPtr& msg);
	};
}
#endif

