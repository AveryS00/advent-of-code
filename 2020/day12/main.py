from typing import List

directions = ('N', 'E', 'S', 'W')


class Ferry:
    def __init__(self):
        self.direction: str = 'E'
        self.x: int = 0
        self.y: int = 0

    def __str__(self):
        return 'Ferry: {}: {},{}'.format(self.direction, self.x, self.y)

    def N(self, value):
        self.y += value

    def S(self, value):
        self.y -= value

    def W(self, value):
        self.x -= value

    def E(self, value):
        self.x += value

    def F(self, value):
        getattr(Ferry, self.direction)(self, value)

    def L(self, value):
        value //= 90
        index = directions.index(self.direction)
        for i in range(value):
            index = (index - 1) % 4
        self.direction = directions[index]

    def R(self, value):
        value //= 90
        index = directions.index(self.direction)
        for i in range(value):
            index = (index + 1) % 4
        self.direction = directions[index]

    def manhattan_distance_origin(self) -> int:
        return abs(self.x) + abs(self.y)


class WaypointFerry(Ferry):
    def __init__(self):
        super().__init__()
        self.waypoint_x = 10
        self.waypoint_y = 1

    def __str__(self):
        return 'Ferry: {}, {} | Waypoint: {}, {}'.format(self.x, self.y, self.waypoint_x, self.waypoint_y)

    def N(self, value):
        self.waypoint_y += value

    def S(self, value):
        self.waypoint_y -= value

    def W(self, value):
        self.waypoint_x -= value

    def E(self, value):
        self.waypoint_x += value

    def F(self, value):
        self.x += self.waypoint_x * value
        self.y += self.waypoint_y * value

    # Left rotation matrix [0, -1]   [x]
    #                      [1,  0] * [y]
    def L(self, value):
        value //= 90
        for i in range(value):
            temp_x = self.waypoint_x
            self.waypoint_x = - self.waypoint_y
            self.waypoint_y = temp_x

    # Right rotation matrix [ 0, 1]
    #                       [-1, 0]
    def R(self, value):
        value //= 90
        for i in range(value):
            temp_x = self.waypoint_x
            self.waypoint_x = self.waypoint_y
            self.waypoint_y = - temp_x


def drive_ferry(direction_list: List[str]) -> int:
    ferry = Ferry()
    for direction in direction_list:
        getattr(Ferry, direction[0])(ferry, int(direction[1:]))
    return ferry.manhattan_distance_origin()


def drive_waypoint_ferry(direction_list: List[str]) -> int:
    ferry = WaypointFerry()
    for direction in direction_list:
        getattr(WaypointFerry, direction[0])(ferry, int(direction[1:]))
    return ferry.manhattan_distance_origin()


with open('input.txt') as f:
    arr = [line.rstrip('\n') for line in f]

print(drive_ferry(arr))
print(drive_waypoint_ferry(arr))
