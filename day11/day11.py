#! /usr/bin/env python

# http://adventofcode.com/2017/day/11

import os

import numpy as np


def walk(directions):
    a = np.array([1, 0, 0])
    b = np.array([0, 1, 0])
    c = np.array([0, 0, 1])
    direction_map = {
        'n': a,
        'ne': b,
        'se': c,
        's': -a,
        'sw': -b,
        'nw': -c,
    }
    position = np.array([0, 0, 0])
    max_steps = 0
    for direction in directions:
        position += direction_map[direction]
        distance = reduce(position)
        max_steps = max(max_steps, distance)
    return position, max_steps


def reduce(position):
    position = np.copy(position)
    equivalence = np.array([1, -1, 1])  # i.e. a - b + c = 0
    min_steps = np.sum(np.absolute(position))
    reduction_direction = -np.sign(np.sum(np.sign(position) * equivalence))
    while True:
        position += reduction_direction * equivalence
        steps = np.sum(np.absolute(position))
        if steps >= min_steps:
            break
        min_steps = steps
    return min_steps


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        directions = file.read().strip().split(',')

    position, max_steps = walk(directions)
    distance = reduce(position)
    print('FINAL DISTANCE', distance)
    print('MAX DISTANCE', max_steps)


if __name__ == '__main__':
    run()
