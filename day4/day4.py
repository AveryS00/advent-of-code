import re

#Based on range from input
MINVAL = 147981
MAXVAL = 691423

def numCombinations():
    global MINVAL
    global MAXVAL
    sum = 0
    for i in range(MINVAL, MAXVAL):
        if isValidPassword(str(i)):
            sum = sum + 1
    return sum

#Does not check if in range, assumes it is
def isValidPassword(password):
    if not isNonDecreasing(password):
        return False;
    if not onlyDoubledDigit(password):
        return False;
    return True;

def isNonDecreasing(password):
    highestNumSeen = password[0]
    for i in password:
        if int(i) < int(highestNumSeen):
            return False
        else:
            highestNumSeen = i
    return True

def onlyDoubledDigit(password):
    pattern = re.compile("00|11|22|33|44|55|66|77|88|99")
    match = pattern.search(password)
    if match is None:
        return False
    newPattern = re.compile(match.group(0))
    newStr = re.sub(newPattern, '', password, 1)
    if match.group(0)[0] in newStr:
        return onlyDoubledDigit(re.sub(newPattern, '', newStr))
    return True
    

if __name__ == '__main__':
    print(numCombinations())
