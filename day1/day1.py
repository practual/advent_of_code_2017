#! /usr/bin/env python

# http://adventofcode.com/2017/day/1

import os


def captcha_output_part_1(captcha):
    partial_sum = 0
    for i in range(len(captcha)):
        next_i = (i + 1) % len(captcha)
        if captcha[i] == captcha[next_i]:
            partial_sum += int(captcha[i])
    return partial_sum


def captcha_output_part_2(captcha):
    if len(captcha) % 2:
        raise Exception('Captcha has an odd number of digits - cannot compute output.')
    step = int(len(captcha) / 2)
    partial_sum = 0
    for i in range(len(captcha)):
        next_i = (i + step) % len(captcha)
        if captcha[i] == captcha[next_i]:
            partial_sum += int(captcha[i])
    return partial_sum


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        captcha = file.read().replace('\n', '')
    print(captcha_output_part_1(captcha))
    print(captcha_output_part_2(captcha))
