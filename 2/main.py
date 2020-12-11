import os


def main() -> None:
    with open('input.txt') as f:
        lines = f.read().splitlines()

    suitable = 0
    for line in lines:
        extracted = line.replace('-', ' ').replace(':', '').split(' ')
        letter_count = extracted[3].count(extracted[2])
        if letter_count >= int(extracted[0]) and letter_count <= int(extracted[1]):
            suitable += 1

    print(f'{suitable}')


if __name__ == "__main__":
    main()
