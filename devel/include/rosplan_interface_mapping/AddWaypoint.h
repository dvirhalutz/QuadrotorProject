// Generated by gencpp from file rosplan_interface_mapping/AddWaypoint.msg
// DO NOT EDIT!


#ifndef ROSPLAN_INTERFACE_MAPPING_MESSAGE_ADDWAYPOINT_H
#define ROSPLAN_INTERFACE_MAPPING_MESSAGE_ADDWAYPOINT_H

#include <ros/service_traits.h>


#include <rosplan_interface_mapping/AddWaypointRequest.h>
#include <rosplan_interface_mapping/AddWaypointResponse.h>


namespace rosplan_interface_mapping
{

struct AddWaypoint
{

typedef AddWaypointRequest Request;
typedef AddWaypointResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct AddWaypoint
} // namespace rosplan_interface_mapping


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::rosplan_interface_mapping::AddWaypoint > {
  static const char* value()
  {
    return "bd9af2cdf47b3141d3559a7b37e0fa5a";
  }

  static const char* value(const ::rosplan_interface_mapping::AddWaypoint&) { return value(); }
};

template<>
struct DataType< ::rosplan_interface_mapping::AddWaypoint > {
  static const char* value()
  {
    return "rosplan_interface_mapping/AddWaypoint";
  }

  static const char* value(const ::rosplan_interface_mapping::AddWaypoint&) { return value(); }
};


// service_traits::MD5Sum< ::rosplan_interface_mapping::AddWaypointRequest> should match 
// service_traits::MD5Sum< ::rosplan_interface_mapping::AddWaypoint > 
template<>
struct MD5Sum< ::rosplan_interface_mapping::AddWaypointRequest>
{
  static const char* value()
  {
    return MD5Sum< ::rosplan_interface_mapping::AddWaypoint >::value();
  }
  static const char* value(const ::rosplan_interface_mapping::AddWaypointRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::rosplan_interface_mapping::AddWaypointRequest> should match 
// service_traits::DataType< ::rosplan_interface_mapping::AddWaypoint > 
template<>
struct DataType< ::rosplan_interface_mapping::AddWaypointRequest>
{
  static const char* value()
  {
    return DataType< ::rosplan_interface_mapping::AddWaypoint >::value();
  }
  static const char* value(const ::rosplan_interface_mapping::AddWaypointRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::rosplan_interface_mapping::AddWaypointResponse> should match 
// service_traits::MD5Sum< ::rosplan_interface_mapping::AddWaypoint > 
template<>
struct MD5Sum< ::rosplan_interface_mapping::AddWaypointResponse>
{
  static const char* value()
  {
    return MD5Sum< ::rosplan_interface_mapping::AddWaypoint >::value();
  }
  static const char* value(const ::rosplan_interface_mapping::AddWaypointResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::rosplan_interface_mapping::AddWaypointResponse> should match 
// service_traits::DataType< ::rosplan_interface_mapping::AddWaypoint > 
template<>
struct DataType< ::rosplan_interface_mapping::AddWaypointResponse>
{
  static const char* value()
  {
    return DataType< ::rosplan_interface_mapping::AddWaypoint >::value();
  }
  static const char* value(const ::rosplan_interface_mapping::AddWaypointResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROSPLAN_INTERFACE_MAPPING_MESSAGE_ADDWAYPOINT_H
