from intcode import IntcodeProcessor




if __name__=='__main__':
    with open('input.txt') as f:
        lines = [int(i) for i in f.read().split(',')]
    # Part 1
    # a = IntcodeProcessor(lines, [1])
    # Part 2
    a = IntcodeProcessor(lines, [2])
    a.runOpcode()
