#! /usr/bin/env python

# http://adventofcode.com/2017/day/16

import os
from collections import deque


def spin(programmes, distance):
    programmes.rotate(distance)


def exchange(programmes, index_a, index_b):
    swap = programmes[index_a]
    programmes[index_a] = programmes[index_b]
    programmes[index_b] = swap


def partner(programmes, programme_a, programme_b):
    # This one is pretty slow since we have to lookup each programme's position. Could maybe keep
    # a separate lookup from programme -> index.
    index_a = programmes.index(programme_a)
    index_b = programmes.index(programme_b)
    exchange(programmes, index_a, index_b)


def process(programmes, instructions):
    programmes = deque(programmes)
    for instruction in instructions:
        operands = instruction[1:].split('/')
        if instruction[0] == 's':
            spin(programmes, int(operands[0]))
        elif instruction[0] == 'x':
            exchange(programmes, int(operands[0]), int(operands[1]))
        elif instruction[0] == 'p':
            operands = instruction[1:].split('/')
            partner(programmes, operands[0], operands[1])
        else:
            raise Exception('Unknown instruction', instruction)
    return list(programmes)


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        instructions = file.read().strip().split(',')

    # a -> p
    programmes = [chr(i) for i in range(97, 97 + 16)]
    print(''.join(process(programmes, instructions)))

    # Run it a billion times! The 'partner' instruction prevents you from working out where each
    # letter ends up relative to its starting position. However, if we see the starting pattern
    # again we can cut out a big chunk of the loop.
    original = programmes.copy()
    for i in range(1000000000):
        programmes = process(programmes, instructions)
        if programmes == original:
            break
    else:
        # Didn't see a repeat - is this possible?
        print(''.join(programmes))
        return

    # We saw a repeat so we can just loop over the last leg:
    for j in range(1000000000 % (i + 1)):
        programmes = process(programmes, instructions)
    print(''.join(programmes))


if __name__ == '__main__':
    run()
