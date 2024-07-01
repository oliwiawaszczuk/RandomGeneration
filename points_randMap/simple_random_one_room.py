from Path import create_room
from create_window import create_window, draw_points_on_tkinter_window

current_canvas = None
one_step_len = 200
how_many_iterations = 20


def create_window_to_simple_one_room():
    root, button_to_generation = create_window('Random Generation Room')
    button_to_generation.config(command=lambda: create_simple_one_room(root))
    root.mainloop()


def create_simple_one_room(root):
    path_points = create_room(0, 0, one_step_len, how_many_iterations)
    global current_canvas
    canvas = draw_points_on_tkinter_window(root, path_points, current_canvas)
    current_canvas = canvas
