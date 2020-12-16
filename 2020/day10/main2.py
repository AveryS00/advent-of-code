from typing import List, Dict
from math import comb

'''
def compute_diffs(adapters: List[int]) -> Dict[int, int]:
    diffs = {}
    for i in adapters[:-1]:
        diffs[i] = -1
        for j in range(1, 4):
            if i + j in adapters:
                diffs[i] += 1
    diffs[adapters[-1]] = 0
    return diffs


def compute_combinations(adapters: List[int]) -> int:
    count = 0
    adapters.sort()
    diffs = compute_diffs(adapters)
    for key, val in diffs.items():
        if val != 0:
            if key + 1 in diffs:
                count += comb(3, diffs[key + 1])
            for i in range(2, 4):
                if key + i in diffs:
                    count += comb(3, diffs[key + i]) - diffs[key + i - 1]
    return count
'''


def generate_graph(adapters: List[int]) -> Dict[int, List[int]]:
    adapters = [0] + adapters  # Append zero to the front
    adapters.sort()  # Sort now for faster filling later
    adapters_set = set(adapters)
    graph = {}
    for adapter in adapters:
        graph[adapter] = []
        for i in range(1, 4):
            if adapter + i in adapters_set:
                graph[adapter] += [adapter + i]
    return graph


with open('example.txt') as f:
    arr = [int(line.rstrip('\n')) for line in f]
print()
