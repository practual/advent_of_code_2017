#! /usr/bin/env python

# http://adventofcode.com/2017/day/9

import os


def process_stream(stream):
    total_score = 0
    score_for_group = 0
    garbage_chars = 0
    skip_next = False
    in_garbage = False
    for char in stream:
        if not char:
            continue
        if skip_next:
            skip_next = False
            continue
        if char == '{' and not in_garbage:
            score_for_group += 1
            total_score += score_for_group
        elif char == '}' and not in_garbage:
            score_for_group -= 1
        elif char == '<' and not in_garbage:
            in_garbage = True
        elif char == '>':
            in_garbage = False
        elif char == '!':
            skip_next = True
        elif in_garbage:
            garbage_chars += 1
    return total_score, garbage_chars


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        stream = file.read()

    print(process_stream(stream))


if __name__ == '__main__':
    run()
