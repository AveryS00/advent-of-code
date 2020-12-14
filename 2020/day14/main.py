import re
from typing import List, Dict
from functools import reduce


def run_masks(assign_arr: List[str]) -> List[int]:
    memory = {}
    mask_pattern = re.compile('mask = ')
    mem_pattern = re.compile('[0-9]+')
    mask = ''
    for command in assign_arr:
        if re.match(mask_pattern, command):
            mask = re.sub(mask_pattern, '', command)
        else:
            address, binary = re.findall(mem_pattern, command)
            binary = '{0:b}'.format(int(binary))
            binary = (len(mask) - len(binary)) * '0' + binary
            for i in range(len(mask)):
                if mask[i] != 'X':
                    binary = binary[:i] + mask[i] + binary[i+1:]
            memory[address] = int(binary, 2)
    return list(memory.values())


def assign_all_mem(binary_address: str, value: int, memory: Dict[str, int]):
    if 'X' not in binary_address:
        memory[binary_address] = value
        return

    assign_all_mem(binary_address.replace('X', '0', 1), value, memory)
    assign_all_mem(binary_address.replace('X', '1', 1), value, memory)


def floating_memory(assign_arr: List[str]) -> int:
    memory = {}
    mask_pattern = re.compile('mask = ')
    mem_pattern = re.compile('[0-9]+')
    mask = ''
    for command in assign_arr:
        if re.match(mask_pattern, command):
            mask = re.sub(mask_pattern, '', command)
        else:
            address, value = re.findall(mem_pattern, command)
            binary = '{0:b}'.format(int(address))
            binary = (len(mask) - len(binary)) * '0' + binary
            for i in range(len(mask)):
                if mask[i] != '0':
                    binary = binary[:i] + mask[i] + binary[i + 1:]
            assign_all_mem(binary, int(value), memory)
    return reduce(lambda a, b: a + b, list(memory.values()))


with open('input.txt') as f:
    arr = [line.rstrip('\n') for line in f]

print(reduce(lambda a, b: a+b, run_masks(arr)))
print(floating_memory(arr))
