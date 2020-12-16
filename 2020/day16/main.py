from typing import List, Dict, Tuple


class Range:
    def __init__(self, lower: int, upper: int):
        self.lower: int = lower
        self.upper: int = upper

    def __lt__(self, other):
        """If the lower bound of the other range is within this range, return True.
        Return False otherwise.
        """
        return self.upper > other.lower > self.lower

    def __gt__(self, other):
        """Return True if the upper bound is within this range, False otherwise.
        """
        return self.upper > other.upper > self.lower

    def __eq__(self, other):
        """Return True if the other range is contained with this range.
        Return False otherwise.
        """
        return self < other and self > other

    def __str__(self):
        return '{}-{}'.format(self.lower, self.upper)

    def __contains__(self, item):
        return self.lower <= item <= self.upper


class Field:
    def __init__(self, field_name: str, range1: str, range2: str):
        self.field_name: str = field_name

        range1 = range1.split('-')
        self.range1: Range = Range(int(range1[0]), int(range1[1]))

        range2 = range2.split('-')
        self.range2: Range = Range(int(range2[0]), int(range2[1]))

    def __str__(self):
        return '{}: {} or {}'.format(self.field_name, self.range1, self.range2)


def add_range(this_range: Range, list_of_ranges: List[Range]):
    i = 0
    while i < len(list_of_ranges):
        # This range is contained in another, get rid of this range
        if list_of_ranges[i] == this_range:
            return

        # Another range is contained in this one, get rid of that range
        elif this_range == list_of_ranges[i]:
            list_of_ranges.pop(i)

        # The lower bound of another range is contained in this one, update our range and remove the other
        elif this_range < list_of_ranges[i]:
            this_range = Range(this_range.lower, list_of_ranges[i].upper)
            list_of_ranges.pop(i)

        # The upper bound of another range is contained in this one, update our range and remove the other
        elif this_range > list_of_ranges[i]:
            this_range = Range(list_of_ranges[i].lower, this_range.upper)
            list_of_ranges.pop(i)
        else:
            i += 1
    list_of_ranges.append(this_range)


def read_rules(rule_set: List[str]) -> Tuple[Dict[str, Field], List[Range]]:
    rule_dict = {}
    range_list = []

    for rule in rule_set:
        field_name, ranges = rule.split(': ')
        range1, range2 = ranges.split(' or ')

        field = Field(field_name, range1, range2)
        rule_dict[field_name] = field

        add_range(field.range1, range_list)
        add_range(field.range2, range_list)
    return rule_dict, range_list


def in_range_list(value: int, range_list: List[Range]) -> bool:
    for r in range_list:
        if value in r:
            return True
    return False


def find_invalid_entries(ticket_list: List[str], range_list: List[Range]) -> int:
    count = 0
    for ticket in ticket_list:
        ticket = [int(t) for t in ticket.split(',')]

        for t in ticket:
            if not in_range_list(t, range_list):
                count += t
    return count


with open('input.txt') as f:
    rules, my_ticket, tickets = f.read().split('\n\n')

rules = [line.rstrip('\n') for line in rules.split('\n')]
my_ticket = [line.rstrip('\n') for line in my_ticket.split('\n')][1]
tickets = [line.rstrip('\n') for line in tickets.split('\n')][1:]

d_o_f, l_o_r = read_rules(rules)
print(find_invalid_entries(tickets, l_o_r))
