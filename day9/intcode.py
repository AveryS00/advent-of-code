class IntcodeProcessor:
    MAX_PARAMS = 3
    
    def __init__(self, intcode, inputArr=None, consoleOut=True):
        self.intcode = intcode
        self.index = 0
        self.inputIdx = 0
        self.consoleOut = consoleOut
        if not consoleOut:
            self.output = None
        self.inputArr = inputArr
        self.rbOffset = 0

    ##Return 0 if complete, 1 if paused, -1 if abnormal termination
    def runOpcode(self):
        while self.index < len(self.intcode):
            op = self.readCode()
            if op[0] == 1:
                self.opAdd(op[1], op[2], op[3])
            elif op[0] == 2:
                self.opMultiply(op[1], op[2], op[3])
            elif op[0] == 3:
                self.intcode[self.getPos(self.index+1, op[1])] = self.inputArr[self.inputIdx]
                self.inputIdx += 1
                self.index += 2
            elif op[0] == 4:
                if self.consoleOut:
                    print(self.getVal(self.index+1, op[1]))
                    self.index += 2
                else:
                    self.output = self.getVal(self.index+1, op[1])
                    self.index += 2
                    return 1
            elif op[0] == 5:
                self.opJumpIfTrue(op[1], op[2])
            elif op[0] == 6:
                self.opJumpIfFalse(op[1], op[2])
            elif op[0] == 7:
                self.opLessThan(op[1], op[2], op[3])
            elif op[0] == 8:
                self.opEquals(op[1], op[2], op[3])
            elif op[0] == 9:
                self.rbOffset += self.getVal(self.index+1, op[1])
                self.index += 2
            elif op[0] == 99:
                return 0
            else:
                print('Invalid input')
                self.index += 1
        print('Abnormal Termination')
        return -1

    def expandMemory(self, idx):
        while idx >= len(self.intcode):
            self.intcode.append(0)

    def opAdd(self, param1, param2, param3):
        self.expandMemory(self.intcode[self.index+3])
        self.intcode[self.getPos(self.index+3, param3)] = self.getVal(self.index+1, param1) + self.getVal(self.index+2, param2)
        self.index += 4
        
    def opMultiply(self, param1, param2, param3):
        self.expandMemory(self.intcode[self.index+3])
        self.intcode[self.getPos(self.index+3, param3)] = self.getVal(self.index+1, param1) * self.getVal(self.index+2, param2)
        self.index += 4
        
    def opJumpIfTrue(self, param1, param2):
        if self.getVal(self.index+1, param1):
            self.index = self.getVal(self.index+2, param2)
        else:
            self.index += 3
            
    def opJumpIfFalse(self, param1, param2):
        if not self.getVal(self.index+1, param1):
            self.index = self.getVal(self.index+2, param2)
        else:
            self.index += 3
            
    def opLessThan(self, param1, param2, param3):
        self.expandMemory(self.intcode[self.index+3])
        if self.getVal(self.index+1, param1) < self.getVal(self.index+2, param2):
            self.intcode[self.getPos(self.index+3, param3)] = 1
        else:
            self.intcode[self.getPos(self.index+3, param3)] = 0
        self.index += 4
        
    def opEquals(self, param1, param2, param3):
        self.expandMemory(self.intcode[self.index+3])
        if self.getVal(self.index+1, param1) == self.getVal(self.index+2, param2):
            self.intcode[self.getPos(self.index+3, param3)] = 1
        else:
            self.intcode[self.getPos(self.index+3, param3)] = 0
        self.index += 4

    def getVal(self, idx, param):
        if param == 2:
            self.expandMemory(self.rbOffset + idx)
            return self.intcode[self.intcode[idx] + self.rbOffset]
        elif param:
            return self.intcode[idx]
        self.expandMemory(self.intcode[idx])
        return self.intcode[self.intcode[idx]]

    def getPos(self, idx, param):
        if param == 2:
            self.expandMemory(self.rbOffset + self.intcode[idx])
            return self.intcode[idx] + self.rbOffset
        elif param:
            print('Invalid Parameter')
            return idx
        self.expandMemory(self.intcode[idx])
        return self.intcode[idx]

    def readCode(self):
        op = []
        code = str(self.intcode[self.index])
        op.append(int(code[-2:]))
        code = code[:-2]
        for i in code[::-1]:
            op.append(int(i))
        for i in range(len(code), 3):
            op.append(0)
        return op
        
