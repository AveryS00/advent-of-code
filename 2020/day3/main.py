from math import ceil


def num_trees(delta_x, delta_y, tree_map):
    width = len(tree_map[0])
    depth = len(tree_map)
    full_map = [ceil(delta_x * depth / delta_y / width) * line for line in tree_map]

    x_pos = 0
    y_pos = 0
    count = 0
    while y_pos < depth:
        count += (full_map[y_pos][x_pos] == '#')
        x_pos += delta_x
        y_pos += delta_y
    return count


with open('input.txt') as f:
    arr = [line.rstrip('\n') for line in f]

deltas = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = 1
for x, y in deltas:
    total *= num_trees(x, y, arr)

print(total)
