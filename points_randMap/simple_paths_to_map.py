from Path import create_path_map
from create_window import create_window, draw_points_on_tkinter_window

current_canvas = None
how_many_steps = 20
how_many_paths = 20


def create_window_to_simple_paths():
    root, button_to_generation = create_window('Random Generation Paths')
    button_to_generation.config(command=lambda: create_simple_paths(root))
    root.mainloop()


def create_simple_paths(root):
    path_points = create_path_map(how_many_steps, how_many_paths)
    global current_canvas
    canvas = draw_points_on_tkinter_window(root, path_points, current_canvas)
    current_canvas = canvas
