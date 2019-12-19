      
def calculateSlope(point1, point2):
    if point2[0] == point1[0]:
        if point2[1] - point1[1] < 0:
            return -float('inf')
        return float('inf')
    if (point2[1]-point1[1])/(point2[0]-point1[0]) == -0.0:
        return 0.0
    return (point2[1]-point1[1])/(point2[0]-point1[0])

# Yikes. To be fair, though. I know exactly why it works. It just looks messy.
def findVisibleAsteroids(point, asteroids):
    slopes = {}
    for i in asteroids:
        if point != i:
            currentSlope = calculateSlope(point, i)
            if currentSlope not in slopes.keys():
                if currentSlope == 0.0:
                    if i[0] > point[0]:
                        slopes[currentSlope] = [i, None]
                    else:
                        slopes[currentSlope] = [None, i]
                elif currentSlope > 0.0:
                    if i[1] > point[1]:
                        slopes[currentSlope] = [i, None]
                    else:
                        slopes[currentSlope] = [None, i]
                else:
                    if i[1] < point[1]:
                        slopes[currentSlope] = [i, None]
                    else:
                        slopes[currentSlope] = [None, i]
            else:
                if currentSlope == 0.0:
                    if i[0] > point[0]:
                        if slopes[currentSlope][0] is None:
                            slopes[currentSlope][0] = i
                        else:
                            if slopes[currentSlope][0][0] > i[0]:
                                slopes[currentSlope][0] = i
                    else:
                        if slopes[currentSlope][1] is None:
                            slopes[currentSlope][1] = i
                        else:
                            if slopes[currentSlope][1][0] < i[0]:
                                slopes[currentSlope][1] = i
                elif currentSlope > 0.0:
                    if i[1] > point[1]:
                        if slopes[currentSlope][0] is None:
                            slopes[currentSlope][0] = i
                        else:
                            if slopes[currentSlope][0][1] > i[1]:
                                slopes[currentSlope][0] = i
                    else:
                        if slopes[currentSlope][1] is None:
                            slopes[currentSlope][1] = i
                        else:
                            if slopes[currentSlope][1][1] < i[1]:
                                slopes[currentSlope][1] = i
                else:
                    if i[1] < point[1]:
                        if slopes[currentSlope][0] is None:
                            slopes[currentSlope][0] = i
                        else:
                            if slopes[currentSlope][0][1] < i[1]:
                                slopes[currentSlope][0] = i
                    else:
                        if slopes[currentSlope][1] is None:
                            slopes[currentSlope][1] = i
                        else:
                            if slopes[currentSlope][1][1] > i[1]:
                                slopes[currentSlope][0] = i
    return slopes

def get200thAsteroid(point, asteroids):
    destroyed = 0
    while destroyed < 200:
        visible = findVisibleAsteroids(point, asteroids)
        keys = sorted(visible.keys())
        for i in keys:
            if visible[i][0] is not None:
                if destroyed == 199:
                    return visible[i][0]
                asteroids.remove(visible[i][0])
                visible[i][0] = None
                destroyed += 1
        for i in keys:
            if visible[i][1] is not None:
                if destroyed == 199:
                    return visible[i][1]
                asteroids.remove(visible[i][1])
                visible[i][0] = None
                destroyed += 1
        

def numVisible(asteroids):
    total = 0
    for i in asteroids.values():
        for j in i:
            if j is not None:
                total += 1
    return total

def maxVisibleAsteroids(asteroids):
    maxVis = 0
    asteroid = ()
    for i in asteroids:
        visible = numVisible(findVisibleAsteroids(i, asteroids))
        if visible > maxVis:
            maxVis = visible
            asteroid = i
    return [maxVis, asteroid]

def getAsteroids(arr):
    asteroidPoints = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '#':
                asteroidPoints.append((j,i))
    return asteroidPoints

if __name__=='__main__':
    with open('input.txt') as f:
        lines = [i for i in f.read().split('\n') ]
    asteroids = getAsteroids(lines)
    aStar = maxVisibleAsteroids(asteroids)
    print(aStar[0])
    a200th = get200thAsteroid(aStar[1], asteroids)
    print(a200th, a200th[0]*100 + a200th[1])
    
