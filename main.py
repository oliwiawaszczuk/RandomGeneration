import numpy as np
import plotly.graph_objects as go
from Path import create_path

if __name__ == '__main__':
    path1 = create_path(5444, 10)

    x_coords = [x.get_first_coordinate() for x in path1]
    y_coords = [x.get_second_coordinate() for x in path1]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x_coords, y=y_coords, mode='markers'))

    fig.show()
