#!/bin/bash

xterm -title "Init world" -hold -e  "source ~/catkin_ws/devel/setup.bash;roslaunch cvg_sim_gazebo ardrone_testworld.launch  " &
xterm -title "launch rosplan" -hold -e  "source ~/catkin_ws/devel/setup.bash;cd ~/catkin_ws/; roslaunch qrotor_launch.launch " &
xterm -title "dispatch" -hold -e  "source ~/catkin_ws/devel/setup.bash; ~/catkin_ws/qrotor_sovler.bash " &
