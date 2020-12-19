from typing import List
from re import compile, fullmatch, search


pattern = compile('[+*](?!((\)[0-9*+]*\()|[0-9*+])*\()')
paren_pattern = compile('\)(([0-9+*]*)|(\)[0-9*+]*\()*)*\(')


# Build an operation tree based on the operators. Thanks CS2103!
class OperatorNode:
    def __init__(self, value: str):
        self.parent = None
        self.value = value

    def evaluate(self) -> int:
        return int(self.value)


class MultiplicationNode(OperatorNode):
    def __init__(self, left: str, right: str):
        super(MultiplicationNode, self).__init__('*')
        self.left = parse_equation(left)
        self.right = parse_equation(right)
        self.left.parent = self
        self.right.parent = self

    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()


class AdditionNode(OperatorNode):
    def __init__(self, left: str, right: str):
        super(AdditionNode, self).__init__('+')
        self.left = parse_equation(left)
        self.right = parse_equation(right)
        self.left.parent = self
        self.right.parent = self

    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()


class Parenthesis(OperatorNode):
    def __init__(self, inner_eq: str):
        super(Parenthesis, self).__init__('()')
        self.inner_eq: OperatorNode = parse_equation(inner_eq)
        self.inner_eq.parent = self

    def evaluate(self) -> int:
        return self.inner_eq.evaluate()


def parse_equation(equation: str) -> OperatorNode:
    if fullmatch(paren_pattern, equation):
        return Parenthesis(equation[1:-1])
    if match := search(pattern, equation):
        operator = match[0]

        if operator[0] == '+':
            return AdditionNode(equation[match.start() + 1:], equation[:match.start()])
        elif operator[0] == '*':
            return MultiplicationNode(equation[match.start() + 1:], equation[:match.start()])
        else:
            print('No')
            exit(12312312)
    else:
        return OperatorNode(equation)


def solve_equation(equation: str) -> int:
    # Work backwards from the string so that evaluation acts left to right
    return parse_equation(equation.replace(' ', '')[::-1]).evaluate()


def sum_eqs(equations: List[str]) -> int:
    count = 0
    for equation in equations:
        count += solve_equation(equation)
    return count


with open('input.txt') as f:
    arr = [line.rstrip('\n') for line in f]

print(sum_eqs(arr))
