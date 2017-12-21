#! /usr/bin/env python

# http://adventofcode.com/2017/day/21

import math
import os

import numpy as np


def unpack(string):
    return np.array([[1 if char == '#' else 0 for char in row] for row in string.split('/')])


def flatten(pattern):
    return '/'.join([''.join(['#' if cell else '.' for cell in row]) for row in pattern])


def expand(rules, pattern):
    size = int(math.sqrt(pattern.size))
    jump = 3 if size % 2 else 2
    new_pattern = None
    for row in range(0, size, jump):
        new_row = None
        for col in range(0, size, jump):
            subpattern = pattern[row:row+jump, col:col+jump]
            target = None
            for f in range(2):
                for r in range(4):
                    try:
                        target = rules[flatten(subpattern)]
                        break
                    except KeyError:
                        pass
                    subpattern = np.rot90(subpattern)
                if target:
                    break
                subpattern = np.flip(subpattern, 0)
            else:
                raise Exception('Could not find pattern in rulebook!')
            if new_row is None:
                new_row = unpack(target)
            else:
                new_row = np.concatenate((new_row, unpack(target)), axis=1)
        if new_pattern is None:
            new_pattern = new_row
        else:
            new_pattern = np.concatenate((new_pattern, new_row), axis=0)
    return new_pattern


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        rules = {from_pattern: to_pattern
                 for from_pattern, to_pattern in [
                     rule_string.split(' => ') for rule_string in file.read().strip().split('\n')
                 ]}

    pattern = unpack('.#./..#/###')
    for i in range(18):
        if i == 5:
            print('PART 1: ', np.sum(pattern))
        pattern = expand(rules, pattern)
    print('PART 2: ', np.sum(pattern))


if __name__ == '__main__':
    run()
