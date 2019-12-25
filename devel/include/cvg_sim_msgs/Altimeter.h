// Generated by gencpp from file cvg_sim_msgs/Altimeter.msg
// DO NOT EDIT!


#ifndef CVG_SIM_MSGS_MESSAGE_ALTIMETER_H
#define CVG_SIM_MSGS_MESSAGE_ALTIMETER_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace cvg_sim_msgs
{
template <class ContainerAllocator>
struct Altimeter_
{
  typedef Altimeter_<ContainerAllocator> Type;

  Altimeter_()
    : header()
    , altitude(0.0)
    , pressure(0.0)
    , qnh(0.0)  {
    }
  Altimeter_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , altitude(0.0)
    , pressure(0.0)
    , qnh(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef float _altitude_type;
  _altitude_type altitude;

   typedef float _pressure_type;
  _pressure_type pressure;

   typedef float _qnh_type;
  _qnh_type qnh;





  typedef boost::shared_ptr< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> const> ConstPtr;

}; // struct Altimeter_

typedef ::cvg_sim_msgs::Altimeter_<std::allocator<void> > Altimeter;

typedef boost::shared_ptr< ::cvg_sim_msgs::Altimeter > AltimeterPtr;
typedef boost::shared_ptr< ::cvg_sim_msgs::Altimeter const> AltimeterConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cvg_sim_msgs::Altimeter_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace cvg_sim_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'cvg_sim_msgs': ['/home/dvir/catkin_ws/src/tum_simulator/cvg_sim_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c785451e2f67a76b902818138e9b53c6";
  }

  static const char* value(const ::cvg_sim_msgs::Altimeter_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc785451e2f67a76bULL;
  static const uint64_t static_value2 = 0x902818138e9b53c6ULL;
};

template<class ContainerAllocator>
struct DataType< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cvg_sim_msgs/Altimeter";
  }

  static const char* value(const ::cvg_sim_msgs::Altimeter_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
float32 altitude\n\
float32 pressure\n\
float32 qnh\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::cvg_sim_msgs::Altimeter_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.altitude);
      stream.next(m.pressure);
      stream.next(m.qnh);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Altimeter_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cvg_sim_msgs::Altimeter_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::cvg_sim_msgs::Altimeter_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "altitude: ";
    Printer<float>::stream(s, indent + "  ", v.altitude);
    s << indent << "pressure: ";
    Printer<float>::stream(s, indent + "  ", v.pressure);
    s << indent << "qnh: ";
    Printer<float>::stream(s, indent + "  ", v.qnh);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CVG_SIM_MSGS_MESSAGE_ALTIMETER_H
