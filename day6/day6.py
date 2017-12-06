#! /usr/bin/env python

# http://adventofcode.com/2017/day/6

import os


def count_steps_until_repeat(banks):
    # Make a copy
    banks = banks[:]
    seen_configs = []
    steps = 0
    while tuple(banks) not in seen_configs:
        seen_configs.append(tuple(banks))
        steps += 1
        blocks_to_redistribute = max(banks)
        bank_index = banks.index(blocks_to_redistribute)
        banks[bank_index] = 0
        while blocks_to_redistribute:
            bank_index = (bank_index + 1) % len(banks)
            banks[bank_index] += 1
            blocks_to_redistribute -= 1
    return steps, steps - seen_configs.index(tuple(banks))


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        banks = [int(instruction) for instruction in file.read().split('\t') if instruction]

    print(count_steps_until_repeat(banks))
