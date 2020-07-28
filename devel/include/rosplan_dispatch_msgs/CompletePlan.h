// Generated by gencpp from file rosplan_dispatch_msgs/CompletePlan.msg
// DO NOT EDIT!


#ifndef ROSPLAN_DISPATCH_MSGS_MESSAGE_COMPLETEPLAN_H
#define ROSPLAN_DISPATCH_MSGS_MESSAGE_COMPLETEPLAN_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <rosplan_dispatch_msgs/ActionDispatch.h>

namespace rosplan_dispatch_msgs
{
template <class ContainerAllocator>
struct CompletePlan_
{
  typedef CompletePlan_<ContainerAllocator> Type;

  CompletePlan_()
    : plan()  {
    }
  CompletePlan_(const ContainerAllocator& _alloc)
    : plan(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector< ::rosplan_dispatch_msgs::ActionDispatch_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::rosplan_dispatch_msgs::ActionDispatch_<ContainerAllocator> >::other >  _plan_type;
  _plan_type plan;





  typedef boost::shared_ptr< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> const> ConstPtr;

}; // struct CompletePlan_

typedef ::rosplan_dispatch_msgs::CompletePlan_<std::allocator<void> > CompletePlan;

typedef boost::shared_ptr< ::rosplan_dispatch_msgs::CompletePlan > CompletePlanPtr;
typedef boost::shared_ptr< ::rosplan_dispatch_msgs::CompletePlan const> CompletePlanConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace rosplan_dispatch_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'rosplan_dispatch_msgs': ['/home/dvir/catkin_new/src/ROSPlan/rosplan_dispatch_msgs/msg', '/home/dvir/catkin_new/devel/share/rosplan_dispatch_msgs/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'diagnostic_msgs': ['/opt/ros/kinetic/share/diagnostic_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7e1d10b4d2f9481e13d9d30c7a8045ff";
  }

  static const char* value(const ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7e1d10b4d2f9481eULL;
  static const uint64_t static_value2 = 0x13d9d30c7a8045ffULL;
};

template<class ContainerAllocator>
struct DataType< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rosplan_dispatch_msgs/CompletePlan";
  }

  static const char* value(const ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#completePlan message\n\
ActionDispatch[] plan\n\
\n\
================================================================================\n\
MSG: rosplan_dispatch_msgs/ActionDispatch\n\
#actionDispatch message\n\
int32 action_id\n\
string name\n\
diagnostic_msgs/KeyValue[] parameters\n\
float32 duration\n\
float32 dispatch_time\n\
\n\
================================================================================\n\
MSG: diagnostic_msgs/KeyValue\n\
string key # what to label this value when viewing\n\
string value # a value to track over time\n\
";
  }

  static const char* value(const ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.plan);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CompletePlan_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rosplan_dispatch_msgs::CompletePlan_<ContainerAllocator>& v)
  {
    s << indent << "plan[]" << std::endl;
    for (size_t i = 0; i < v.plan.size(); ++i)
    {
      s << indent << "  plan[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::rosplan_dispatch_msgs::ActionDispatch_<ContainerAllocator> >::stream(s, indent + "    ", v.plan[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROSPLAN_DISPATCH_MSGS_MESSAGE_COMPLETEPLAN_H
