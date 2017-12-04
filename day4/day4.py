#! /usr/bin/env python

# http://adventofcode.com/2017/day/4

import os


def check_valid_passphrases_part_1(passphrases):
    num_valid = 0
    for passphrase in passphrases.split('\n'):
        words = passphrase.split()
        if not words:
            continue
        # Add 1 if there as many unique words as there are words.
        num_valid += len(set(words)) == len(words)
    return num_valid


def check_valid_passphrases_part_2(passphrases):
    num_valid = 0
    for passphrase in passphrases.split('\n'):
        words = [''.join(sorted(word)) for word in passphrase.split()]
        if not words:
            continue
        num_valid += len(set(words)) == len(words)
    return num_valid


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        passphrases = file.read()

    print(check_valid_passphrases_part_1(passphrases))
    print(check_valid_passphrases_part_2(passphrases))
