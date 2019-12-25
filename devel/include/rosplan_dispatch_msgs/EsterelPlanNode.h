// Generated by gencpp from file rosplan_dispatch_msgs/EsterelPlanNode.msg
// DO NOT EDIT!


#ifndef ROSPLAN_DISPATCH_MSGS_MESSAGE_ESTERELPLANNODE_H
#define ROSPLAN_DISPATCH_MSGS_MESSAGE_ESTERELPLANNODE_H


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
struct EsterelPlanNode_
{
  typedef EsterelPlanNode_<ContainerAllocator> Type;

  EsterelPlanNode_()
    : node_type(0)
    , node_id(0)
    , name()
    , action()
    , edges_out()
    , edges_in()  {
    }
  EsterelPlanNode_(const ContainerAllocator& _alloc)
    : node_type(0)
    , node_id(0)
    , name(_alloc)
    , action(_alloc)
    , edges_out(_alloc)
    , edges_in(_alloc)  {
  (void)_alloc;
    }



   typedef int8_t _node_type_type;
  _node_type_type node_type;

   typedef int32_t _node_id_type;
  _node_id_type node_id;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  _name_type name;

   typedef  ::rosplan_dispatch_msgs::ActionDispatch_<ContainerAllocator>  _action_type;
  _action_type action;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _edges_out_type;
  _edges_out_type edges_out;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _edges_in_type;
  _edges_in_type edges_in;



  enum {
    ACTION_START = 0,
    ACTION_END = 1,
    PLAN_START = 2,
  };


  typedef boost::shared_ptr< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> const> ConstPtr;

}; // struct EsterelPlanNode_

typedef ::rosplan_dispatch_msgs::EsterelPlanNode_<std::allocator<void> > EsterelPlanNode;

typedef boost::shared_ptr< ::rosplan_dispatch_msgs::EsterelPlanNode > EsterelPlanNodePtr;
typedef boost::shared_ptr< ::rosplan_dispatch_msgs::EsterelPlanNode const> EsterelPlanNodeConstPtr;

// constants requiring out of line definition

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace rosplan_dispatch_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'rosplan_dispatch_msgs': ['/home/dvir/catkin_ws/src/rosplan/rosplan_dispatch_msgs/msg', '/home/dvir/catkin_ws/devel/share/rosplan_dispatch_msgs/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'diagnostic_msgs': ['/opt/ros/kinetic/share/diagnostic_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> >
{
  static const char* value()
  {
    return "da4ec1de4a3a375abc1d2472c95de8b7";
  }

  static const char* value(const ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xda4ec1de4a3a375aULL;
  static const uint64_t static_value2 = 0xbc1d2472c95de8b7ULL;
};

template<class ContainerAllocator>
struct DataType< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rosplan_dispatch_msgs/EsterelPlanNode";
  }

  static const char* value(const ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#EsterelPlanNode message\n\
\n\
byte ACTION_START = 0\n\
byte ACTION_END   = 1\n\
byte PLAN_START   = 2\n\
\n\
byte node_type\n\
int32 node_id\n\
string name\n\
rosplan_dispatch_msgs/ActionDispatch action\n\
\n\
int32[] edges_out\n\
int32[] edges_in\n\
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

  static const char* value(const ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.node_type);
      stream.next(m.node_id);
      stream.next(m.name);
      stream.next(m.action);
      stream.next(m.edges_out);
      stream.next(m.edges_in);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct EsterelPlanNode_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rosplan_dispatch_msgs::EsterelPlanNode_<ContainerAllocator>& v)
  {
    s << indent << "node_type: ";
    Printer<int8_t>::stream(s, indent + "  ", v.node_type);
    s << indent << "node_id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.node_id);
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "action: ";
    s << std::endl;
    Printer< ::rosplan_dispatch_msgs::ActionDispatch_<ContainerAllocator> >::stream(s, indent + "  ", v.action);
    s << indent << "edges_out[]" << std::endl;
    for (size_t i = 0; i < v.edges_out.size(); ++i)
    {
      s << indent << "  edges_out[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.edges_out[i]);
    }
    s << indent << "edges_in[]" << std::endl;
    for (size_t i = 0; i < v.edges_in.size(); ++i)
    {
      s << indent << "  edges_in[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.edges_in[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROSPLAN_DISPATCH_MSGS_MESSAGE_ESTERELPLANNODE_H
