#!/usr/bin/env python
# main script

from __future__ import with_statement
from __future__ import absolute_import
from controllerClass import controlQuadrotor as CQ
from renderPlanClass import createRenderedPlanFile as RPL
from io import open

locations = {
    u'location00': (15, -15, 5),
    u'location01': (15, -5, 5),
    u'location02': (15, 5, 5),
    u'location03': (15, 15, 5),
    u'location10': (5, -15, 5),
    u'location11': (5, -5, 5),
    u'location12': (5, 5, 5),
    u'location13': (5, 15, 5),
    u'location20': (-5, -15, 5),
    u'location21': (-5, -5, 5),
    u'location22': (-5, 5, 5),
    u'location23': (-5, 15, 5),
    u'location30': (-15, -15, 5),
    u'location31': (-15, -5, 5),
    u'location32': (-15, 5, 5),
    u'location33': (-15, 15, 5),
}
#mode = 'teleport'
mode = u'fly'

dictOfAtions = {
    u'movebetweensquares': [(u'moveDroneToNewLocation', 3)],
    u'takepic': [(u'moveDroneLower', -1), (u'evaluateImage', -1), (u'moveDroneHigher', -1)]
}
pathToPlan = u'/home/dvir/catkin_ws/src/rotor_control/common/plan.pddl'
pathToSaveRenderedFile = u'/home/dvir/catkin_ws/src/rotor_control/common/planRendered.txt'


# create the file for plan exec
cl = RPL(pathToPlan, pathToSaveRenderedFile, dictOfAtions, locations)
cl.readLinesOfFile()

# read the rendered file and execute its commands

cq = CQ(mode, lowHight=2, highHight=5)
with open(pathToSaveRenderedFile, u"r") as fp:
    for _, line in enumerate(fp):
        func_name = line.split(u'(')
        if func_name[0] == u'moveDroneToNewLocation':
            params = func_name[1][:-2]
            print u'moveDroneToNewLocation'
            print params
            params = params.split(u',')
            params = [int(number) for number in params]
            cq.moveDroneToNewLocation((params[0], params[1], params[2]))
        elif func_name[0] == u'moveDroneLower':
            print u'moveDroneLower'
            cq.moveDroneLower()
        elif func_name[0] == u'moveDroneHigher':
            print u'moveDroneHigher'
            cq.moveDroneHigher()
        elif func_name[0] == u'evaluateImage':
            print u'evaluateImage'
            cq.evaluateImage()
        else:
            print u'BUG!!!!!'
