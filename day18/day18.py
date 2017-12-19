#! /usr/bin/env python

# http://adventofcode.com/2017/day/18

import os
from collections import deque, defaultdict


def get_val(registry, value):
    try:
        return int(value)
    except ValueError:
        return registry[value]


def snd(registry, frequency):
    return get_val(registry, frequency)


def xset(registry, register, value):
    registry[register] = get_val(registry, value)


def add(registry, register, value):
    registry[register] += get_val(registry, value)


def mul(registry, register, value):
    registry[register] *= get_val(registry, value)


def mod(registry, register, value):
    registry[register] %= get_val(registry, value)


def process_part_1(instructions):
    registry = defaultdict(int)
    last_sound_freq = None
    pointer = 0
    while 0 <= pointer < len(instructions):
        instruction = instructions[pointer]
        operands = instruction[1:]
        if instruction[0] == 'snd':
            last_sound_freq = snd(registry, *operands)
        elif instruction[0] == 'set':
            xset(registry, *operands)
        elif instruction[0] == 'add':
            add(registry, *operands)
        elif instruction[0] == 'mul':
            mul(registry, *operands)
        elif instruction[0] == 'mod':
            mod(registry, *operands)
        elif instruction[0] == 'rcv':
            if get_val(registry, operands[0]):
                return last_sound_freq
        elif instruction[0] == 'jgz':
            if get_val(registry, operands[0]) > 0:
                pointer += get_val(registry, operands[1])
                continue
        else:
            raise Exception('Unknown instruction', instruction)
        pointer += 1


def process_part_2(instructions):
    queues = [
        deque(),
        deque(),
    ]

    registries = [
        defaultdict(int),
        defaultdict(int),
    ]

    pointers = [0, 0]

    waiting = [0, 0]

    running_process = 0

    send_count = [0, 0]

    # Each registry starts with register 'p' holding the process ID (0 or 1).
    registries[1]['p'] = 1

    while True:
        if all(waiting):
            break
        try:
            instruction = instructions[pointers[running_process]]
        except IndexError:
            waiting[running_process] = 1
            running_process = 1 - running_process
            continue
        registry = registries[running_process]
        operands = instruction[1:]
        if instruction[0] == 'snd':
            queues[1 - running_process].append(snd(registry, *operands))
            send_count[running_process] += 1
            waiting[1 - running_process] = 0
        elif instruction[0] == 'set':
            xset(registry, *operands)
        elif instruction[0] == 'add':
            add(registry, *operands)
        elif instruction[0] == 'mul':
            mul(registry, *operands)
        elif instruction[0] == 'mod':
            mod(registry, *operands)
        elif instruction[0] == 'rcv':
            try:
                received_value = queues[running_process].popleft()
            except IndexError:
                waiting[running_process] = 1
                running_process = 1 - running_process
                continue
            xset(registry, operands[0], received_value)
        elif instruction[0] == 'jgz':
            if get_val(registry, operands[0]) > 0:
                pointers[running_process] += get_val(registry, operands[1])
                continue
        else:
            raise Exception('Unknown instruction', instruction)
        pointers[running_process] += 1

    return send_count[1]


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        instructions = [instruction.split() for instruction in file.read().strip().split('\n')]

    print(process_part_1(instructions))

    print(process_part_2(instructions))


if __name__ == '__main__':
    run()
