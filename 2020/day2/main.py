
def valid_password_p1(string):
    string = string.split(' ')
    string[1] = string[1].replace(':', '')
    string[0] = string[0].split('-')
    num_occurrences = 0
    for j in string[2]:
        if j == string[1]:
            num_occurrences += 1
    return int(string[0][0]) <= num_occurrences <= int(string[0][1])


def valid_password(string):
    string = string.split(' ')
    string[1] = string[1].replace(':', '')
    string[0] = string[0].split('-')
    return (string[2][int(string[0][0]) - 1] == string[1]) ^ (string[2][int(string[0][1]) - 1] == string[1])


with open('input.txt') as f:
    arr = [line.rstrip('\n') for line in f]

count = 0
for i in arr:
    count += valid_password_p1(i)
print('Number of valid passwords (Part 1): {}'.format(count))

count = 0
for i in arr:
    count += valid_password(i)
print('Number of valid passwords (Part 2): {}'.format(count))
