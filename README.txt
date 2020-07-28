How to install:


MODEL WEIGHTS:
- Download weights from 
https://technionmail-my.sharepoint.com/:u:/g/personal/dvirh_campus_technion_ac_il/EQF8Vy6U3DtKrs31kuydLcQBTFFsNGRQevdqaUaKciIajg?e=uhSMYD

- cp <downloaded weights path> catkin_new/src/rotor_control/scripts/ML/saved_models/


ROSPLAN:
- cd catkin_new/src
- clone https://github.com/KCL-Planning/ROSPlan
- cd ..
- catkin_make


RUNNING SIMULATION: 
- In a new terminal type "source catkin_new/devel/setup.bash" and then "roscore"
- In a diffrent terminal run  ./runAll.sh src/rotor_control/common/plan.pddl src/rotor_control/scripts/mainScript.py

