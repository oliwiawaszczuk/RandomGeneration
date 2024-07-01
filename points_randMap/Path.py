import tkinter as tk
import random

from Point import Point, random_direction


def create_room(start_position_x, start_position_y, one_step_len, how_many_iterations):
    path_points = []
    start_position = Point(start_position_x, start_position_y)
    path_points.append(start_position)

    for i in range(how_many_iterations):
        start_position.set_custom_position(start_position_x, start_position_y)
        for j in range(one_step_len):
            new_position = Point(start_position.x, start_position.y)
            new_position.random_move()
            path_points.append(new_position)
            start_position = new_position

    return path_points


def create_path_map(how_many_steps, how_many_paths):
    path_points = []
    start_position = Point(0, 0)
    path_points.append(start_position)
    random_dir = random_direction()

    for i in range(how_many_paths):
        prev_random_dir = random_dir
        while prev_random_dir == random_dir:
            random_dir = random_direction()
        for j in range(how_many_steps):
            new_position = Point(start_position.x, start_position.y)
            new_position.move(*random_dir)
            path_points.append(new_position)
            start_position = new_position

    return path_points


def create_simple_map(how_many_steps, how_many_paths, opportunity_to_create_room, one_step_len, how_many_iterations):
    path_points = []
    start_position = Point(0, 0)
    path_points.append(start_position)
    random_dir = random_direction()

    for i in range(how_many_paths):
        prev_random_dir = random_dir
        while prev_random_dir == random_dir:
            random_dir = random_direction()
        for j in range(how_many_steps):
            new_position = Point(start_position.x, start_position.y)
            new_position.move(*random_dir)
            path_points.append(new_position)
            start_position = new_position

        if random.random() < opportunity_to_create_room:
            points_from_room = create_room(start_position.get_first_coordinate(), start_position.get_second_coordinate(), one_step_len, how_many_iterations)
            path_points.extend(points_from_room)

    return path_points
