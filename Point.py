import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, first_coordinate, second_coordinate):
        self.x += first_coordinate
        self.y += second_coordinate

    def get_first_coordinate(self):
        return self.x

    def get_second_coordinate(self):
        return self.y

    def zero(self):
        self.x = 0
        self.y = 0

    def random_move(self):
        self.move(random.choice([-1, 1]), random.choice([-1, 1]))

    def __str__(self):
        return f'({self.x}, {self.y})'
