import plotly.graph_objects as go


def generation_plot(path):
    x_coords = [x.get_first_coordinate() for x in path]
    y_coords = [x.get_second_coordinate() for x in path]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_coords, y=y_coords, mode='markers'))
    fig.show()
