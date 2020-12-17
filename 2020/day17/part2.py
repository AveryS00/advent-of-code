from __future__ import annotations

from typing import List, Dict, Tuple
from copy import deepcopy


class HyperCube:
    def __init__(self, coord: Tuple[int, int, int, int], active: bool):
        self.coordinate: Tuple[int, int, int, int] = coord
        self.active: bool = active
        self.neighbors: List[Tuple[int, int, int, int]] = []
        for x in range(coord[0] - 1, coord[0] + 2):
            for y in range(coord[1] - 1, coord[1] + 2):
                for z in range(coord[2] - 1, coord[2] + 2):
                    for w in range(coord[3] - 1, coord[3] + 2):
                        if (x, y, z, w) != coord:
                            self.neighbors.append((x, y, z, w))

    def determine_next_state(self, board: Dict[Tuple[int, int, int, int], HyperCube]) -> bool:
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


def print_board(board: Dict[Tuple[int, int, int, int], HyperCube]):
    coord_list = list(board.keys())
    x_min = min(map(lambda coord: coord[0], coord_list))
    x_max = max(map(lambda coord: coord[0], coord_list))
    y_min = min(map(lambda coord: coord[1], coord_list))
    y_max = max(map(lambda coord: coord[1], coord_list))
    z_min = min(map(lambda coord: coord[2], coord_list))
    z_max = max(map(lambda coord: coord[2], coord_list))
    w_min = min(map(lambda coord: coord[3], coord_list))
    w_max = max(map(lambda coord: coord[3], coord_list))
    for w in range(w_min, w_max + 1):
        for z in range(z_min, z_max + 1):
            print('z = {}, w = {}'.format(z, w))
            for y in range(y_min, y_max + 1):
                for x in range(x_min, x_max + 1):
                    if (x, y, z, w) in board:
                        print(board[(x, y, z, w)], end='')
                    else:
                        print('.', end='')
                print()
            print()
        print()


def count_active(board: Dict[Tuple[int, int, int, int], HyperCube]) -> int:
    count = 0
    for cube in board.values():
        count += cube.active
    return count


def play_game(board: Dict[Tuple[int, int, int, int], HyperCube], iterations: int) -> int:
    current_iter = 0
    while current_iter < iterations:
        print(25*'~')
        print('Cycle: {}'.format(current_iter))
        print_board(board)

        next_board = deepcopy(board)
        for coord, cube in board.items():
            next_board[coord].active = cube.determine_next_state(board)
            if next_board[coord].active:
                initialize_empty_adjacent(next_board[coord], next_board)

        board = next_board
        current_iter += 1
    return count_active(board)


def initialize_empty_adjacent(cube: HyperCube, board: Dict[Tuple[int, int, int, int]]):
    for coord in cube.neighbors:
        if coord not in board:
            board[coord] = HyperCube(coord, False)


def convert_input_to_board(initial: List[str]) -> Dict[Tuple[int, int, int, int], HyperCube]:
    board: Dict[Tuple[int, int, int, int], HyperCube] = {}

    for y in range(len(initial)):
        for x in range(len(initial[0])):
            active = initial[y][x] == '#'
            current_coord = (x, y, 0, 0)
            board[current_coord] = HyperCube(current_coord, active)

            if active:
                initialize_empty_adjacent(board[current_coord], board)
    return board


with open('input.txt') as f:
    arr = [line.rstrip('\n') for line in f]

print(play_game(convert_input_to_board(arr), 6))
