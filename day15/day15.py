#! /usr/bin/env python

# http://adventofcode.com/2017/day/15


def generator(factor, seed, multiple=1):
    prev = seed
    while True:
        new = prev * factor % 2147483647
        prev = new
        if not new % multiple:
            yield new


def part1():
    matches = 0
    generator_a = generator(16807, 703)
    generator_b = generator(48271, 516)
    for i in range(40000000):
        # 0 fill up to at least 16 digits
        if format(next(generator_a), '016b')[-16:] == format(next(generator_b), '016b')[-16:]:
            matches += 1
    return matches


def part2():
    matches = 0
    generator_a = generator(16807, 703, 4)
    generator_b = generator(48271, 516, 8)
    for i in range(5000000):
        # 0 fill up to at least 16 digits
        if format(next(generator_a), '016b')[-16:] == format(next(generator_b), '016b')[-16:]:
            matches += 1
    return matches


def run():
    print(part1())
    print(part2())




if __name__ == '__main__':
    run()
