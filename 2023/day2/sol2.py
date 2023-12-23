

def add_group(g: str) -> int:
    rounds = [r.strip() for r in g.split(';')]
    max_g = 0
    max_r = 0
    max_b = 0

    for r in rounds:
        colors = r.split(', ')
        for c in colors:
            count, col = c.split(' ')
            count = int(count)

            if col == 'green':
                if max_g < count:
                    max_g = count
            if col == 'red':
                if max_r < count:
                    max_r = count
            if col == 'blue':
                if max_b < count:
                    max_b = count
    return max_g * max_r * max_b


count = 0
with open('input.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        line = line.lstrip('Game ')
        game_num, rounds = line.split(':')
        game_num = int(game_num)
        print(game_num)
        count += add_group(rounds)

print(count)
