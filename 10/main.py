import os


def main() -> None:
    adapters = [int(adapter.strip()) for adapter in open("input.txt", 'r')]

    part_1(adapters)
    part_2(adapters)


def part_1(adapters) -> int:
    initial_jolts, diff_one, diff_three = 0, 0, 0
    max_adapters = max(adapters)
    while initial_jolts <= max_adapters:
        potential_adapters = [x for x in adapters if x >
                              initial_jolts and x <= initial_jolts+3]
        if not potential_adapters:
            print(diff_one * (diff_three + 1))
            break
        initial_jolts, diff_one, diff_three = next_adapter(
            potential_adapters, initial_jolts, diff_one, diff_three)


def next_adapter(adapters, initial_jolts, diff_one, diff_three):
    next_minimum = min(adapters)
    if (abs(initial_jolts - next_minimum) == 1):
        diff_one += 1
    elif (abs(initial_jolts - next_minimum) == 3):
        diff_three += 1
    return next_minimum, diff_one, diff_three


def part_2(adapters) -> int:
    adapters.append(max(adapters) + 3)
    sol = {0: 1}
    for adapter in sorted(adapters):
        sol[adapter] = 0

        print(sol)
        if adapter - 1 in sol:
            sol[adapter] += sol[adapter-1]
        if adapter - 2 in sol:
            sol[adapter] += sol[adapter-2]
        if adapter - 3 in sol:
            sol[adapter] += sol[adapter-3]

    print(sol[max(adapters)])


if __name__ == "__main__":
    main()
