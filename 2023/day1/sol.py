from typing import Union


def parse_line(line: str) -> int:
    first: Union[int, None] = None
    last: Union[int, None] = None
    for c in line:
        try:
            val: int = int(c)
        except ValueError:
            continue
        if first is None:
            first = val
        last = val
    return first * 10 + last


values: list[int] = []

with open('input.txt', 'r') as f:
    for line in f:
        values.append(parse_line(line))

print(sum(values))
