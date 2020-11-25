from math import floor

def fuelNeeded(mass):
    return floor(mass / 3.0) - 2


def fuelNeededRec(mass):
    fuel = floor(mass / 3.0) - 2
    if fuel < 0:
        return 0
    else:
        return fuel + fuelNeededRec(fuel)


if __name__ == '__main__':
    with open('input.txt') as file:
        lines = [int(i) for i in file.read().split('\n')]
    total = 0
    for i in lines:
        total = total + fuelNeeded(i)
    print(total)
    total = 0
    for i in lines:
        total = total + fuelNeededRec(i)
    print(total)
