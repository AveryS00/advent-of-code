from copy import deepcopy
from itertools import permutations
from intcode import IntcodeProcessor

def runAmps(intcode, order):
    ouput = 0
    ampA = IntcodeProcessor(deepcopy(intcode))
    ampB = IntcodeProcessor(deepcopy(intcode))
    ampC = IntcodeProcessor(deepcopy(intcode))
    ampD = IntcodeProcessor(deepcopy(intcode))
    ampE = IntcodeProcessor(deepcopy(intcode))
    ampA.inputArr = [int(order[0]), 0]
    ampA.runOpcode()
    ampB.inputArr = [int(order[1]), ampA.output]
    ampB.runOpcode()
    ampC.inputArr = [int(order[2]), ampB.output]
    ampC.runOpcode()
    ampD.inputArr = [int(order[3]), ampC.output]
    ampD.runOpcode()
    ampE.inputArr = [int(order[4]), ampD.output]
    while ampE.runOpcode():
       ampA.inputArr.append(ampE.output)
       ampA.runOpcode()
       ampB.inputArr.append(ampA.output)
       ampB.runOpcode()
       ampC.inputArr.append(ampB.output)
       ampC.runOpcode()
       ampD.inputArr.append(ampC.output)
       ampD.runOpcode()
       ampE.inputArr.append(ampD.output)
    return ampE.output

def runAmpCombinations(intcode, combinations):
    highestSeen = 0
    comb = ''
    for i in combinations:
        output = runAmps(intcode, i)
        if int(output) > highestSeen:
            highestSeen = int(output)
            comb = i
    return highestSeen
    
if __name__=='__main__':
    with open('input.txt') as f:
        lines = [int(i) for i in f.read().split(',')]
    combinations = [''.join(p) for p in permutations('56789')]
    combinations = set(combinations)
    print(runAmpCombinations(lines, combinations))

    

