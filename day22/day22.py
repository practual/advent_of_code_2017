#! /usr/bin/env python

# http://adventofcode.com/2017/day/22


import copy
import math
import os
from collections import defaultdict


TURN_RIGHT_MAP = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}


TURN_LEFT_MAP = {
    (-1, 0): (0, -1),
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
}


def vector_add(a, b):
    return tuple(map(sum, zip(a, b)))


def turn(direction, left_or_right):
    # left_or_right = 1 for left and 0 for right.
    turn_map = TURN_LEFT_MAP if left_or_right else TURN_RIGHT_MAP
    return turn_map[direction]


def part_1(grid):
    grid = copy.deepcopy(grid)
    coords = (0, 0)
    direction = (-1, 0)  # Starts facing up
    infected_count = 0
    for i in range(10000):
        try:
            is_clean = int(not grid[coords[0]][coords[1]])
        except KeyError:
            is_clean = 1
        direction = turn(direction, is_clean)
        grid[coords[0]][coords[1]] = is_clean
        infected_count += 1 if is_clean else 0
        coords = vector_add(coords, direction)

    return infected_count


STATE_MAP = {
    0: 'W',
    'W': 1,
    1: 'F',
    'F': 0,
}


def part_2(grid):
    grid = copy.deepcopy(grid)
    coords = (0, 0)
    direction = (-1, 0)
    infected_count = 0
    for i in range(10000000):
        try:
            state = grid[coords[0]][coords[1]]
        except KeyError:
            state = 0
        if state == 0 or state == 1:
            # Clean or infected, turn as normal
            direction = turn(direction, 1 - state)
        elif state == 'F':
            # Flagged, turn around
            direction = turn(turn(direction, 0), 0)
        state = STATE_MAP[state]
        grid[coords[0]][coords[1]] = state
        infected_count += 1 if state == 1 else 0
        coords = vector_add(coords, direction)

    return infected_count


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    grid = defaultdict(dict)
    with open(input_file_name, 'r') as file:
        grid_strings = file.read().strip().split('\n')

    # Constructs a grid where the negative coords are in the top left.
    starting_coord = -math.floor(len(grid_strings) / 2)
    for i, row in enumerate(grid_strings, start=starting_coord):
        for j, col in enumerate(row, start=starting_coord):
            grid[i][j] = 1 if col == '#' else 0

    print(part_1(grid))
    print(part_2(grid))


if __name__ == '__main__':
    run()
