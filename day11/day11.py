from intcode import IntcodeProcessor
from enum import IntEnum

class direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

robotFacing = direction.UP

def createRobotTrail(intcode):
    global robotFacing
    trail = {}
    robot = IntcodeProcessor(intcode, [1], False, False)
    robot.runOpcode()
    trail[(0,0)] = robot.output
    point = [0,0]
    while robot.runOpcode():
        turnRobot(robot.output)
        moveRobot(point)
        if (point[0], point[1]) in trail:
            robot.inputArr.append(trail[(point[0], point[1])])
        else:
            trail[(point[0], point[1])] = 0
            robot.inputArr.append(0)
        robot.runOpcode()
        trail[(point[0], point[1])] = robot.output
    return trail

def printPaint(paintTrail):
    for i in range(5,-10,-1):
        for j in range(-10,60):
            if (j, i) in paintTrail:
                if paintTrail[(j, i)]:
                    print('X', end='')
                else:
                    print(' ', end='')
            else:
                print(' ', end='')
        print()

def moveRobot(point):
    global robotFacing
    if robotFacing == direction.UP:
        point[1] += 1
    elif robotFacing == direction.RIGHT:
        point[0] += 1
    elif robotFacing == direction.LEFT:
        point[0] -= 1
    elif robotFacing == direction.DOWN:
        point[1] -= 1
    else:
        print("invalid direction")
        
def turnRobot(direction):
    global robotFacing
    if direction:
        robotFacing = (robotFacing + 1) % 4
    else:
        robotFacing = (robotFacing - 1) % 4

if __name__=='__main__':
    with open('input.txt') as f:
        code = [int(i) for i in f.read().split(',')]
    paint = createRobotTrail(code)
    printPaint(paint)
    
