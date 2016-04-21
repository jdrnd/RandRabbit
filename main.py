#!/usr/bin/env python3

from math import cos, sin, sqrt, pi
from random import uniform as random
from timeit import default_timer as time


class RandPoint(object):
    def __init__(self):
        angle = random(0, 2 * pi)
        position = sqrt(random(0, 1))
        self.x = position * cos(angle)
        self.y = position * sin(angle)

    def move(self):
        angle = random(0, 2 * pi)
        self.x += cos(angle)
        self.y += sin(angle)

    def check(self):
        return self.x ** 2 + self.y ** 2 < 1 ** 2  # Last exponent added for clarity


def main():
    start = time()
    passed = 0
    num = int(input("How many trials would you like? \n"))

    for _ in range(num):
        startingPoint = RandPoint()
        startingPoint.move()
        passed += float(startingPoint.check())

    end = time()
    elapsed = end - start
    print("{} tries, {} passes, {:.2f}% in {:0.2f} seconds, {:0.2f} tries/second".format(num, passed, passed / num * 100, elapsed, num /elapsed))


if __name__ == "__main__":
    main()
