from Point import Point


def create_path(one_step_len, how_many_iterations):
    path_points = []
    start_position = Point(0, 0)
    path_points.append(start_position)

    for i in range(how_many_iterations):
        start_position.zero()
        for j in range(one_step_len):
            new_position = Point(start_position.x, start_position.y)
            new_position.random_move()
            path_points.append(new_position)
            start_position = new_position

    return list(set(path_points))
