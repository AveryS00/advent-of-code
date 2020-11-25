from copy import deepcopy

wire1List = []
crossList = []

def traverseWire1(arr):
    global wire1List
    point = [0,0]
    for i in range(len(arr)):
        if arr[i][0] == 'R':
            for j in range(int(arr[i][1:])):
                point[0] = point[0] + 1
                wire1List.append((point[0], point[1]))
        elif arr[i][0] == 'L':
            for j in range(int(arr[i][1:])):
                point[0] = point[0] - 1
                wire1List.append((point[0], point[1]))
        elif arr[i][0] == 'U':
            for j in range(int(arr[i][1:])):
                point[1] = point[1] + 1
                wire1List.append((point[0], point[1]))
        elif arr[i][0] == 'D':
            for j in range(int(arr[i][1:])):
                point[1] = point[1] - 1
                wire1List.append((point[0], point[1]))
                
def traverseWire2(arr):
    steps = 0
    global wire1List
    global crossList
    point = [0,0]
    for i in range(len(arr)):
        if arr[i][0] == 'R':
            for j in range(int(arr[i][1:])):
                point[0] = point[0] + 1
                steps += 1
                if (point[0], point[1]) in wire1List:
                    crossList.append(((point[0], point[1]), steps))
        elif arr[i][0] == 'L':
            for j in range(int(arr[i][1:])):
                steps += 1
                point[0] = point[0] - 1
                if (point[0], point[1]) in wire1List:
                    crossList.append(((point[0], point[1]), steps))
        elif arr[i][0] == 'U':
            for j in range(int(arr[i][1:])):
                steps += 1
                point[1] = point[1] + 1
                if (point[0], point[1]) in wire1List:
                    crossList.append(((point[0], point[1]), steps))
        elif arr[i][0] == 'D':
            for j in range(int(arr[i][1:])):
                point[1] = point[1] - 1
                steps += 1
                if (point[0], point[1]) in wire1List:
                    crossList.append(((point[0], point[1]), steps))
    return steps

def closestCross():
    global crossList
    minDistance = 1000000
    for i in crossList:
        if abs(i[0][0]) + abs(i[0][1]) < minDistance:
            minDistance = abs(i[0][0]) + abs(i[0][1])
    return minDistance

def minSteps():
    global crossList
    global wire1List
    minSteps = 100000000
    for i in crossList:
        wire1steps = wire1List.index(i[0]) + 1
        if i[1] + wire1steps < minSteps:
            minSteps = i[1] + wire1steps
    return minSteps

def inSeen(point, arr):
    for i in arr:
        if i[0] == point[0] and i[1] == point[1]:
            return True
    return False



if __name__ == '__main__':
    with open('input.txt') as f:
        wire1 = f.readline()
        wire1 = wire1.strip('\n').split(',')
        wire2 = f.readline()
        wire2 = wire2.split(',')
    traverseWire1(wire1)
    traverseWire2(wire2)
    print(closestCross())
    print(minSteps())
    
