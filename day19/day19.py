#! /usr/bin/env python

# http://adventofcode.com/2017/day/19

import os


def vector_add(a, b):
    # Index-wise summing of two tuples.
    return tuple(map(sum, zip(a, b)))


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        route_map = [list(row) for row in file.read().split('\n')]

    # First line only has the | so the array will end on that character.
    coords = (0, len(route_map[0]) - 1)
    direction = (1, 0)
    letters_seen = ''
    steps = 1
    while True:
        coords = vector_add(coords, direction)
        char = route_map[coords[0]][coords[1]]
        if char == '+':
            if direction[0] == 0:
                # Moving left / right, so look up and down
                direction = (1, 0)
                try:
                    if route_map[coords[0] - 1][coords[1]] == '|':
                        direction = (-1, 0)
                except IndexError:
                    pass
            else:
                # Moving up / down, so look left and right
                direction = (0, 1)
                try:
                    if coords[1] and route_map[coords[0]][coords[1] - 1] == '-':
                        direction = (0, -1)
                except IndexError:
                    pass
        elif char in ['-', '|']:
            pass
        elif char != ' ':
            letters_seen += char
        else:
            break
        steps += 1
    print('{} in {} steps.'.format(''.join(letters_seen), steps))


if __name__ == '__main__':
    run()
