import os
from collections import Counter


def main() -> None:
    customs_list = []
    with open('input.txt', 'r') as file:
        lines = file.read().split('\n\n')

        for line in lines:
            customs_list.append(line.replace('\n', ' ').split(' '))

    print(f'{part_one(customs_list)}')
    print(f'{part_two(customs_list)}')


def part_one(lines) -> int:
    total = []

    for group in lines:
        unique_ques = []
        for ques in group:
            unique_ques.extend([uq for uq in ques])
        total.extend(list(set(unique_ques)))

    return len(total)


def part_two(lines) -> int:
    total = 0
    for group in lines:
        group_size = len(group)
        counts = Counter("".join(group))
        counts = Counter(list(counts.values()))[group_size]
        total += counts

    return total


if __name__ == "__main__":
    main()
