# fuck around and shorten it I guess
# What can't I do with list comprehension, reduce, and the newly learned walrus operator?
from functools import reduce
from math import ceil
print(reduce(lambda a, b: a*b, [reduce(lambda c, d: c+d, [([ceil(delta_x * len(arr) / delta_y / len(arr)) * line for line in arr][y_pos][x_pos] == '#') for x_pos, y_pos in zip(range(0, 10000000, delta_x), range(0, len((arr := [line.rstrip('\n') for line in open('input.txt')])), delta_y))]) for delta_x, delta_y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]], 1))
