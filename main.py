from __future__ import division
import math
import random


class RandPoint(object):
    def __init__(self):
        angle = random.uniform(0, 2 * math.pi)
        position = math.sqrt(random.uniform(0, 1))
        self.x = position * math.cos(angle)
        self.y = position * math.sin(angle)

    def move(self):
        angle = random.uniform(0, 2 * math.pi)
        self.x += math.cos(angle)
        self.y += math.sin(angle)

    def check(self):
        return self.x ** 2 + self.y ** 2 < 1 ** 2 # Last exponent added for clarity

passed = 0
num = int(raw_input("How many trials would you like? \n"))

for _ in range(num):
    startingpoint = RandPoint()
    startingpoint.move()
    passed += int(startingpoint.check())

print("{} tries, {} passes, {}%".format(num, passed, passed / num * 100))