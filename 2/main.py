import os


def main() -> None:
    with open('input.txt') as f:
        lines = f.read().splitlines()

    print(f'{part_one(lines)}')
    print(f'{part_two(lines)}')


def part_one(lines):
    suitable = 0
    for line in lines:
        extracted = line.replace('-', ' ').replace(':', '').split(' ')
        letter_count = extracted[3].count(extracted[2])
        if letter_count >= int(extracted[0]) and letter_count <= int(extracted[1]):
            suitable += 1

    return suitable


def part_two(lines):
    suitable = 0
    for line in lines:
        extracted = line.replace('-', ' ').replace(':', '').split(' ')
        if((extracted[3][int(extracted[0]) - 1] == extracted[2])
                is not (extracted[3][int(extracted[1]) - 1] == extracted[2])):
            suitable += 1

    return suitable


if __name__ == "__main__":
    main()
