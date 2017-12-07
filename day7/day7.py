#! /usr/bin/env python

# http://adventofcode.com/2017/day/7

import os
import re
from collections import Counter, defaultdict


def find_root(programme_map):
    # reverse map holds child -> parent maps. A blank string is used if the parent is not known.
    reverse = defaultdict(str)
    for parent, details in programme_map.items():
        # Set a blank parent for the parent if it's not already set.
        reverse[parent] = '' or reverse[parent]
        for child in details['children']:
            reverse[child] = parent
    # Follow a child up through its parents until a child with no parent is found.
    # This is going to be faster on average than looping through all the values assuming the
    # tree is reasonably well balanced.
    # `parent` is still defined from the previous loop so we'll use that as a starting point.
    while parent != '':
        child = parent
        parent = reverse[child]
    return child


def get_child_weight(programme_map, parent):
    child_weights = {}
    for child in programme_map[parent]['children']:
        child_weights[child] = get_child_weight(programme_map, child)

    if len(set(child_weights.values())) <= 1:
        return sum(child_weights.values()) + programme_map[parent]['weight']

    # One child has a mismatched weight. Problem doesn't make sense unless we have three or
    # more children (otherwise we couldn't say that 'only one' value needs to change - if there
    # were only two children, we could change either one.
    weights_to_children = {}
    for child, weight in child_weights.items():
        # This may override an existing value, but that's fine - we'll only lookup a weight
        # that we know has a single child for it.
        weights_to_children[weight] = child
    weight_counter = Counter(child_weights.values())
    problem_weight = min(weight_counter, key=weight_counter.get)
    problem_child = weights_to_children[problem_weight]
    target_weight = weight_counter.most_common(1)[0][0]
    updated_weight = programme_map[problem_child]['weight'] + target_weight - problem_weight
    raise Exception(
        '{} is the wrong weight. Is {} but should be {}'.format(
            problem_child, programme_map[problem_child]['weight'], updated_weight)
    )


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        lines = file.read().split('\n')

    programme_map = {}
    pattern = re.compile('([a-z]+) \(([0-9]+)\)( ->( [a-z]+,?)+)?')
    child_pattern = re.compile('[a-z]+')
    for line in lines:
        if not line:
            continue
        match = pattern.match(line)
        parent = match.group(1)
        weight = match.group(2)
        children = match.group(3)
        if children:
            children = re.findall(child_pattern, children)
        else:
            children = []
        programme_map[parent] = {'weight': int(weight), 'children': children}

    root = find_root(programme_map)
    print(root)

    get_child_weight(programme_map, root)


if __name__ == '__main__':
    run()
