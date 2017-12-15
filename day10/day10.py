#! /usr/bin/env python

# http://adventofcode.com/2017/day/10

import os
from collections import deque
from functools import reduce


def run_loop(loop, lengths, position, step):
    for length in lengths:
        # Rotate the loop so that the current position is as the start.
        loop = deque(loop)
        loop.rotate(-position)
        loop = list(loop)
        # Reverse the starting portion of the loop.
        loop[:length] = loop[:length][::-1]
        # Rotate the loop back to its original position.
        loop = deque(loop)
        loop.rotate(position)
        loop = list(loop)
        position += length + step
        step += 1
    return loop, position, step


def compute_hash(input_string):
    # Get the ASCII code point vals for each character
    points = [ord(char) for char in input_string]
    # Add the given suffix
    points = points + [17, 31, 73, 47, 23]
    loop = list(range(0, 256))
    position = 0
    step = 0
    for i in range(0,64):
        loop, position, step = run_loop(loop, points, position, step)
    # Split the loops into blocks of 16.
    blocks = [loop[i:i+16] for i in range(0, len(loop), 16)]
    # XOR each block
    dense_hash = [reduce(lambda x, y: x ^ y, block) for block in blocks]
    return ''.join([format(block, '02x') for block in dense_hash])


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        chars = file.read()

    lengths = [int(length.strip()) for length in chars.split(',') if length]

    loop, position, step = run_loop(list(range(0, 256)), lengths, 0, 0)
    print(loop[0] * loop[1])

    print(compute_hash(chars.strip()))


if __name__ == '__main__':
    run()
