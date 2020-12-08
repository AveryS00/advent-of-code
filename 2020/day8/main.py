from typing import List, NoReturn


class GameCode:
    def __init__(self, instruction_set: List[str]):
        self.accumulator: int = 0
        self.instruction_pointer: int = 0
        self.instruction_set: List[str] = instruction_set

    def acc(self, val: int) -> NoReturn:
        self.accumulator += val
        self.instruction_pointer += 1

    def jmp(self, offset: int) -> NoReturn:
        self.instruction_pointer += offset

    def nop(self, val: int) -> NoReturn:
        self.instruction_pointer += 1

    def run(self) -> int:
        """Run one instruction and return the current accumulator value
        :return: The current accumulator value
        """
        instruction = self.instruction_set[self.instruction_pointer]
        operation, value = instruction.split(' ')
        getattr(GameCode, operation)(self, int(value))  # Call the appropriate operation
        return self.accumulator

    def run_all(self) -> int:
        """Continue to run all instructions and return the accumulator value. Will not stop if a loop occurs
        :return: The resultant accumulator value
        """
        while self.instruction_pointer != len(self.instruction_set):
            self.run()
        return self.accumulator


def contains_loop(instructions: List[str]) -> bool:
    seen = set()
    code = GameCode(instructions)
    while code.instruction_pointer not in seen:
        if code.instruction_pointer == len(instructions):
            return False
        seen.add(code.instruction_pointer)
        code.run()
    return True


def accumulator_val_loop(instructions: List[str]) -> int:
    seen = set()
    code = GameCode(instructions)
    while code.instruction_pointer not in seen:
        seen.add(code.instruction_pointer)
        code.run()
    return code.accumulator


def try_swap(instructions_copy, index, orig_op, swap_op):
    instructions_copy[index] = instructions_copy[index].replace(orig_op, swap_op)
    if not contains_loop(instructions_copy):
        g_code = GameCode(instructions_copy)
        return g_code.run_all()
    return None


with open('input.txt') as f:
    arr = [line.rstrip('\n') for line in f]

print(accumulator_val_loop(arr))

fixed_output = 0
for i in range(len(arr)):
    if 'jmp' in arr[i]:
        result = try_swap(arr.copy(), i, 'jmp', 'nop')
        if result is not None:
            fixed_output = result
            break
    if 'nop' in arr[i]:
        result = try_swap(arr.copy(), i, 'nop', 'jmp')
        if result is not None:
            fixed_output = result
            break
print(fixed_output)
