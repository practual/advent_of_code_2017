#! /usr/bin/env python

# http://adventofcode.com/2017/day/17


def run():
    steps = 376
    buffer = [0]
    position = 0
    for i in range(2017):
        position = (position + steps) % len(buffer) + 1
        buffer[position:1] = [i + 1]
    # Print the number after 2017.
    print(buffer[position + 1])

    position = 0
    val_after_zero = None
    for i in range(1, 50000000 + 1):
        position = (position + steps) % i + 1
        if position == 1:
            val_after_zero = i
    print(val_after_zero)


if __name__ == '__main__':
    run()
