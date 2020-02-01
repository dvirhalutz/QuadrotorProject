# Install script for directory: /home/dvir/catkin_ws/src/rosplan_demos/rosplan_demos_interfaces/rosplan_interface_mapping

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/dvir/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rosplan_interface_mapping/srv" TYPE FILE FILES
    "/home/dvir/catkin_ws/src/rosplan_demos/rosplan_demos_interfaces/rosplan_interface_mapping/srv/CreatePRM.srv"
    "/home/dvir/catkin_ws/src/rosplan_demos/rosplan_demos_interfaces/rosplan_interface_mapping/srv/AddWaypoint.srv"
    "/home/dvir/catkin_ws/src/rosplan_demos/rosplan_demos_interfaces/rosplan_interface_mapping/srv/RemoveWaypoint.srv"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rosplan_interface_mapping/cmake" TYPE FILE FILES "/home/dvir/catkin_ws/build/rosplan_demos/rosplan_demos_interfaces/rosplan_interface_mapping/catkin_generated/installspace/rosplan_interface_mapping-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/dvir/catkin_ws/devel/include/rosplan_interface_mapping")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/dvir/catkin_ws/devel/share/roseus/ros/rosplan_interface_mapping")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/dvir/catkin_ws/devel/share/common-lisp/ros/rosplan_interface_mapping")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/dvir/catkin_ws/devel/share/gennodejs/ros/rosplan_interface_mapping")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/dvir/catkin_ws/devel/lib/python2.7/dist-packages/rosplan_interface_mapping")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/dvir/catkin_ws/devel/lib/python2.7/dist-packages/rosplan_interface_mapping")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/dvir/catkin_ws/build/rosplan_demos/rosplan_demos_interfaces/rosplan_interface_mapping/catkin_generated/installspace/rosplan_interface_mapping.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rosplan_interface_mapping/cmake" TYPE FILE FILES "/home/dvir/catkin_ws/build/rosplan_demos/rosplan_demos_interfaces/rosplan_interface_mapping/catkin_generated/installspace/rosplan_interface_mapping-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rosplan_interface_mapping/cmake" TYPE FILE FILES
    "/home/dvir/catkin_ws/build/rosplan_demos/rosplan_demos_interfaces/rosplan_interface_mapping/catkin_generated/installspace/rosplan_interface_mappingConfig.cmake"
    "/home/dvir/catkin_ws/build/rosplan_demos/rosplan_demos_interfaces/rosplan_interface_mapping/catkin_generated/installspace/rosplan_interface_mappingConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/rosplan_interface_mapping" TYPE FILE FILES "/home/dvir/catkin_ws/src/rosplan_demos/rosplan_demos_interfaces/rosplan_interface_mapping/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/rosplan_interface_mapping/rp_roadmap_server" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/rosplan_interface_mapping/rp_roadmap_server")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/rosplan_interface_mapping/rp_roadmap_server"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/rosplan_interface_mapping" TYPE EXECUTABLE FILES "/home/dvir/catkin_ws/devel/lib/rosplan_interface_mapping/rp_roadmap_server")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/rosplan_interface_mapping/rp_roadmap_server" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/rosplan_interface_mapping/rp_roadmap_server")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/rosplan_interface_mapping/rp_roadmap_server"
         OLD_RPATH "/home/dvir/catkin_ws/devel/lib:/opt/ros/kinetic/lib:/opt/ros/kinetic/lib/x86_64-linux-gnu:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/rosplan_interface_mapping/rp_roadmap_server")
    endif()
  endif()
endif()

