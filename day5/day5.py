#! /usr/bin/env python

# http://adventofcode.com/2017/day/5

import os


def count_steps_until_exit_part_1(programme):
    programme = programme[:]
    steps = 0
    pointer = 0
    while 0 <= pointer < len(programme):
        steps += 1
        offset = programme[pointer]
        programme[pointer] += 1
        pointer += offset
    return steps


def count_steps_until_exit_part_2(programme):
    programme = programme[:]
    steps = 0
    pointer = 0
    while 0 <= pointer < len(programme):
        steps += 1
        offset = programme[pointer]
        programme[pointer] += -1 if offset >= 3 else 1
        pointer += offset
    return steps


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        programme = [int(instruction) for instruction in file.read().split('\n') if instruction]

    print(count_steps_until_exit_part_1(programme))
    print(count_steps_until_exit_part_2(programme))
