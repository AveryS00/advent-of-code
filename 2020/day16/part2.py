import main
from typing import List, Tuple, Dict
from re import match


def get_departure_values(my_tick: List[int], positions: Dict[str, int]) -> int:
    count = 1
    for key, val in positions.items():
        if match('departure', key):
            count *= my_tick[val]
    return count


def pigeonhole_fields(fields: Dict[str, List[int]]) -> Dict[str, int]:
    keys = sorted(fields, key=lambda key: len(fields[key]))  # Sort the keys by the length of the value
    new_dict = {}

    for i in range(len(keys)):
        if len(fields[keys[i]]) == 1:
            new_dict[keys[i]] = fields[keys[i]][0]

            for field_name in keys[i+1:]:
                fields[field_name].remove(new_dict[keys[i]])
        else:
            print('Hi dumb programmer you made a mistake somewhere else')
            exit(1)

    return new_dict


def determine_fields(ticket_list: List[Tuple[int]], field_dict: Dict[str, main.Field]) -> Dict[str, int]:
    new_fields_dict = {}
    for key in field_dict.keys():
        new_fields_dict[key] = list(range(len(field_dict)))

    for ticket in ticket_list:
        for i in range(len(ticket)):
            for field_name, field in field_dict.items():
                if ticket[i] not in field.range1 and ticket[i] not in field.range2:
                    new_fields_dict[field_name].remove(i)

    return pigeonhole_fields(new_fields_dict)


def valid_ticket(ticket, range_list):
    for t in ticket:
        if not main.in_range_list(t, range_list):
            return False
    return True


def discard_tickets(ticket_list: List[str], range_list: List[main.Range]) -> List[Tuple[int]]:
    new_ticket_list: List[Tuple[int]] = []

    for ticket in ticket_list:
        ticket = [int(t) for t in ticket.split(',')]

        if valid_ticket(ticket, range_list):
            new_ticket_list.append(tuple(ticket))

    return new_ticket_list


with open('input.txt') as f:
    rules, my_ticket, tickets = f.read().split('\n\n')

rules = [line.rstrip('\n') for line in rules.split('\n')]
my_ticket = [line.rstrip('\n') for line in my_ticket.split('\n')][1]
my_ticket = [int(value) for value in my_ticket.split(',')]
tickets = [line.rstrip('\n') for line in tickets.split('\n')][1:]

d_o_f, l_o_r = main.read_rules(rules)
field_pos = determine_fields(discard_tickets(tickets, l_o_r), d_o_f)

print(get_departure_values(my_ticket, field_pos))
