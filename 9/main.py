import os


def main() -> None:
    with open('input.txt') as f:
        instructions = [
            int(line)
            for line in f.read().splitlines()
        ]

    solution_part_one = part_1(instructions)
    print(solution_part_one)
    part_2(solution_part_one, instructions)


def part_1(instructions) -> int:
    preamble = 25
    index = 25
    while isValid(instructions, index, preamble) == True:
        index += 1

    return instructions[index]


def isValid(instructions, index, preamble):
    for i in range(index - preamble, index - 1):
        for j in range(i + 1, index):
            if instructions[i] + instructions[j] == instructions[index]:
                return True


def part_2(solution_part_one, instructions) -> int:
    startPoint = 0
    while testTotal(solution_part_one, instructions, startPoint) == True:
        startPoint += 1


def testTotal(solution, instructions, startPoint):
    total = 0
    for i in range(startPoint, len(instructions)):
        total = total + instructions[i]
        if(total > solution):
            break
        elif(total == solution):
            solution_arr = instructions[startPoint:i+1]
            if(len(solution_arr) > 2):
                print(max(solution_arr) + min(solution_arr))
                return False
    return True


if __name__ == "__main__":
    main()
