#! /usr/bin/env python

# http://adventofcode.com/2017/day/2

import os


def checksum_part_1(spreadsheet):
    checksum = 0
    for row in spreadsheet.split('\n'):
        cells = [int(cell) for cell in row.split('\t') if cell]
        if not cells:
            continue
        checksum += max(cells) - min(cells)
    return checksum


def checksum_part_2(spreadsheet):
    checksum = 0
    for row in spreadsheet.split('\n'):
        sorted_cells = sorted([int(cell) for cell in row.split('\t') if cell], key=int)
        if not sorted_cells:
            continue
        max_value = sorted_cells[-1]
        multiples = dict()
        for base in sorted_cells:
            if base in multiples:
                checksum += multiples[base]
                break
            multiplier = 2
            while True:
                product = base * multiplier
                if product > max_value:
                    break
                multiples[product] = multiplier
                multiplier += 1
    return checksum


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        spreadsheet = file.read()

    print(checksum_part_1(spreadsheet))
    print(checksum_part_2(spreadsheet))
