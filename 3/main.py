import os


def main() -> None:
    with open('input.txt') as f:
        lines = f.read().splitlines()

    print(f'{part_one(lines, 3)}')
    print(f'{part_one(lines, 1) * part_one(lines, 3) * part_one(lines, 5) * part_one(lines, 7) * part_two(lines, 1)}')


def part_one(lines, right) -> int:
    current_index = 0
    total = 0

    for line in lines:
        if line[current_index] == "#":
            total = total + 1
        current_index = current_index + right
        if current_index >= len(line):
            current_index = current_index - len(line)

    return total


def part_two(lines, right) -> int:
    current_index = 0
    total = 0
    vline = 0
    for line in lines:
        vline += 1
        if (vline % 2):
            if line[current_index] == "#":
                total = total + 1
            current_index = current_index + right
            if current_index >= len(line):
                current_index = current_index - len(line)

    return total


if __name__ == "__main__":
    main()
