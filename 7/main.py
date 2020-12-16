from collections import defaultdict
from typing import List, DefaultDict, Tuple
import os
from collections import Counter, defaultdict
import re
from re import findall


parents = defaultdict(lambda: [])
child_map = defaultdict(lambda: ())


def main() -> None:
    with open('input.txt', 'r') as file:
        lines = file.read().split('\n')

    part_one(lines)
    print(len(find_parents('shiny gold')))
    part_two(lines)
    print(count_children('shiny gold'))


def part_one(lines) -> None:
    for line in lines:
        parent = line.split(' bags contain ')[0]
        children = re.findall(r'\d ([\w ]+) bag', line)

        for child in children:
            parents[child].append(parent)


def find_parents(bag) -> set:
    return set().union(parents[bag], *(find_parents(parent) for parent in parents[bag]))


def part_two(lines) -> int:
    for line in lines:
        parent = line.split(' bags contain ')[0]
        children: List[Tuple[str, str]] = findall(r'(\d+) ([\w ]+) bag', line)
        child_map[parent] = tuple((int(a), b) for a, b in children)


def count_children(bag: str) -> int:
    return sum(child_count * (1 + count_children(child)) for child_count, child in child_map[bag])


if __name__ == "__main__":
    main()
