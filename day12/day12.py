#! /usr/bin/env python

# http://adventofcode.com/2017/day/12

import os
import re
from collections import defaultdict


def find_links(pipes):
    linked = defaultdict(set)
    for parent, children in pipes.items():
        process_set = set([parent] + children)
        for process in [parent] + children:
            linked[process] |= process_set
    return linked


def find_group(links, root, seen=None):
    seen = seen or set()
    seen.add(root)
    for process in links[root]:
        if process in seen:
            continue
        else:
            find_group(links, process, seen)
    return seen


def count_groups(links):
    processes = set(links.keys())
    group_count = 0
    while len(processes):
        group_count += 1
        process = processes.pop()
        processes_in_group = find_group(links, process)
        processes -= processes_in_group
    return group_count


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        pipe_strings = file.read().strip().split('\n')

    pipes = {}
    for pipe in pipe_strings:
        pattern = re.compile('([0-9]+) <->(( [0-9]+,?)+)')
        match = pattern.match(pipe)
        parent = int(match.group(1))
        children = [int(child.strip()) for child in match.group(2).split(',')]
        pipes[parent] = children

    links = find_links(pipes)
    print(len(find_group(links, 0)))
    print(count_groups(links))


if __name__ == '__main__':
    run()
