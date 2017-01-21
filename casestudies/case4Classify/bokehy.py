from bokeh.models import HoverTool, ColumnDataSource
from bokeh.io import output_file
from bokeh.plotting import figure, show
import numpy as np


def bokeh_test():
    # Let's plot a simple 5x5 grid of squares, alternating in color as red and blue.
    plot_values = [1, 2, 3, 4, 5]
    plot_colors = ["red", "blue"]
    # How do we tell Bokeh to plot each point in a grid?  Let's use a function that
    # finds each combination of values from 1-5.
    from itertools import product
    grid = list(product(plot_values, plot_values))
    print(grid)
    # The first value is the x coordinate, and the second value is the y coordinate.
    # Let's store these in separate lists.
    xs, ys = zip(*grid)
    print(xs)
    print(ys)
    # Now we will make a list of colors, alternating between red and blue.
    colors = [plot_colors[i % 2] for i in range(len(grid))]
    print(colors)
    # Finally, let's determine the strength of transparency (alpha) for each point,
    # where 0 is completely transparent.
    alphas = np.linspace(0, 1, len(grid))
    # Bokeh likes each of these to be stored in a special dataframe, called
    # ColumnDataSource.  Let's store our coordinates, colors, and alpha values.
    source = ColumnDataSource(
        data={
            "x": xs,
            "y": ys,
            "colors": colors,
            "alphas": alphas,
        }
    )
    # We are ready to make our interactive Bokeh plot!
    output_file("Basic_Example.html", title="Basic Example")
    fig = figure(tools="resize, hover, save")
    fig.rect("x", "y", 0.9, 0.9, source=source, color="colors", alpha="alphas")
    hover = fig.select(dict(type=HoverTool))
    hover.tooltips = {
        "Value": "@x, @y",
    }
    show(fig)



def colors_define():
    cluster_colors = ["red", "orange", "green", "blue", "purple", "gray"]
    regions = ["Speyside", "Highlands", "Lowlands", "Islands", "Campbelltown", "Islay"]

    region_colors =  1## ENTER CODE HERE! ##

if __name__ == '__main__':
    # bokeh_test()
    colors_define()
