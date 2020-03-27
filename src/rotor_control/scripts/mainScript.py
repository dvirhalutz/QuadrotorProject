#!/usr/bin/env python
# main script

from controllerClass import controlQuadrotor  as CQ
from renderPlanClass import createRenderedPlanFile  as RPL

locations={
    'location00':(0,0,5),
    'location01':(0,1,5),
    'location02':(0,2,5),
    'location03':(0,3,5),
    'location10':(1,0,5),
    'location11':(1,1,5),
    'location12':(1,2,5),
    'location13':(1,3,5),
    'location20':(2,0,5),
    'location21':(2,1,5),
    'location22':(2,2,5),
    'location23':(2,3,5),
    'location30':(3,0,5),
    'location31':(3,1,5),
    'location32':(3,2,5),
    'location33':(3,3,5),
}
#mode = 'teleport'
mode = 'fly'

dictOfAtions = {
        'movebetweensquares':[('moveDroneToNewLocation',3)],
        'takepic':[('moveDroneLower',-1),('moveDroneHigher',-1)]
    }
pathToPlan = '/home/dvir/catkin_ws/src/rotor_control/common/plan.pddl'
pathToSaveRenderedFile = '/home/dvir/catkin_ws/src/rotor_control/common/planRendered.txt'


# create the file for plan exec
cl = RPL(pathToPlan, pathToSaveRenderedFile, dictOfAtions,locations)
cl.readLinesOfFile()

# read the rendered file and execute its commands

cq = CQ(mode,lowHight=2,highHight=5)
with open(pathToSaveRenderedFile, "r") as fp:
    for _, line in enumerate(fp):
	func_name = line.split('(')
	if func_name[0]=='moveDroneToNewLocation':
		params = func_name[1][:-2]
		print('moveDroneToNewLocation')
		print(params)
		params = params.split(',')
		params = [int(number) for number in params]
		cq.moveDroneToNewLocation((params[0],params[1],params[2]))
	elif func_name[0]=='moveDroneLower':
		print('moveDroneLower')
		cq.moveDroneLower()
	elif func_name[0]=='moveDroneHigher':
		print('moveDroneHigher')
		cq.moveDroneHigher()
	else:
		print('BUG!!!!!')
		



        #getattr(cq,line)

