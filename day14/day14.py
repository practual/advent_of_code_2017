# http://adventofcode.com/2017/day/14

# Note, this is a bit screwy but you need to run this program as `python -m day14.day14` to make
# the relative imports work.
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3

import copy
from day10.day10 import compute_hash


def count_ones(bin_array):
    ones_sum = 0
    for row in bin_array:
        ones_sum += sum(row)
    return ones_sum


def _explore_region(bin_array, i, j):
    if not bin_array[i][j]:
        return
    bin_array[i][j] = 0
    if i:
        # Look up
        _explore_region(bin_array, i - 1, j)
    if j + 1 < 128:
        # Look right
        _explore_region(bin_array, i, j + 1)
    if i + 1 < 128:
        # Look down
       _explore_region(bin_array, i + 1, j)
    if j:
        # Look left
        _explore_region(bin_array, i, j - 1)


def count_regions(bin_array):
    # Make a copy
    bin_array = copy.deepcopy(bin_array)
    region_count = 0
    for i in range(128):
        for j in range(128):
            if not bin_array[i][j]:
                continue
            region_count += 1
            _explore_region(bin_array, i, j)
    return region_count


def run():
    key_string = 'uugsqrei'
    bin_array = []
    region_array = []
    max_region_num = 0
    replacements = {}
    for i in range(128):
        hex_hash = compute_hash('{}-{}'.format(key_string, i))
        bin_hash = ''.join(['{0:04b}'.format(int(hex_char, 16)) for hex_char in hex_hash])
        bin_array.append([int(bin_char) for bin_char in bin_hash])

    print('SUM OF "1"s', count_ones(bin_array))
    print('REGION COUNT:', count_regions(bin_array))
    return


if __name__ == '__main__':
    run()
