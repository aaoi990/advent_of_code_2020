import os


def main() -> None:
    with open('input.txt') as f:
        lines = f.read().splitlines()

    seat_numbers = part_one(lines)
    print(f'{part_two(seat_numbers)}')


def part_one(lines) -> list:
    seat_numbers = []
    for line in lines:
        seat_numbers.append(int(line.replace("F", "0").replace(
            "B", "1").replace("L", "0").replace("R", "1"), 2))

    return seat_numbers


def part_two(lines) -> int:
    missing = 0
    for line in lines:
        if line + 1 not in lines:
            missing = line

    return missing + 1


if __name__ == "__main__":
    main()
