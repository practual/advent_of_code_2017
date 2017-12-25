#! /usr/bin/env python

# http://adventofcode.com/2017/day/25

import os
from collections import defaultdict


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        blueprint = file.read().strip().split('\n\n')

    checksum_steps = int(blueprint[0].split()[-2])

    states = []
    for state in blueprint[1:]:
        state = state.split('\n')
        states.append([
            (1 if '1' in state[2] else 0, 1 if 'right' in state[3] else -1, ord(state[4][-2]) - 65),
            (1 if '1' in state[6] else 0, 1 if 'right' in state[7] else -1, ord(state[8][-2]) - 65),
        ])

    tape = defaultdict(int)
    slot = 0
    state = 0
    for i in range(checksum_steps):
        current_value = tape[slot]
        tape[slot] = states[state][current_value][0]
        slot += states[state][current_value][1]
        state = states[state][current_value][2]

    checksum = sum(tape.values())
    print(checksum)


if __name__ == '__main__':
    run()
