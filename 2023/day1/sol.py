import re
from typing import Union


conversions: dict[str, int] = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
p = re.compile(r'(one|two|three|four|five|six|seven|eight|nine|[1-9])')
p_rev = re.compile(r'(?s:.*)(one|two|three|four|five|six|seven|eight|nine|[1-9])')


def parse_line(line: str) -> int:
    print(line, end='')
    m = p.search(line)
    try:
        first: int = int(m.group(1))
    except ValueError:
        first = conversions[m.group(1)]
    print(first)
    m = p_rev.search(line)
    try:
        last: int = int(m.group(1))
    except ValueError:
        last = conversions[m.group(1)]
    print(last)

    return first * 10 + last


values: list[int] = []

with open('input.txt', 'r') as f:
    for line in f:
        values.append(parse_line(line))

print(values)
print(sum(values))
