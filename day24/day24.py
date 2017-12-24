#! /usr/bin/env python

# http://adventofcode.com/2017/day/24

import os


def components_for_left(components, left):
    return [component for component in components if left in component]


def get_right(component, left):
    return component[1] if component[0] == left else component[0]


def get_chains(components, left):
    max_strength = 0
    longest = 0
    strength_for_longest = 0
    chains = {}
    for component in components_for_left(components, left):
        components_copy = components.copy()
        components_copy.remove(component)
        chain, max_subchain_strength, longest_subchain, longest_subchain_strength = get_chains(components_copy, get_right(component, left))
        longest_subchain += 1
        longest_subchain_strength += sum(component)
        max_subchain_strength += sum(component)
        if longest_subchain > longest:
            longest = longest_subchain
            strength_for_longest = longest_subchain_strength
        elif longest_subchain == longest:
            strength_for_longest = max(strength_for_longest, longest_subchain_strength)
        max_strength = max(max_strength, max_subchain_strength)
        chains[component] = chain
    return chains, max_strength, longest, strength_for_longest


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        components = set(tuple(map(int, component.split('/'))) for component in file.read().strip().split('\n'))

    chain_output = get_chains(components, 0)
    print(chain_output[1], chain_output[3])


if __name__ == '__main__':
    run()
