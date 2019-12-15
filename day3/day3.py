from copy import deepcopy
#FUCK
def findCrosses(arr):
    cross = []
    seen = []
    point = [0,0]
    for i in range(len(arr)):
        if arr[i][0] == 'R':
            for j in range(int(arr[i][1:])):
                point[0] = point[0] + 1
                if any(point[0] == elem[0] and point[1] == elem[1] for elem in seen):
                    cross.append(deepcopy(point))
                else:
                    seen.append(deepcopy(point))
        elif arr[i][0] == 'L':
            for j in range(int(arr[i][1:])):
                point[0] = point[0] - 1
                if any(point[0] == elem[0] and point[1] == elem[1] for elem in seen):
                    cross.append(deepcopy(point))
                else:
                    seen.append(deepcopy(point))
        elif arr[i][0] == 'U':
            for j in range(int(arr[i][1:])):
                point[1] = point[1] + 1
                if any(point[0] == elem[0] and point[1] == elem[1] for elem in seen):
                    cross.append(deepcopy(point))
                else:
                    seen.append(deepcopy(point))
        elif arr[i][0] == 'D':
            for j in range(int(arr[i][1:])):
                point[1] = point[1] - 1
                if any(point[0] == elem[0] and point[1] == elem[1] for elem in seen):
                    cross.append(deepcopy(point))
                else:
                    seen.append(deepcopy(point))
    return cross

def closestCross(arr):
    minDistance = 1000000
    for i in arr:
        if abs(i[0]) + abs(i[1]) + 2 < minDistance:
            minDistance = abs(i[0]) + abs(i[1]) + 2
    return minDistance

def inSeen(point, arr):
    for i in arr:
        if i[0] == point[0] and i[1] == point[1]:
            return True
    return False

def createCrossList(arr):
    cross = []
    seen = []
    point = [0,0]
    for i in arr:
        direction = i[0]
        if direction == 'R':
            for j in range(int(i[1:])):
                point[0] = point[0] + 1
                if inSeen(point, seen):
                    cross.append([point[0], point[1]])
                else:
                    seen.append([point[0], point[1]])
        elif direction == 'U':
            for j in range(int(i[1:])):
                point[1] = point[1] + 1
                if inSeen(point, seen):
                    cross.append([point[0], point[1]])
                else:
                    seen.append([point[0], point[1]])
        elif direction == 'L':
            for j in range(int(i[1:])):
                point[0] = point[0] - 1
                if inSeen(point, seen):
                    cross.append([point[0], point[1]])
                else:
                    seen.append([point[0], point[1]])
        elif direction == 'D':
            for j in range(int(i[1:])):
                point[1] = point[1] - 1
                if inSeen(point, seen):
                    cross.append([point[0], point[1]])
                else:
                    seen.append([point[0], point[1]])
    return cross

def pathList(arr):
    path = []
    start = [0,0]
    for i in arr:
        for j in range(int(i[1:])):
            path.append(tuple((start[:])))
            if i[0] == 'R':
                start[0] += 1
            elif i[0] == 'U':
                start[1] += 1
            elif i[0] == 'L':
                start[0] -= 1
            elif i[0] == 'D':
                start[1] -= 1
            else:
                print('invalid input')
    return path

def getCrosses(arr):
    return set([i for i in arr if arr.count(i)>1])

if __name__ == '__main__':
    with open('input.txt') as f:
        text = [str(i) for i in f.read().split(',')]
    with open('test1.txt') as f:
        test1 = [str(i) for i in f.read().split(',')]
    with open('test2.txt') as f:
        test2 = [str(i) for i in f.read().split(',')]
    #print(closestCross(getCrosses(pathList(test1))))
    #print(closestCross(getCrosses(pathList(test2))))
    #crossList = createCrossList(text)
    #print(crossList)
    #print(closestCross(crossList))
