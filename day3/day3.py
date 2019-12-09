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
        if abs(i[0]) + abs(i[1]) < minDistance:
            minDistance = abs(i[0]) + abs(i[1])
    return minDistance


if __name__ == '__main__':
    with open('input.txt') as f:
        text = [str(i) for i in f.read().split(',')]
    print(closestCross(findCrosses(text)))
