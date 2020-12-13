import os


def main() -> None:
    with open('input.txt') as f:
        lines = f.read().splitlines()

    print(f'{part_one(lines)}')


def part_one(lines) -> int:
    seat_numbers = []
    for line in lines:
        seat_numbers.append(int(line.replace("F", "0").replace(
            "B", "1").replace("L", "0").replace("R", "1"), 2))

    return (max(seat_numbers))


if __name__ == "__main__":
    main()
