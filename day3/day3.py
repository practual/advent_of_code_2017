#! /usr/bin/env python

# http://adventofcode.com/2017/day/3

import math
from collections import defaultdict


def _ring_number_from_position(position):
    return math.ceil((math.sqrt(position) - 1) / 2)


def _side_length(ring_number):
    return ring_number * 2 + 1


def _max_position_for_ring(ring_number):
    return (ring_number * 2 + 1)**2


def _is_corner(position):
    if position == 1:
        return True
    ring_number = _ring_number_from_position(position)
    return not (position - _max_position_for_ring(ring_number - 1)) % (_side_length(ring_number) - 1)


def calculate_distance(position):
    ring_number = _ring_number_from_position(position)
    if ring_number == 0:
        return ring_number
    side_length = _side_length(ring_number)
    inner_ring_max_value = _max_position_for_ring(ring_number - 1)
    distance_from_prev_midpoint = (position - inner_ring_max_value - ring_number) % (side_length - 1)
    distance_from_midpoint = min(distance_from_prev_midpoint, side_length - 1 - distance_from_prev_midpoint)
    return ring_number + distance_from_midpoint


def _sum_of_neighbours(plane, coords):
    neighbours = [(-1, 1), (0, 1), (1, 1),
                  (-1, 0),         (1, 0),
                  (-1, -1), (0, -1), (1, -1)]
    partial_sum = 0
    for neighbour in neighbours:
        try:
            partial_sum += plane[coords[0] + neighbour[0]][coords[1] + neighbour[1]]
        except KeyError:
            continue
    return partial_sum


def _turn_corner(step):
    turns = {
        (0, 1): (-1, 0),  # up -> left
        (-1, 0): (0, -1),  # left -> down
        (0, -1): (1, 0),  # down -> right
        (1, 0): (0, 1),  # right -> up
    }
    return turns[step]


def calculate_rotating_sum_greater_than_threshold(threshold):
    plane = defaultdict(dict)
    val = 1
    plane[0][0] = val
    position = 2
    coords = 1, 0
    step = 0, 1
    while val <= threshold:
        val = _sum_of_neighbours(plane, coords)
        plane[coords[0]][coords[1]] = val
        if position == _max_position_for_ring(_ring_number_from_position(position)):
            coords = coords[0] + step[0], coords[1] + step[1]
            step = _turn_corner(step)
        elif _is_corner(position):
            step = _turn_corner(step)
            coords = coords[0] + step[0], coords[1] + step[1]
        else:
            coords = coords[0] + step[0], coords[1] + step[1]
        position += 1
    return val


if __name__ == '__main__':
    input_val = 368078
    print(calculate_distance(input_val))
    print(calculate_rotating_sum_greater_than_threshold(input_val))
