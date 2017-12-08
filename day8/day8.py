#! /usr/bin/env python

# http://adventofcode.com/2017/day/8

import os
import re
from collections import defaultdict


def run_programme(registers, instructions):
    max_value_seen = 0
    for instruction in instructions:
        compare_value = registers[instruction['compare_register']]
        operator = instruction['operator']
        operand = int(instruction['operand'])
        if operator not in ['==', '!=', '<', '<=', '>', '>=']:
            raise Exception('Unknown operator {}'.format(operator))
        condition_met = eval('{} {} {}'.format(compare_value, operator, operand))
        if not condition_met:
            continue
        modifier_operator = {'dec': '-', 'inc': '+'}[instruction['instruction']]
        modifier = int(instruction['modifier'])
        register = instruction['register']
        current_value = registers[register]
        new_value = eval('{} {} {}'.format(current_value, modifier_operator, modifier))
        registers[register] = new_value
        max_value_seen = max(max_value_seen, new_value)
    return max_value_seen


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        lines = file.read().split('\n')

    instructions = []
    pattern = re.compile(
        '(?P<register>[a-z]+) (?P<instruction>inc|dec) (?P<modifier>-?[0-9]+) if (?P<compare_regist'
        'er>[a-z]+) (?P<operator>[!=<>]+) (?P<operand>-?[0-9]+)'
    )
    for line in lines:
        match = re.match(pattern, line)
        if not match:
            continue
        instructions.append(match.groupdict())

    registers = defaultdict(int)
    max_value_seen = run_programme(registers, instructions)
    print(max(registers.values()), max_value_seen)


if __name__ == '__main__':
    run()
