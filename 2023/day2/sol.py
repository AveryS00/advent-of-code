
colors: dict[str, int] = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def check(r: str) -> bool:
    groups = r.split(',')
    for g in groups:
        g = g.strip()
        num, col = g.split(' ')
        num = int(num)
        if num > colors[col]:
            return False
    return True


count = 0
with open('input.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        line = line.lstrip('Game ')
        game_num, rounds = line.split(':')
        game_num = int(game_num)
        print(game_num)
        rounds = rounds.split(';')
        if all([check(r) for r in rounds]):
            print('Valid round')
            count += game_num
        else:
            print('Invalid round')

print(count)
