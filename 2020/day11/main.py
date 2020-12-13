from typing import List
from copy import deepcopy


def count_occupied_seats(seats: List[List[str]]) -> int:
    count = 0
    for x in range(len(seats)):
        for y in range(len(seats[0])):
            count += (seats[x][y] == '#')
    return count


def occupied_adjacent_seats(cell_x: int, cell_y: int, seats: List[List[str]]) -> int:
    """
    0,0     1,0     2,0
    0,1     1,1     2,1
    0,2     1,2     2,2
    """
    count = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if 0 <= cell_x + x < len(seats) and 0 <= cell_y + y < len(seats[0]) and (x != 0 or y != 0):
                count += (seats[cell_x + x][cell_y + y] == '#')
    return count


def run_iteration(seats: List[List[str]]) -> List[List[str]]:
    new_seats = deepcopy(seats)
    for x in range(len(seats)):
        for y in range(len(seats[0])):
            if seats[x][y] != '.':
                num_adjacent = occupied_adjacent_seats(x, y, seats)
                if seats[x][y] == 'L':
                    if num_adjacent == 0:
                        new_seats[x][y] = '#'
                else:
                    if num_adjacent >= 4:
                        new_seats[x][y] = 'L'
    return new_seats


def run_seat_game(seats: List[List[str]]) -> int:
    new_seats = run_iteration(seats)
    while new_seats != seats:
        seats = new_seats
        new_seats = run_iteration(seats)
    return count_occupied_seats(new_seats)


with open('input.txt') as f:
    arr = [line.rstrip('\n') for line in f]

arrangement = [[char for char in i] for i in arr]

print(run_seat_game(arrangement))
