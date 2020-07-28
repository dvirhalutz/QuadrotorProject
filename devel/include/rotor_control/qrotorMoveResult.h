// Generated by gencpp from file rotor_control/qrotorMoveResult.msg
// DO NOT EDIT!


#ifndef ROTOR_CONTROL_MESSAGE_QROTORMOVERESULT_H
#define ROTOR_CONTROL_MESSAGE_QROTORMOVERESULT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rotor_control
{
template <class ContainerAllocator>
struct qrotorMoveResult_
{
  typedef qrotorMoveResult_<ContainerAllocator> Type;

  qrotorMoveResult_()
    : dest()  {
    }
  qrotorMoveResult_(const ContainerAllocator& _alloc)
    : dest(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _dest_type;
  _dest_type dest;





  typedef boost::shared_ptr< ::rotor_control::qrotorMoveResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rotor_control::qrotorMoveResult_<ContainerAllocator> const> ConstPtr;

}; // struct qrotorMoveResult_

typedef ::rotor_control::qrotorMoveResult_<std::allocator<void> > qrotorMoveResult;

typedef boost::shared_ptr< ::rotor_control::qrotorMoveResult > qrotorMoveResultPtr;
typedef boost::shared_ptr< ::rotor_control::qrotorMoveResult const> qrotorMoveResultConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rotor_control::qrotorMoveResult_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rotor_control::qrotorMoveResult_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace rotor_control

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'rotor_control': ['/home/dvir/catkin_new/devel/share/rotor_control/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::rotor_control::qrotorMoveResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rotor_control::qrotorMoveResult_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rotor_control::qrotorMoveResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rotor_control::qrotorMoveResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rotor_control::qrotorMoveResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rotor_control::qrotorMoveResult_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rotor_control::qrotorMoveResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5b71877c96ea31e76c519018632328bc";
  }

  static const char* value(const ::rotor_control::qrotorMoveResult_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5b71877c96ea31e7ULL;
  static const uint64_t static_value2 = 0x6c519018632328bcULL;
};

template<class ContainerAllocator>
struct DataType< ::rotor_control::qrotorMoveResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rotor_control/qrotorMoveResult";
  }

  static const char* value(const ::rotor_control::qrotorMoveResult_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rotor_control::qrotorMoveResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#result definition\n\
string dest\n\
";
  }

  static const char* value(const ::rotor_control::qrotorMoveResult_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rotor_control::qrotorMoveResult_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.dest);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct qrotorMoveResult_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rotor_control::qrotorMoveResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rotor_control::qrotorMoveResult_<ContainerAllocator>& v)
  {
    s << indent << "dest: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.dest);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROTOR_CONTROL_MESSAGE_QROTORMOVERESULT_H
