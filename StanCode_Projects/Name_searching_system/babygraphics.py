"""
File: babygraphics.py
Name: Andy Chi
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900,1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue', 'magenta']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coord = int(width / len(YEARS)) * int(year_index)
    return x_coord


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i),
                           0,
                           GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i),
                           CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i) + TEXT_DX,
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # Test Code: ``python3 babygraphics.py``

    # Create a x dis, y dis and y coordinate when rank is out of 1000
    dis_x = int((CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) / len(YEARS))
    dis_y = float((CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK)
    lowest_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

    # Nested for loop for each year and name
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        for j in range(len(YEARS) - 1):
            # Create a name rank and assign 1001 if name is ranked over 1000
            yr = YEARS[j]
            if str(yr) in name_data[name]:
                name_rank = int(name_data[name][str(yr)])
            else:
                name_rank = 1001
            # Create a next year name rank and assign 1001 if next year's name is ranked over 1000
            next_yr = YEARS[j + 1]
            if str(next_yr) in name_data[name]:
                next_yr_rank = int(name_data[name][str(next_yr)])
            else:
                next_yr_rank = 1001

            # Four ranking combinations
            # Use COLORS[i % len(COLORS)] to loop colors

            if name_rank > 1000 and next_yr_rank < 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * dis_x, lowest_y, GRAPH_MARGIN_SIZE + (j + 1) * dis_x,
                                   GRAPH_MARGIN_SIZE + next_yr_rank * dis_y, fill=COLORS[i % len(COLORS)],
                                   width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * dis_x, lowest_y, text=name + '*',
                                   fill=COLORS[i % len(COLORS)], anchor=tkinter.SW)

            elif name_rank > 1000 and next_yr_rank > 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * dis_x, lowest_y, GRAPH_MARGIN_SIZE + (j + 1) * dis_x,
                                   lowest_y, fill=COLORS[i % len(COLORS)], width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * dis_x, lowest_y, text=name + '*',
                                   fill=COLORS[i % len(COLORS)], anchor=tkinter.SW)

            elif name_rank < 1000 and next_yr_rank > 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * dis_x, GRAPH_MARGIN_SIZE + name_rank * dis_y,
                                   GRAPH_MARGIN_SIZE + (j + 1) * dis_x, lowest_y, fill=COLORS[i % len(COLORS)],
                                   width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + j * dis_x + TEXT_DX, GRAPH_MARGIN_SIZE + name_rank * dis_y,
                                   text=str(name) + str(name_rank), fill=COLORS[i % len(COLORS)], anchor=tkinter.SW)

            else:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * dis_x, GRAPH_MARGIN_SIZE + name_rank * dis_y,
                                   GRAPH_MARGIN_SIZE + (j + 1) * dis_x, GRAPH_MARGIN_SIZE + next_yr_rank * dis_y,
                                   fill=COLORS[i % len(COLORS)], width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + j * dis_x + TEXT_DX, GRAPH_MARGIN_SIZE + name_rank * dis_y,
                                   text=str(name) + str(name_rank), fill=COLORS[i % len(COLORS)], anchor=tkinter.SW)
        # Last rank
        if next_yr_rank > 1000:
            canvas.create_text(GRAPH_MARGIN_SIZE + (len(YEARS) - 1) * dis_x + TEXT_DX, lowest_y, text=str(name) + '*',
                               fill=COLORS[i % len(COLORS)], anchor=tkinter.SW)
        else:
            canvas.create_text(GRAPH_MARGIN_SIZE + (len(YEARS) - 1) * dis_x + TEXT_DX,
                               GRAPH_MARGIN_SIZE + next_yr_rank * dis_y,
                               text=str(name) + str(next_yr_rank), fill=COLORS[i % len(COLORS)], anchor=tkinter.SW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
