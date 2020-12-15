from typing import List


def play_game(starting_numbers: List[int], max_iter: int) -> int:
    """Play the Recitation game for the given number of iterations

    :param starting_numbers: The list of starting numbers
    :param max_iter: The total number of turns to play
    :return: The last spoken number at max_iter
    """
    last_turn_spoken = {}
    current_turn = 1
    for starting_number in starting_numbers[:-1]:
        last_turn_spoken[starting_number] = current_turn
        current_turn += 1

    next_spoken = starting_numbers[-1]

    while current_turn < max_iter:
        if next_spoken not in last_turn_spoken:
            last_turn_spoken[next_spoken] = current_turn
            next_spoken = 0
        else:
            temp = current_turn - last_turn_spoken[next_spoken]
            last_turn_spoken[next_spoken] = current_turn
            next_spoken = temp
        current_turn += 1
    return next_spoken


with open('input.txt') as f:
    starting_nums = [int(num) for num in f.read().split(',')]

print(play_game(starting_nums, 2020))
print(play_game(starting_nums, 30000000))
