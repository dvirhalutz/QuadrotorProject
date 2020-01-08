# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "rotor_control: 7 messages, 0 services")

set(MSG_I_FLAGS "-Irotor_control:/home/dvir/catkin_ws/devel/share/rotor_control/msg;-Iactionlib_msgs:/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(rotor_control_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg" NAME_WE)
add_custom_target(_rotor_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rotor_control" "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg" "rotor_control/qrotorMoveResult:actionlib_msgs/GoalID:std_msgs/Header:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg" NAME_WE)
add_custom_target(_rotor_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rotor_control" "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg" "rotor_control/qrotorMoveGoal:actionlib_msgs/GoalID:std_msgs/Header"
)

get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg" NAME_WE)
add_custom_target(_rotor_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rotor_control" "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg" "rotor_control/qrotorMoveFeedback:actionlib_msgs/GoalID:std_msgs/Header:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg" NAME_WE)
add_custom_target(_rotor_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rotor_control" "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg" ""
)

get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveAction.msg" NAME_WE)
add_custom_target(_rotor_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rotor_control" "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveAction.msg" "rotor_control/qrotorMoveGoal:actionlib_msgs/GoalStatus:rotor_control/qrotorMoveFeedback:rotor_control/qrotorMoveActionFeedback:rotor_control/qrotorMoveActionGoal:rotor_control/qrotorMoveActionResult:rotor_control/qrotorMoveResult:actionlib_msgs/GoalID:std_msgs/Header"
)

get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg" NAME_WE)
add_custom_target(_rotor_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rotor_control" "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg" ""
)

get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg" NAME_WE)
add_custom_target(_rotor_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rotor_control" "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rotor_control
)
_generate_msg_cpp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rotor_control
)
_generate_msg_cpp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rotor_control
)
_generate_msg_cpp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rotor_control
)
_generate_msg_cpp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveAction.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rotor_control
)
_generate_msg_cpp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rotor_control
)
_generate_msg_cpp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rotor_control
)

### Generating Services

### Generating Module File
_generate_module_cpp(rotor_control
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rotor_control
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(rotor_control_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(rotor_control_generate_messages rotor_control_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_cpp _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_cpp _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_cpp _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_cpp _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveAction.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_cpp _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_cpp _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_cpp _rotor_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rotor_control_gencpp)
add_dependencies(rotor_control_gencpp rotor_control_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rotor_control_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rotor_control
)
_generate_msg_eus(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rotor_control
)
_generate_msg_eus(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rotor_control
)
_generate_msg_eus(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rotor_control
)
_generate_msg_eus(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveAction.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rotor_control
)
_generate_msg_eus(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rotor_control
)
_generate_msg_eus(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rotor_control
)

### Generating Services

### Generating Module File
_generate_module_eus(rotor_control
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rotor_control
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(rotor_control_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(rotor_control_generate_messages rotor_control_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_eus _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_eus _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_eus _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_eus _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveAction.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_eus _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_eus _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_eus _rotor_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rotor_control_geneus)
add_dependencies(rotor_control_geneus rotor_control_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rotor_control_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rotor_control
)
_generate_msg_lisp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rotor_control
)
_generate_msg_lisp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rotor_control
)
_generate_msg_lisp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rotor_control
)
_generate_msg_lisp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveAction.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rotor_control
)
_generate_msg_lisp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rotor_control
)
_generate_msg_lisp(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rotor_control
)

### Generating Services

### Generating Module File
_generate_module_lisp(rotor_control
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rotor_control
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(rotor_control_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(rotor_control_generate_messages rotor_control_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_lisp _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_lisp _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_lisp _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_lisp _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveAction.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_lisp _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_lisp _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_lisp _rotor_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rotor_control_genlisp)
add_dependencies(rotor_control_genlisp rotor_control_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rotor_control_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rotor_control
)
_generate_msg_nodejs(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rotor_control
)
_generate_msg_nodejs(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rotor_control
)
_generate_msg_nodejs(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rotor_control
)
_generate_msg_nodejs(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveAction.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rotor_control
)
_generate_msg_nodejs(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rotor_control
)
_generate_msg_nodejs(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rotor_control
)

### Generating Services

### Generating Module File
_generate_module_nodejs(rotor_control
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rotor_control
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(rotor_control_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(rotor_control_generate_messages rotor_control_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_nodejs _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_nodejs _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_nodejs _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_nodejs _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveAction.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_nodejs _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_nodejs _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_nodejs _rotor_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rotor_control_gennodejs)
add_dependencies(rotor_control_gennodejs rotor_control_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rotor_control_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rotor_control
)
_generate_msg_py(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rotor_control
)
_generate_msg_py(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rotor_control
)
_generate_msg_py(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rotor_control
)
_generate_msg_py(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveAction.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg;/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rotor_control
)
_generate_msg_py(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rotor_control
)
_generate_msg_py(rotor_control
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rotor_control
)

### Generating Services

### Generating Module File
_generate_module_py(rotor_control
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rotor_control
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(rotor_control_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(rotor_control_generate_messages rotor_control_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionResult.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_py _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionGoal.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_py _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveActionFeedback.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_py _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveFeedback.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_py _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveAction.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_py _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveResult.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_py _rotor_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/dvir/catkin_ws/devel/share/rotor_control/msg/qrotorMoveGoal.msg" NAME_WE)
add_dependencies(rotor_control_generate_messages_py _rotor_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rotor_control_genpy)
add_dependencies(rotor_control_genpy rotor_control_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rotor_control_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rotor_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rotor_control
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(rotor_control_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(rotor_control_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rotor_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rotor_control
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(rotor_control_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(rotor_control_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rotor_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rotor_control
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(rotor_control_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(rotor_control_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rotor_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rotor_control
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(rotor_control_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(rotor_control_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rotor_control)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rotor_control\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rotor_control
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(rotor_control_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(rotor_control_generate_messages_py std_msgs_generate_messages_py)
endif()
