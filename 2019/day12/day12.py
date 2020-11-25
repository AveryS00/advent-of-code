import re

def totalEnergy(moonPos):
    moonVel = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for i in range(1000):
        runStep(moonPos, moonVel)
    totalEnergy = 0
    for i in range(4):
        totalEnergy += calculateEnergy(moonPos[i], moonVel[i])
    return totalEnergy

def calculateEnergy(pos, vel):
    potential = abs(pos[0]) + abs(pos[1]) + abs(pos[2])
    kinetic = abs(vel[0]) + abs(vel[1]) + abs(vel[2])
    return potential * kinetic

def runStep(moonPos, moonVel):
    for i in range(len(moonPos)):
        calculateVelocity(moonPos[i], moonVel[i], moonPos[:i]+moonPos[i+1:])
    for i in range(len(moonPos)):
        for j in range(len(moonPos[i])):
            moonPos[i][j] += moonVel[i][j]

def hashState(moonPos, moonVel):
    stateStr = ''
    for i in range(len(moonPos)):
        for j in range(len(moonPos[i])):
            stateStr = stateStr + str(moonPos[i][j]) #+ str(moonVel[i][j])
    return stateStr

def findRepeatedState(moonPos):
    moonVel = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    steps = 0
    #states = set()
    initialState = hashState(moonPos, moonVel)
    currentState = ''
    #while currentState not in states:
    while currentState != initialState:
        #Cycle cannot start at any point other than initial
        #states.add(currentState)
        runStep(moonPos, moonVel)
        currentState = hashState(moonPos, moonVel)
        steps += 1
        if steps % 1000000 == 0:
            print(steps)
    return steps

def calculateVelocity(moonPos, moonVel, otherMoons):
    for i in range(3):
        velAdd = 0
        for j in otherMoons:
            if j[i] > moonPos[i]:
                velAdd += 1
            elif j[i] < moonPos[i]:
                velAdd -= 1
        moonVel[i] += velAdd
        
if __name__=='__main__':
    with open('input.txt') as f:
        line = f.readlines()
    moons = []
    for i in line:
        pattern = re.compile('-?[0-9]+')
        moons.append([int(j) for j in re.findall(pattern, i)])
    #print(totalEnergy(moons))
    print(findRepeatedState(moons))
    
