
System environment:

OS: ubuntu 16.4
Gazebo simulator: ver 7.16.0
ROS: Kinetic
Ros Packages:
RosPlan: ver. June 2018
Tum_Simulator
Rotor_Control (our package)
Python: ver. 2.7



How to install:

MODEL WEIGHTS:
- Download weights from 
https://technionmail-my.sharepoint.com/:u:/g/personal/dvirh_campus_technion_ac_il/EQF8Vy6U3DtKrs31kuydLcQBTFFsNGRQevdqaUaKciIajg?e=uhSMYD
- mkdir <workspace_folder>/src/rotor_contorl/scripts/ML/saved_models/
- cp <downloaded weights path> <workspace_folder>/src/rotor_control/scripts/ML/saved_models/

ADDDIONAL ENVIOURMENT SETTINGS:
- cd <workspace_folder>/src
- mkdir ROSPlan/rosplan_knowledge_base/common/mongoDB
- ```mkdir rotor_control/scripts/photos_taken_by_quadrotor/InTesting```
- mkdir rotor_control/scripts/photos_taken_by_quadrotor/InTesting/tmp

ROSPLAN:
- cd <workspace_folder>/src
- clone https://github.com/KCL-Planning/ROSPlan
- cd ..
- catkin_make


RUNNING SIMULATION: 
- In a new terminal type "roscore"
- In a diffrent terminal type "source <workspace_folder>/devel/setup.bash"
- Run ./runAll.sh src/rotor_control/common/plan.pddl src/rotor_control/scripts/mainScript.py

