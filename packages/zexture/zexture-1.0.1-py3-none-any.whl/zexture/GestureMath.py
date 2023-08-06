from math import *

def getFpsColor(fps):
    if fps<=10:
        return (0,0,150)
    if fps>=30:
        return (0,150,0)
    g = min(150,(fps-10)*15)
    r = min(150,150-((fps-20)*15))
    return (0,g,r)
    

def getCenterOfMass(lmList):
    sumX = 0
    for i in range(21):
        sumX = sumX + lmList[i][1]
    sumY = 0
    for i in range(21):
        sumY = sumY + lmList[i][2]

    return sumX/21, sumY/21

def getAngle(pt1, pt2):
    comX, comY = pt1[0], pt1[1]
    x, y = pt2[0], pt2[1]
    if x == comX:
        return 1.570796
    angle = atan((y-comY)/(x-comX))
    return angle

def getDistance(pt1, pt2):
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def getVector(pt1, pt2):
    return getDistance(pt1, pt2), getAngle(pt1, pt2)

def getVectorFromCenter(lmList):
    comX, comY = getCenterOfMass(lmList)
    distFromCOM = [0 for i in range(21)]
    angleFromCOM = [0 for i in range(21)]

    for i in range(21):
        distFromCOM[i] = getDistance((comX, comY), (lmList[i][1], lmList[i][2]))
        angleFromCOM[i] = getAngle((comX, comY), (lmList[i][1], lmList[i][2]))

    return distFromCOM, angleFromCOM