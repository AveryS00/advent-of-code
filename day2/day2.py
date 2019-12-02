import copy

def opcode(arr):
	idx = 0
	while idx < len(arr):
		if arr[idx] == 1:
			arr[arr[idx+3]] = arr[arr[idx+1]] + arr[arr[idx+2]]
		elif arr[idx] == 2:
			arr[arr[idx+3]] = arr[arr[idx+1]] * arr[arr[idx+2]]
		elif arr[idx] == 99:
			break
		else:
			print('Invalid input')
		idx = idx + 4
	return arr


def findNounVerb(arr):
	for i in range(0,99):
		for j in range(0,99):
			arrCopy = copy.deepcopy(arr)
			arrCopy[1] = i
			arrCopy[2] = j
			if opcode(arrCopy)[0] == 19690720:
				return 100 * i + j

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [int(i) for i in f.read().split(',')]
    lineCopy = copy.deepcopy(lines)
    lineCopy[1] = 12
    lineCopy[2] = 2
    print(opcode(lineCopy)[0])
    print(findNounVerb(lines))
    


