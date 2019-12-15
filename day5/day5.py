MAX_PARAMS = 3

def runOpcode(arr):
    idx = 0
    while idx < len(arr):
        op = arr[idx][-2:]
        if op[0] == '0':
            op = op[1:]
        opParam = fillZeros(arr[idx][:-2])
        if op == '1':
            arr[int(arr[idx+3])] = str(getVal(arr, idx+1, opParam[-1]) + getVal(arr, idx+2, opParam[-2]))
            idx += 4
        elif op == '2':
            arr[int(arr[idx+3])] = str(getVal(arr, idx+1, opParam[-1]) * getVal(arr, idx+2, opParam[-2]))
            idx += 4
        elif op == '3':
            arr[int(arr[idx+1])] = input("Enter input value: ")
            idx += 2
        elif op == '4':
            print(getVal(arr, idx+1, opParam[-1]))
            idx += 2
        elif op == '5':
            if getVal(arr, idx+1, opParam[-1]):
                idx = getVal(arr, idx+2, opParam[-2])
            else:
                idx += 3
        elif op == '6':
            if not getVal(arr, idx+1, opParam[-1]):
                idx = getVal(arr, idx+2, opParam[-2])
            else:
                idx += 3
        elif op == '7':
            if getVal(arr, idx+1, opParam[-1]) < getVal(arr, idx+2, opParam[-2]):
                arr[int(arr[idx+3])] = '1'
            else:
                arr[int(arr[idx+3])] = '0'
            idx += 4
        elif op == '8':
            if getVal(arr, idx+1, opParam[-1]) == getVal(arr, idx+2, opParam[-2]):
                arr[int(arr[idx+3])] = '1'
            else:
                arr[int(arr[idx+3])] = '0'
            idx += 4
        elif op== '99':
            return arr
        else:
            print('Invalid input')
            idx += 1
    print('Abnormal Termination')
    return arr


def getVal(arr, index, param):
    if int(param):
        return int(arr[index])
    return int(arr[int(arr[index])])

def fillZeros(inputStr):
    global MAX_PARAMS
    while len(inputStr) < MAX_PARAMS:
        inputStr = '0' + inputStr
    return inputStr

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [i for i in f.read().split(',')]
    runOpcode(lines)
    


