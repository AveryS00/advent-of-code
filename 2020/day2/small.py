from re import sub
from functools import reduce
print(reduce(lambda a, b: a + b, [(sub('[:\n]', '', i).split(' ')[2][int(sub('[:\n]', '', i).split(' ')[0].split('-')[0]) - 1] == sub('[:\n]', '', i).split(' ')[1]) ^ (sub('[:\n]', '', i).split(' ')[2][int(sub('[:\n]', '', i).split(' ')[0].split('-')[1]) - 1] == sub('[:\n]', '', i).split(' ')[1]) for i in open('input.txt')]))