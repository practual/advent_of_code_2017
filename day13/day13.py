#! /usr/bin/env python

# http://adventofcode.com/2017/day/13

import os
import re
from collections import defaultdict


def count_severity(layers):
    severity = 0
    for depth, layer_range in layers.items():
        assert layer_range > 1
        severity += (depth * layer_range) if not depth % (2 * layer_range - 2) else 0
    return severity


def find_min_delay(layers):
    delay = 0
    caught = True
    while caught:
        caught = False
        for depth, layer_range in layers.items():
            if not (depth + delay) % (2 * layer_range - 2):
                caught = True
                delay += 1
                break
    return delay


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        layers = {
            int(depth.strip()): int(layer_range.strip())
            for depth, layer_range in [line.split(':') for line in file.readlines()]
        }

    print(count_severity(layers))
    print(find_min_delay(layers))


if __name__ == '__main__':
    run()
