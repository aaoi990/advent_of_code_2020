import os


def main() -> None:
    with open('input.txt') as f:
        numbers = [
            int(line)
            for line in f.read().splitlines()
        ]

    print(f'Results 1 {part_1(numbers)}')
    print(f'Results 2 {part_2(numbers)}')


def part_1(numbers) -> int:
    for a in numbers:
        for b in numbers:
            if(a + b == 2020):
                return a * b


def part_2(numbers) -> int:
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if(a + b + c == 2020):
                    return a * b * c


if __name__ == "__main__":
    main()
