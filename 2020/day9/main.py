from typing import List


def validate_num(num: int, index: int, preamble_len: int, xmas_list: List[int]) -> bool:
    possible_vals = xmas_list[index-preamble_len:index]
    for i in possible_vals:
        if num - i in possible_vals and num - i != i:
            return True
    return False


def find_invalid_num(preamble_len: int, xmas_list: List[int]):
    index = preamble_len
    while index < len(xmas_list):
        if not validate_num(xmas_list[index], index, preamble_len, xmas_list):
            return xmas_list[index]
        index += 1


def find_continuous_sum(look: int, xmas_list: List[int]) -> List[int]:
    for i in range(len(xmas_list)):
        current_sum = xmas_list[i]
        for j in range(i + 1, len(xmas_list)):
            current_sum += xmas_list[j]
            if current_sum == look:
                return xmas_list[i: j+1]
            elif current_sum > look:
                break


with open('input.txt') as f:
    arr = [int(line.rstrip('\n')) for line in f]

result = find_invalid_num(25, arr)
print(result)

r2 = find_continuous_sum(result, arr)
print(min(r2) + max(r2))
