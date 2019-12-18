IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6

def processData(string):
    layers= []
    while len(string) >= IMAGE_WIDTH * IMAGE_HEIGHT:
        layers.append(string[:IMAGE_WIDTH * IMAGE_HEIGHT])
        string = string[IMAGE_WIDTH * IMAGE_HEIGHT:]
    decodedPicture = ''
    for i in range(IMAGE_WIDTH * IMAGE_HEIGHT):
        decodedPicture += getValue(layers, i)
    printPicture(decodedPicture)
        
def getValue(layers, index):
    for i in layers:
        if i[index] != '2':
            return i[index]
    return '2'

def printPicture(picture):
    for i in range(len(picture)):
        if picture[i] == '2':
            print(" ", end = '')
        elif picture[i] == '1':
            print("0", end = '')
        else:
            print("X", end = '')
        if (i + 1) % 25 == 0 and i != 0:
            print()

    #Part 1
    #leastZeroLayer = findLeastZeroes(layers)
    #return layers[leastZeroLayer].count('1') * layers[leastZeroLayer].count('2')

def findLeastZeroes(arr):
    layer = 0
    leastZeroes = 10000
    for i in range(len(arr)):
        zeroes = arr[i].count('0')
        if zeroes < leastZeroes:
            leastZeroes = zeroes
            layer = i
    return layer

if __name__=='__main__':
    with open('input.txt') as f:
        data = f.read()
    processData(data)
    
