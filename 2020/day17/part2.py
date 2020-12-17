from __future__ import annotations

from typing import List, Dict, Tuple


class HyperCube:
    def __init__(self, coord: Tuple[int, int, int, int], active: bool):
        self.coordinate: Tuple[int, int, int, int] = coord
        self.active: bool = active
        self.neighbors: List[Tuple[int, int, int, int]] = []
        for x in range(coord[0] - 1, coord[0] + 2):
            for y in range(coord[1] - 1, coord[1] + 2):
                for z in range(coord[1] - 1, coord[1] + 2):
                    for w in range(coord[1] - 1, coord[1] + 2):
                        self.neighbors.append((x, y, z, w))

    def determine_next_state(self, board: Dict[Tuple[int, int, int], HyperCube]) -> bool:
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


