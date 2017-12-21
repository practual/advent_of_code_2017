#! /usr/bin/env python

# http://adventofcode.com/2017/day/20

import os
import re
from collections import defaultdict


def vector_add(a, b):
    # Index-wise summing of two tuples.
    return tuple(map(sum, zip(a, b)))


def sort_by(particles, attribute, index):
    return tuple(map(lambda particle: particle['id'], sorted(particles, key=lambda particle: particle[attribute][index])))


def run():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = os.path.join(current_dir, 'input')

    with open(input_file_name, 'r') as file:
        particles_input = file.read().strip().split('\n')

    pattern = re.compile('.*a=<(.*)>')
    particle_num = 0
    min_acceleration = float('inf')
    slowest_particles = set()
    for particle_string in particles_input:
        match = pattern.match(particle_string)
        a_x, a_y, a_z = [int(a) for a in match.group(1).split(',')]
        acceleration = abs(a_x) + abs(a_y) + abs(a_z)
        if acceleration == min_acceleration:
            slowest_particles.add(particle_num)
        elif acceleration < min_acceleration:
            min_acceleration = acceleration
            slowest_particles = {particle_num}
        particle_num += 1

    # It turns out that there's only one 'slowest' particle so this solution is good enough.
    print('CLOSEST PARTICLE', slowest_particles)

    pattern = re.compile('p=<(.*)>, v=<(.*)>, a=<(.*)>')
    particles = []
    particle_num = 0
    for particle_string in particles_input:
        match = pattern.match(particle_string)
        p_x, p_y, p_z = [int(p) for p in match.group(1).split(',')]
        v_x, v_y, v_z = [int(v) for v in match.group(2).split(',')]
        a_x, a_y, a_z = [int(a) for a in match.group(3).split(',')]
        particles.append({'id': particle_num, 'p': (p_x, p_y, p_z),
                          'v': (v_x, v_y, v_z), 'a': (a_x, a_y, a_z)})
        particle_num += 1

    collided = set()
    # Seems that this is sufficient iterations to determine a steady state.
    for i in range(10000):
        positions = defaultdict(set)
        for particle in particles:
            if particle['id'] in collided:
                continue
            did_collide = False
            if particle['p'] in positions:
                did_collide = True
            positions[(particle['p'])].add(particle['id'])
            if did_collide:
                collided |= positions[particle['p']]
            particle['v'] = vector_add(particle['v'], particle['a'])
            particle['p'] = vector_add(particle['p'], particle['v'])

    min_distance = float('inf')
    closest_particle = None
    for particle in particles:
        distance = abs(particle['p'][0]) + abs(particle['p'][1]) + abs(particle['p'][2])
        if distance < min_distance:
            min_distance = distance
            closest_particle = particle['id']

    print('CLOSEST PARTICLE', closest_particle)

    print('REMAINING', len(particles) - len(collided))




if __name__ == '__main__':
    run()
