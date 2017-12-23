#! /usr/bin/env python

# http://adventofcode.com/2017/day/23

import math
import os
from collections import defaultdict


def get_val(registry, value):
    try:
        return int(value)
    except ValueError:
        return registry[value]


def snd(registry, frequency):
    return get_val(registry, frequency)


def xset(registry, register, value):
    registry[register] = get_val(registry, value)


def sub(registry, register, value):
    registry[register] -= get_val(registry, value)


def mul(registry, register, value):
    registry[register] *= get_val(registry, value)


def mod(registry, register, value):
    registry[register] %= get_val(registry, value)


def process(instructions):
    registry = defaultdict(int)
    mul_count = 0
    pointer = 0
    while 0 <= pointer < len(instructions):
        instruction = instructions[pointer]
        operands = instruction[1:]
        if instruction[0] == 'set':
            xset(registry, *operands)
        elif instruction[0] == 'sub':
            sub(registry, *operands)
        elif instruction[0] == 'mul':
            mul(registry, *operands)
            mul_count += 1
        elif instruction[0] == 'jnz':
            if get_val(registry, operands[0]):
                pointer += get_val(registry, operands[1])
                continue
        else:
            raise Exception('Unknown instruction', instruction)
        pointer += 1
    return mul_count


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        instructions = [instruction.split() for instruction in file.read().strip().split('\n')]

    print(process(instructions))

    """
    When a is set to 1, the programme condenses down to:

    h = 0
    for b in range(105700, 122700 + 1, 17):
        f = 1
        for d in range(2, b + 1):
            for e in range(2, b + 1):
                if d * e == b:
                    f = 0
        if not f:
            h += 1
            
    Which asks how many non-primes there are between 105700 and 122700 (in steps of 17).
    """

    # Sieve to find the primes not greater than sqrt(122700)
    root = math.floor(math.sqrt(122700))
    primes = set(range(2, root + 1))
    for i in range(2, root + 1):
        if i not in primes:
            continue
        j = i ** 2
        while j <= root:
            try:
                primes.remove(j)
            except KeyError:
                pass
            j += i

    # Now use these primes to find non-primes in the range.
    non_primes = 0
    for b in range(105700, 122700 + 1, 17):
        for p in primes:
            if not b % p:
                non_primes += 1
                break
    print(non_primes)


if __name__ == '__main__':
    run()
