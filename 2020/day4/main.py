import re

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


def valid_year(year, length, min_year, max_year):
    return len(year) == length and min_year <= int(year) <= max_year


class Validation:
    def v_byr(self, year):
        return valid_year(year, 4, 1920, 2002)

    def v_iyr(self, year):
        return valid_year(year, 4, 2010, 2020)

    def v_eyr(self, year):
        return valid_year(year, 4, 2020, 2030)

    def v_hgt(self, height):
        if 'in' in height:
            return 59 <= int(height[:-2]) <= 76
        if 'cm' in height:
            return 150 <= int(height[:-2]) <= 193
        return False

    def v_hcl(self, color):
        if color[0] != '#':
            return False
        return re.search('[a-f0-9]{6}', color) is not None

    def v_ecl(self, color):
        valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return color in valid_colors

    def v_pid(self, pid):
        return len(pid) == 9 and re.match('[0-9]', pid) is not None

    def v_cid(self, cid):
        return True


# Take in a string of a passport and turn it into a dictionary object IF AND ONLY IF it is valid.
# If it is invalid, return None. The string should just be one line which contains the field:value
# pairs separated by spaces
def read_passport(passport):
    validation = Validation()
    new_ppt = {}
    passport = [field.split(':') for field in passport.split(' ')]
    for i in passport:
        is_valid = getattr(validation, 'v_%s' % i[0])(i[1])
        if is_valid:
            new_ppt[i[0]] = i[1]
    if len(new_ppt) == len(fields):
        return new_ppt
    elif len(new_ppt) == len(fields) - 1 and 'cid' not in new_ppt:
        return new_ppt
    return None


with open('input.txt') as f:
    arr = [line.replace('\n', ' ') for line in f.read().split('\n\n')]

count = 0
for item in arr:
    count += read_passport(item) is not None
print(count)
