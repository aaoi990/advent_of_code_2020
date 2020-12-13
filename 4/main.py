import os
import re


def main() -> None:
    passports = []
    with open('input.txt', 'r') as file:
        lines = file.read().split('\n\n')

        for line in lines:
            passports.append(line.replace('\n', ' ').split(' '))

    valid = part_one(passports)
    print(f'{len(part_two(valid))}')


def part_one(lines) -> list:
    valid = []
    for passport in lines:
        if(len(passport) == 8):
            valid.append(passport)
        elif (len(passport) == 7):
            if all('cid' not in s for s in passport):
                valid.append(passport)

    return valid


def part_two(lines) -> int:
    valid_passports = []
    for line in lines:
        valid = 0
        for field in line:
            info = field.split(":")
            if info[0] == "hgt":
                if('cm' in info[1] and (int(info[1].split('cm', 1)[0]) >= 150 and int(info[1].split('cm', 1)[0]) <= 193)):
                    valid += 1
                elif('in' in info[1] and (int(info[1].split('in', 1)[0]) >= 59 and int(info[1].split('in', 1)[0]) <= 76)):
                    valid += 1
            if info[0] == "iyr":
                if int(info[1]) >= 2010 and int(info[1]) <= 2020:
                    valid += 1
            if info[0] == "eyr":
                if int(info[1]) >= 2020 and int(info[1]) <= 2030:
                    valid += 1
            if info[0] == "byr":
                if int(info[1]) >= 1920 and int(info[1]) <= 2002:
                    valid += 1
            if info[0] == "hcl":
                if(re.search("^#[0-9a-f]{6}", info[1])):
                    valid += 1
            if info[0] == "ecl":
                if info[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    valid += 1
            if info[0] == "pid":
                if len(info[1]) == 9:
                    valid += 1

        if(valid == 7):
            valid_passports.append(line)

    print(valid_passports)
    return valid_passports


if __name__ == "__main__":
    main()
