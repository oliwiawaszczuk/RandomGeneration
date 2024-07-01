import random


def random_direction():
    directions = [
        (0, 1),  # TOP
        (0, -1),  # DOWN
        (1, 0),  # RIGHT
        (-1, 0)  # LEFT
    ]
    return random.choice(directions)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_custom_position(self, x, y):
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
        move = random_direction()
        self.move(*move)

    def __str__(self):
        return f'({self.x}, {self.y})'
