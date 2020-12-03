# fuck around and shorten it I guess
# not at all efficient. It's remaking the inputs every single iteration
from functools import reduce
from math import ceil
print(reduce(lambda a, b: a*b, [reduce(lambda c, d: c+d, [([ceil(delta_x * len([line.rstrip('\n') for line in open('input.txt')]) / delta_y / len([line.rstrip('\n') for line in open('input.txt')][0])) * line for line in [line.rstrip('\n') for line in open('input.txt')]][y_pos][x_pos] == '#') for x_pos, y_pos in zip(range(0, 10000000, delta_x), range(0, len([line.rstrip('\n') for line in open('input.txt')]), delta_y))]) for delta_x, delta_y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]], 1))
