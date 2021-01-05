import os


def main() -> None:
    with open('input.txt') as f:
        instructions = [
            int(line)
            for line in f.read().splitlines()
        ]
    print(part_1(instructions))


def part_1(instructions) -> int:
    preamble = 25
    index = 25
    while isValid(instructions, index, preamble) == True:
        index += 1

    return instructions[index]


def isValid(instructions, index, preamble):
    for i in range(index - preamble, index - 1):
        for j in range(i + 1, index):
            if instructions[i] + instructions[j] == instructions[index]:
                return True


def part_2(numbers) -> int:
    pass


if __name__ == "__main__":
    main()
