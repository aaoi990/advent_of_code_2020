import os


def main() -> None:
    with open('input.txt') as f:
        lines = f.read().splitlines()

    processed_file = process_file(lines)
    check_passwords(processed_file)


def process_file(file):
    refactored = []
    for line in file:
        refactored.append(line.replace('-', ' ').replace(':', '').split(' '))

    return refactored


def check_passwords(passwords):
    suitable_passwords = 0
    for password in passwords:
        letter_count = password[3].count(password[2])
        if letter_count >= int(password[0]) and letter_count <= int(password[1]):
            suitable_passwords += 1

    print(f'{suitable_passwords}')


if __name__ == "__main__":
    main()
