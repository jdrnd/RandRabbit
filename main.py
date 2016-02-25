import math
import random


class RandPoint:
    x = 0
    y = 0

    def __init__(self):
        self.x = random.uniform(-1,1)
        self.y = random.uniform(-1,1)

    def move(self):
        angle = random.uniform(0, 2 * math.pi)
        self.x+=math.cos(angle)
        self.y+=math.sin(angle)

    def check(self):
        return math.sqrt(math.pow(self.x,2)+math.pow(self.y,2)) < 1


passed = 0.0
num = int(raw_input("How many trials would you like? \n"))

for value in range (1,num):
    startingpoint = RandPoint()

    while not(startingpoint.check()):
        startingpoint = RandPoint()

    startingpoint.move()
    passed += int(startingpoint.check())

print (str(num) + " trys, " + str(passed) + " passes, " + str((passed/num)*100) + "%")