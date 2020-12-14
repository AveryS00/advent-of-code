from typing import List, Dict
from math import comb


def compute_diffs(adapters: List[int]) -> Dict[int, int]:
    diffs = {}
    for i in adapters[:-1]:
        diffs[i] = -1
        for j in range(1, 4):
            if i + j in adapters:
                diffs[i] += 1
    diffs[adapters[-1]] = 0
    return diffs


def find_largest_diff(current_adapter, adapters, totals):
    for j in range(3, 0, -1):
        for adapter in adapters:
            if adapter - current_adapter == j:
                totals[adapter - current_adapter - 1] += 1
                return adapter


def find_smallest_diff(current_adapter, adapters, totals):
    for j in range(1, 4):
        for adapter in adapters:
            if adapter - current_adapter == j:
                totals[adapter - current_adapter - 1] += 1
                return adapter


def find_total_diff_small(adapters: List[int]) -> List[int]:
    totals = [0, 0, 1]
    current_adapter = 0
    for i in range(len(adapters)):
        current_adapter = find_smallest_diff(current_adapter, adapters, totals)
    return totals


def compute_combinations(totals: List[int], adapters: List[int]) -> int:
    num_left = len(adapters) - totals[0] - totals[1] - totals[2]
    combs = 0
    for i in range(num_left + 1):
        combs += comb(num_left, i)

    #  No
    adapters.sort()
    diffs = compute_diffs(adapters)
    two_diffs = 0
    for i in range(len((vals := list(diffs.values()))) - 1):
        two_diffs += (vals[i] == 2)
        two_diffs += (vals[i] == 1 and vals[i+1] == 1)
    return combs * two_diffs


def find_total_diff_large(adapters: List[int]) -> List[int]:
    totals = [0, 0, 0]
    seen = []
    current_adapter = 0
    highest_adapter = max(adapters)
    while current_adapter != highest_adapter:
        current_adapter = find_largest_diff(current_adapter, adapters, totals)
        seen.append(current_adapter)
    return totals


with open('example2.txt') as f:
    arr = [int(line.rstrip('\n')) for line in f]


result = find_total_diff_small(arr)
print(result[0]*result[2])


# Here's how I want to solve part 2. Find the smallest path for adapters by taking the largest gaps possible.
# Then, everything else just has to be inserted in somewhere to generate the combinations.
# Let n = number of adapters, Let k = length of shortest adapter chain. Then the answer is the summation from
# i = 0 -> k of k choose i.
result2 = find_total_diff_large(arr)
print(compute_combinations(result2, arr))
