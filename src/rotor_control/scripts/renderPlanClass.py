#!/usr/bin/env python
from __future__ import with_statement
from __future__ import absolute_import
import re
import os
from io import open


class createRenderedPlanFile(object):
    u'''
    pathToPlan => Full not relative path to the file we would like to render
    pathToSaveRenderedFile => Full not relative path to the location we want to save tehe rendered file
    dictOfAtions => dictionary of plan actions to tuple containing functions to execute and number of
                    prameters of the plan action, for example:
                    'movebetweensquares' => 'teleport'
                    'movebetweensquares drone location00 location11'
                            ^0            ^1      ^2         ^3

                    'takepic' => (('lowerDrone',-1),3)
                    'takepic drone location12 person1'

    '''

    def __init__(self, pathToPlan, pathToSaveRenderedFile, dictOfAtions, locationDict,toFile = False,mode=u'teleport'):
        self.toFile = toFile
        self.mode  = mode
        self.locationDict=locationDict
        self.pathToPlan = pathToPlan
        self.pathToSaveRenderedFile = pathToSaveRenderedFile
        self.dictOfAtions = dictOfAtions
        self.listOfPlanAction = [key for key in dictOfAtions]
        # (movebetweensquares [0-9a-zA-Z ?]*)
        self.regexPatterns = [re.compile(
            u"("+actionInPlan+u" [0-9a-zA-Z ]*)") for actionInPlan in self.listOfPlanAction]
        if os.path.exists(self.pathToSaveRenderedFile):
            os.remove(self.pathToSaveRenderedFile)

    def writeToFile(self, commandToWrite):
        if os.path.exists(self.pathToSaveRenderedFile):
            append_write = u'a'  # append if already exists
        else:
            append_write = u'w'  # make a new file if not
        with open(self.pathToSaveRenderedFile, append_write) as fp:
            fp.write(commandToWrite)

    def convertPlanLineToActionAndSaveIt(self, lineToConvert):
        stringToWrite = u""
        for pattern in self.regexPatterns:
            match = pattern.search(lineToConvert)
            if(match):
                stringToWrite = match.group()
                break
        if stringToWrite != u"":
            stringToArr = stringToWrite.split()
            actionsLstToExec = self.dictOfAtions[stringToArr[0]]
            argString=u''
            for func,arg in actionsLstToExec:
                if arg>-1:
                    arglocation = self.locationDict[stringToArr[arg]]
                    argString = unicode(arglocation[0])+u","+unicode(arglocation[1])+u","+unicode(arglocation[2])
                stringToWrite = func + u"(" + argString+u")\n"
                self.writeToFile(stringToWrite)
            

    def readLinesOfFile(self):
        with open(self.pathToPlan, "r") as fp:
            for _, line in enumerate(fp):
                self.convertPlanLineToActionAndSaveIt(line)





