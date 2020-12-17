from __future__ import annotations

from typing import Tuple, Dict, List
from copy import deepcopy


class Cube:
    def __init__(self, coord: Tuple[int, int, int], active: bool):
        x, y, z = coord
        self.coordinate: Tuple[int, int, int] = coord
        self.active: bool = active
        self.neighbors: List[Tuple[int, int, int]] = [
            # Level below
            (x - 1, y - 1, z - 1),
            (x, y - 1, z - 1),
            (x + 1, y - 1, z - 1),
            (x - 1, y, z - 1),
            (x, y, z - 1),
            (x + 1, y, z - 1),
            (x - 1, y + 1, z - 1),
            (x, y + 1, z - 1),
            (x + 1, y + 1, z - 1),

            # Current level
            (x + 1, y + 1, z),
            (x - 1, y - 1, z),
            (x, y - 1, z),
            (x + 1, y - 1, z),
            (x - 1, y, z),
            (x + 1, y, z),
            (x - 1, y + 1, z),
            (x, y + 1, z),

            # Level above
            (x - 1, y - 1, z + 1),
            (x, y - 1, z + 1),
            (x + 1, y - 1, z + 1),
            (x - 1, y, z + 1),
            (x, y, z + 1),
            (x + 1, y, z + 1),
            (x - 1, y + 1, z + 1),
            (x, y + 1, z + 1),
            (x + 1, y + 1, z + 1)
        ]

    def determine_next_state(self, board: Dict[Tuple[int, int, int], Cube]) -> bool:
        num_active_neighbors = 0
        for coord in self.neighbors:
            if coord in board:
                num_active_neighbors += board[coord].active

        if self.active:
            if num_active_neighbors == 2 or num_active_neighbors == 3:
                return self.active
            else:
                return not self.active
        else:
            if num_active_neighbors == 3:
                return not self.active
            else:
                return self.active

    def __str__(self):
        if self.active:
            return '#'
        else:
            return '.'


def print_board(board: Dict[Tuple[int, int, int], Cube]):
    coord_list = list(board.keys())
    x_min = min(map(lambda coord: coord[0], coord_list))
    x_max = max(map(lambda coord: coord[0], coord_list))
    y_min = min(map(lambda coord: coord[1], coord_list))
    y_max = max(map(lambda coord: coord[1], coord_list))
    z_min = min(map(lambda coord: coord[2], coord_list))
    z_max = max(map(lambda coord: coord[2], coord_list))
    for z in range(z_min, z_max + 1):
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                if (x, y, z) in board:
                    print(board[(x, y, z)], end='')
                else:
                    print('.', end='')
            print()
        print()


def count_active(board: Dict[Tuple[int, int, int], Cube]) -> int:
    count = 0
    for cube in board.values():
        count += cube.active
    return count


def play_game(board: Dict[Tuple[int, int, int], Cube], iterations: int) -> int:
    current_iter = 0
    while current_iter < iterations:
        print(current_iter)
        print_board(board)

        next_board = deepcopy(board)
        for coord, cube in board.items():
            next_board[coord].active = cube.determine_next_state(board)
            if next_board[coord].active:
                initialize_empty_adjacent(next_board[coord], next_board)

        board = next_board
        current_iter += 1
    return count_active(board)


def initialize_empty_adjacent(cube: Cube, board: Dict[Tuple[int, int, int]]):
    for coord in cube.neighbors:
        if coord not in board:
            board[coord] = Cube(coord, False)


def convert_input_to_board(initial: List[str]) -> Dict[Tuple[int, int, int], Cube]:
    board: Dict[Tuple[int, int, int], Cube] = {}

    for y in range(len(initial)):
        for x in range(len(initial[0])):
            active = initial[y][x] == '#'
            current_coord = (x, y, 0)
            board[current_coord] = Cube(current_coord, active)

            if active:
                initialize_empty_adjacent(board[current_coord], board)
    return board


with open('input.txt') as f:
    arr = [line.rstrip('\n') for line in f]

print(play_game(convert_input_to_board(arr), 6))
