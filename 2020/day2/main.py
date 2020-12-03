from re import sub


def valid_password_p1(lower_bound, upper_bound, char, password):
    num_occurrences = 0
    for j in password:
        num_occurrences += (j == char)
    return lower_bound <= num_occurrences <= upper_bound


def valid_password(first_index, second_index, char, password):
    return (password[int(first_index) - 1] == char) ^ (password[int(second_index) - 1] == char)


with open('input.txt') as f:
    arr = [sub('[:\n]', '', line).split(' ') for line in f]

count = 0
for i in arr:
    bounds = i[0].split('-')
    count += valid_password_p1(int(bounds[0]), int(bounds[1]), i[1], i[2])
print('Number of valid passwords (Part 1): {}'.format(count))

count = 0
for i in arr:
    bounds = i[0].split('-')
    count += valid_password(int(bounds[0]), int(bounds[1]), i[1], i[2])
print('Number of valid passwords (Part 2): {}'.format(count))
