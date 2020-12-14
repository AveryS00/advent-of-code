from typing import List, Dict


def equation_system(bus_list: List[str]) -> Dict[int, int]:
    busses = {}
    remainder = 0
    for bus_id in bus_list:
        if bus_id != 'x':
            busses[int(bus_id)] = remainder
        remainder += 1
    sorted_by_id = {}
    for key, value in sorted(busses.items(), reverse=True):
        sorted_by_id[key] = value
    return sorted_by_id


def crt_sieve(bus_list: Dict[int, int]):
    current_product = 1
    next_product = 1
    x = 0
    for mod, remainder in bus_list.items():
        next_product *= mod
        arith_progression = [x + current_product * j for j in range(next_product // current_product)]
        for val in arith_progression:
            if val % mod == -remainder % mod:
                x = val
                break
        current_product = next_product
    return x


def find_closest_time(timestamp, bus_list):
    closest_time = 1000
    min_id = 0
    for bus_id in bus_list:
        if bus_id != 'x':
            loop = int(bus_id)
            while loop <= timestamp:
                loop += int(bus_id)
            diff = loop - timestamp
            if diff < closest_time:
                closest_time = diff
                min_id = int(bus_id)
    return min_id * closest_time


with open('input.txt') as f:
    arr = [line.rstrip('\n') for line in f]

print(find_closest_time(int(arr[0]), arr[1].split(',')))
print(crt_sieve(equation_system(arr[1].split(','))))
