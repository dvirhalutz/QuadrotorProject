# main script

from controllerClass import controlQuadrotor  as CQ
from renderPlanClass import createRenderedPlanFile  as RPL

locations={
    'location00':(0,0,0),
    'location01':(0,1,0),
    'location02':(0,2,0),
    'location03':(0,3,0),
    'location10':(1,0,0),
    'location11':(1,1,0),
    'location12':(1,2,0),
    'location13':(1,3,0),
    'location20':(2,0,0),
    'location21':(2,1,0),
    'location22':(2,2,0),
    'location23':(2,3,0),
    'location30':(3,0,0),
    'location31':(3,1,0),
    'location32':(3,2,0),
    'location33':(3,3,0),
}
mode = 'teleport'

dictOfAtions = {
        'movebetweensquares':[('moveDroneToNewLocation',3)],
        'takepic':[('moveDroneLower',-1),('moveDroneHigher',-1)]
    }
pathToPlan = '/Users/Bar/Desktop/test_proj2/plan.pddl'
pathToSaveRenderedFile = '/Users/Bar/Desktop/test_proj2/planRendered.txt'


# create the file for plan exec
cl = RPL(pathToPlan, pathToSaveRenderedFile, dictOfAtions,locations)
cl.readLinesOfFile()

# read the rendered file and execute its commands
cq = CQ(locations, mode)
with open(pathToSaveRenderedFile, "r") as fp:
    for _, line in enumerate(fp):
        getattr(cq,line)

