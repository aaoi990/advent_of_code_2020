import os


def main() -> None:
    with open('input.txt') as f:
        instructions = [
            line
            for line in f.read().splitlines()
        ]
    print(part_1(instructions))


def part_1(instructions) -> int:
    read = []
    acc = 0
    i = 0
    while i not in read:
        read.append(i)
        order = instructions[i].split(" ")
        if order[0] == "acc":
            i += 1
            acc = acc + int(order[1])
        if order[0] == "jmp":
            i += int(order[1])
        if order[0] == "nop":
            i += 1

    return acc


def part_2(numbers) -> int:
    pass


if __name__ == "__main__":
    main()
