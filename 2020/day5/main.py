from math import floor

num_cols = 8
num_rows = 128


def bin_search(upper_bound, search, lower_char, upper_char):
    lower_bound = 0
    for half in search:
        middle = floor((upper_bound + lower_bound) / 2)
        if half == lower_char:
            upper_bound = middle
        elif half == upper_char:
            lower_bound = middle + 1
    return lower_bound


def get_id(seat):
    row = bin_search(num_rows - 1, seat[:7], 'F', 'B')
    col = bin_search(num_cols - 1, seat[-3:], 'L', 'R')
    return row * num_cols + col


with open('input.txt') as f:
    arr = [line.rstrip('\n') for line in f]


min_id = 1000
max_id = 0
for i in arr:
    new_id = get_id(i)
    if new_id > max_id:
        max_id = new_id
    if new_id < min_id:
        min_id = new_id

seat_list = [*range(min_id, max_id + 1)]
for i in arr:
    seat_id = get_id(i)
    del seat_list[seat_list.index(seat_id)]
print(seat_list)
