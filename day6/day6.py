#! /usr/bin/env python

# http://adventofcode.com/2017/day/6

import os


def _redistribute_blocks(banks):
    blocks_to_redistribute = max(banks)
    bank_index = banks.index(blocks_to_redistribute)
    banks[bank_index] = 0
    while blocks_to_redistribute:
        bank_index = (bank_index + 1) % len(banks)
        banks[bank_index] += 1
        blocks_to_redistribute -= 1


def count_steps_until_repeat(banks):
    # Make a copy
    banks = banks[:]
    seen_configs = set()
    steps = 0
    while tuple(banks) not in seen_configs:
        seen_configs.add(tuple(banks))
        steps += 1
        _redistribute_blocks(banks)
    return steps, banks


def count_steps_in_loop(banks):
    # Make a copy
    banks = banks[:]
    starting_point = tuple(banks)
    steps = 0
    while tuple(banks) != starting_point or steps == 0:
        steps += 1
        _redistribute_blocks(banks)
    return steps


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        banks = [int(instruction) for instruction in file.read().split('\t') if instruction]

    steps, loop_starting_point = count_steps_until_repeat(banks)
    print(steps)
    print(count_steps_in_loop(loop_starting_point))
