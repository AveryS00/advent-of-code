from typing import List
from copy import deepcopy


def print_seats(seats: List[List[str]]):
    for row in seats:
        for seat in row:
            print(seat, end='')
        print()
    print(len(seats[0])*'-')


def find_vis(seat_x: int, seat_y: int, op1: str, op2: str, condition1: str, condition2: str,
             x_increment: int, y_increment: int, seats: List[List[str]]) -> bool:
    index_x = x_increment
    index_y = y_increment
    while not (eval(str(seat_x) + op1 + str(index_x) + condition1)
               or eval(str(seat_y) + op2 + str(index_y) + condition2)):
        if seats[eval(str(seat_y) + op2 + str(index_y))][eval(str(seat_x) + op1 + str(index_x))] == '#':
            return True
        elif seats[eval(str(seat_y) + op2 + str(index_y))][eval(str(seat_x) + op1 + str(index_x))] == 'L':
            return False
        index_x += x_increment
        index_y += y_increment
    return False


def occupied_adjacent_seats(seat_x: int, seat_y: int, seats: List[List[str]]) -> int:
    tot = 0
    tot += find_vis(seat_x, seat_y, '-', '-', '< 0', '< 0', 1, 1, seats)  # Upper Left Diagonal
    tot += find_vis(seat_x, seat_y, '+', '-', '& 0', '< 0', 0, 1, seats)  # Up
    tot += find_vis(seat_x, seat_y, '+', '-', '>= len(seats[0])', '< 0', 1, 1, seats)  # Upper Right Diagonal
    tot += find_vis(seat_x, seat_y, '-', '+', '< 0', '& 0', 1, 0, seats)  # Left
    tot += find_vis(seat_x, seat_y, '+', '+', '>= len(seats[0])', '& 0', 1, 0, seats)  # Right
    tot += find_vis(seat_x, seat_y, '-', '+', '< 0', '>= len(seats)', 1, 1, seats)  # Lower Left Diagonal
    tot += find_vis(seat_x, seat_y, '+', '+', '& 0', '>= len(seats)', 0, 1, seats)  # Down
    tot += find_vis(seat_x, seat_y, '+', '+', '>= len(seats[0])', '>= len(seats)', 1, 1, seats)  # Lower Right Diagonal
    return tot


def run_iteration(seats: List[List[str]]) -> List[List[str]]:
    new_seats = deepcopy(seats)
    for x in range(len(seats[0])):
        for y in range(len(seats)):
            if seats[y][x] != '.':
                num_adjacent = occupied_adjacent_seats(x, y, seats)
                if seats[y][x] == 'L':
                    if num_adjacent == 0:
                        new_seats[y][x] = '#'
                else:
                    if num_adjacent >= 5:
                        new_seats[y][x] = 'L'
    return new_seats


def count_occupied_seats(seats: List[List[str]]) -> int:
    count = 0
    for x in range(len(seats[0])):
        for y in range(len(seats)):
            count += (seats[y][x] == '#')
    return count


# This may be the slowest game of life you've ever seen
def run_seat_game(seats: List[List[str]]) -> int:
    print_seats(seats)
    new_seats = run_iteration(seats)
    print_seats(new_seats)
    while new_seats != seats:
        seats = new_seats
        new_seats = run_iteration(seats)
        print_seats(new_seats)
    return count_occupied_seats(new_seats)


with open('input.txt') as f:
    arr = [line.rstrip('\n') for line in f]

arrangement = [[char for char in i] for i in arr]
# print(arrangement[1][0])  # y is vertical
# print(arrangement[0][1])  # x is horizontal, access should be [y][x]
print(run_seat_game(arrangement))
