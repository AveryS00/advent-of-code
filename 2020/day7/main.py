from typing import Dict, List
import re


class Luggage:
    def __init__(self, color: str, bags: Dict[str, int]):
        """
        :param color: A string of the color
        :param bags: A dictionary of sub-bags where key:val is bag:quantity
        """
        self.color: str = color
        self.bags: Dict[str, int] = bags

    def __eq__(self, other):
        if isinstance(other, Luggage):
            return self.color == other.color
        return False

    def __str__(self):
        return self.color


def process_sub_rule(rule: str) -> Dict[str, int]:
    """

    :param rule:
    :return:
    """
    bags = {}
    if rule == 'no other bags.':
        pass
    elif ',' in rule:
        rule = re.sub('( bag)s*\.*', '', rule)
        rule = rule.split(', ')
        for r in rule:
            quantity = re.match('[0-9]+', r)
            r = re.sub('[0-9]+ ', '', r)
            bags[r] = int(quantity[0])
    else:
        rule = re.sub('( bag)s*\.*', '', rule)
        quantity = re.match('[0-9]+', rule)
        rule = re.sub('[0-9]+ ', '', rule)
        bags[rule] = int(quantity[0])
    return bags


def read_rule(rule: str) -> Luggage:
    """Read the rule from the string and return a Luggage object representing the rule

    :param rule: The rule
    :return: Luggage object with the color and sub-bags
    """
    color, sub_bag_rule = rule.split(' bags contain ')
    sub_bags = process_sub_rule(sub_bag_rule)
    return Luggage(color, sub_bags)


def generate_bag_dict(rules: List[str]) -> Dict[str, Luggage]:
    """

    :param rules:
    :return:
    """
    bags = {}
    for rule in rules:
        bag = read_rule(rule)
        bags[bag.color] = bag
    return bags


def contains_color(bag: Luggage, bag_list: Dict[str, Luggage], color: str) -> bool:
    """

    :param bag:
    :param bag_list:
    :param color:
    :return:
    """
    # Ignore this bag if it's the one we're searching for, has to be contained in at least one bag
    if bag.color == color:
        return False

    # Do BFS on the bags
    seen: List[str] = [bag.color]
    queue: List[bag] = [bag]
    while len(queue) != 0:
        bag = queue.pop(0)
        if bag.color == color:
            return True
        for s_bag_color, s_bag_quantity in bag.bags.items():
            if s_bag_color not in seen:
                queue.append(bag_list[s_bag_color])
                seen.append(s_bag_color)
    return False


def count_sub_bags(bag: Luggage, bag_list: Dict[str, Luggage]) -> int:
    num = 0
    for sub_bag, quantity in bag.bags.items():
        num += quantity * (count_sub_bags(bag_list[sub_bag], bag_list) + 1)
    return num


def sum_of_quantities(bag: Luggage):
    sum = 0
    for color, quantity in bag.bags.items():
        sum += quantity
    return sum


with open('input.txt') as f:
    list_of_rules = [line.rstrip('\n') for line in f]

all_bags = generate_bag_dict(list_of_rules)

count = 0
for c, b in all_bags.items():
    if contains_color(b, all_bags, 'shiny gold'):
        count += 1
print(count)

print(count_sub_bags(all_bags['shiny gold'], all_bags))

