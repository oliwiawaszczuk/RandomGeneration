from Path import create_simple_map
from create_window import create_window, draw_points_on_tkinter_window

current_canvas = None
how_many_steps = 20
how_many_paths = 20
opportunity_to_create_room = 0.7
one_step_len = 20
how_many_iterations = 10


def create_window_to_simple_paths_with_rooms():
    root, button_to_generation = create_window('Random Generation Paths With Rooms')
    button_to_generation.config(command=lambda: create_simple_paths_with_rooms(root))
    root.mainloop()


def create_simple_paths_with_rooms(root):
    path_points = create_simple_map(how_many_steps, how_many_paths, opportunity_to_create_room, one_step_len, how_many_iterations)
    global current_canvas
    canvas = draw_points_on_tkinter_window(root, path_points, current_canvas)
    current_canvas = canvas
