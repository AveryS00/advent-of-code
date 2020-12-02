# Sloppy but quick to type

"""
def valid_password(string):
    string = string.split(' ')
    string[1] = string[1].replace(':', '')
    string[0] = string[0].split('-')
    num_occurrences = 0
    for j in string[2]:
        if j == string[1]:
            num_occurrences += 1
    if int(string[0][0]) <= num_occurrences <= int(string[0][1]):
        return True
"""


def valid_password(string):
    string = string.split(' ')
    string[1] = string[1].replace(':', '')
    string[0] = string[0].split('-')
    if string[2][int(string[0][0]) - 1] == string[1]:
        if string[2][int(string[0][1]) - 1] == string[1]:
            return False
        return True
    elif string[2][int(string[0][1]) - 1] == string[1]:
        return True
    return False


with open('input.txt') as f:
    arr = f.readlines()
    count = 0
    for i in arr:
        if valid_password(i):
            count += 1
    print('Number of valid passwords: ' + str(count))
