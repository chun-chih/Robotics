// Generated by gencpp from file mav_system_msgs/ProcessInfo.msg
// DO NOT EDIT!


#ifndef MAV_SYSTEM_MSGS_MESSAGE_PROCESSINFO_H
#define MAV_SYSTEM_MSGS_MESSAGE_PROCESSINFO_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace mav_system_msgs
{
template <class ContainerAllocator>
struct ProcessInfo_
{
  typedef ProcessInfo_<ContainerAllocator> Type;

  ProcessInfo_()
    : pid(0)
    , name()
    , username()
    , cpu_percent(0.0)  {
    }
  ProcessInfo_(const ContainerAllocator& _alloc)
    : pid(0)
    , name(_alloc)
    , username(_alloc)
    , cpu_percent(0.0)  {
  (void)_alloc;
    }



   typedef uint32_t _pid_type;
  _pid_type pid;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _name_type;
  _name_type name;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _username_type;
  _username_type username;

   typedef float _cpu_percent_type;
  _cpu_percent_type cpu_percent;





  typedef boost::shared_ptr< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> const> ConstPtr;

}; // struct ProcessInfo_

typedef ::mav_system_msgs::ProcessInfo_<std::allocator<void> > ProcessInfo;

typedef boost::shared_ptr< ::mav_system_msgs::ProcessInfo > ProcessInfoPtr;
typedef boost::shared_ptr< ::mav_system_msgs::ProcessInfo const> ProcessInfoConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mav_system_msgs::ProcessInfo_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::mav_system_msgs::ProcessInfo_<ContainerAllocator1> & lhs, const ::mav_system_msgs::ProcessInfo_<ContainerAllocator2> & rhs)
{
  return lhs.pid == rhs.pid &&
    lhs.name == rhs.name &&
    lhs.username == rhs.username &&
    lhs.cpu_percent == rhs.cpu_percent;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::mav_system_msgs::ProcessInfo_<ContainerAllocator1> & lhs, const ::mav_system_msgs::ProcessInfo_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace mav_system_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e230da576ecad86012b88749ce2ed125";
  }

  static const char* value(const ::mav_system_msgs::ProcessInfo_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe230da576ecad860ULL;
  static const uint64_t static_value2 = 0x12b88749ce2ed125ULL;
};

template<class ContainerAllocator>
struct DataType< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mav_system_msgs/ProcessInfo";
  }

  static const char* value(const ::mav_system_msgs::ProcessInfo_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Miscellaneous information about process status.\n"
"# Written by Marco Tranzatto (see: https://github.com/ethz-asl/mav_eurathlon/blob/master/mav_eurathlon_msgs/msg/ProcessInfo.msg)\n"
"\n"
"uint32 pid              # Process PID\n"
"string name             # Process name\n"
"string username         # Name of the user that owns the process\n"
"float32 cpu_percent     # Process CPU utilization as a percentage\n"
;
  }

  static const char* value(const ::mav_system_msgs::ProcessInfo_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.pid);
      stream.next(m.name);
      stream.next(m.username);
      stream.next(m.cpu_percent);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ProcessInfo_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mav_system_msgs::ProcessInfo_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mav_system_msgs::ProcessInfo_<ContainerAllocator>& v)
  {
    s << indent << "pid: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.pid);
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.name);
    s << indent << "username: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.username);
    s << indent << "cpu_percent: ";
    Printer<float>::stream(s, indent + "  ", v.cpu_percent);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MAV_SYSTEM_MSGS_MESSAGE_PROCESSINFO_H