import tkinter as tk


def find_size_and_center_for_window(path_points, win_size):
    x_coords = [x.get_first_coordinate() for x in path_points]
    y_coords = [x.get_second_coordinate() for x in path_points]

    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    abs_x = abs(min_x) + abs(max_x)
    abs_y = abs(min_y) + abs(max_y)

    size = win_size // (3 * max(abs_x, abs_y))
    center_of_window_x = (abs_x + win_size) // 2
    center_of_window_y = (abs_y + win_size) // 2

    return size, center_of_window_x, center_of_window_y


def create_window(title):
    root = tk.Tk()
    root.geometry('750x790+550+15')
    root.resizable(False, False)
    root.title(title)
    root['bg'] = '#252831'

    button_to_generation = tk.Button(root, text=title)
    button_to_generation.pack(side=tk.TOP, pady=5)

    return root, button_to_generation


def draw_points_on_tkinter_window(root, path_points, current_canvas):
    diff_points = set((point.get_first_coordinate(), point.get_second_coordinate()) for point in path_points)
    print(f'generating random points with {len(path_points)} points, which contains {len(diff_points)} different points')

    if current_canvas:
        current_canvas.destroy()
    win_size = 750
    canvas = tk.Canvas(root, width=win_size, height=win_size, bg='#3b404e')
    canvas.pack()

    size, center_of_window_x, center_of_window_y = find_size_and_center_for_window(path_points, win_size)

    position_x = center_of_window_x
    position_y = center_of_window_y

    for i in range(1, len(path_points)):
        prev_point = path_points[i - 1]
        point = path_points[i]
        canvas.create_rectangle(position_x - size / 2, position_y - size / 2, position_x + size / 2, position_y + size / 2, fill='#ffc951', outline='white')

        prev_point_x, prev_point_y = prev_point.get_first_coordinate(), prev_point.get_second_coordinate()
        point_x, point_y = point.get_first_coordinate(), point.get_second_coordinate()
        diff_x = point_x - prev_point_x
        diff_y = point_y - prev_point_y

        position_x += diff_x * size
        position_y += diff_y * size

    return canvas
