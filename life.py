from my_class import Cell
from random import choice
import pygame


def make_grid(win_x, win_y, size):
    """
    Create a multi-dimensional LIST full of Cell instances
    :param win_x: desired window's x pixels
    :param win_y: desired window's y pixels
    :param size: the size of each cell
    :return: multi-dimensional LIST full of Cell instances
    """
    cols = win_y // size
    rows = win_x // size
    grid = []
    # making rows and cols in list because np arrays didn't like objects
    for i in range(rows):
        temp_row = []
        for j in range(cols):
            temp_row.append(0)
        grid.append(temp_row)
    # replacing the garbage i put in the list to make it with actual cell instances
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = Cell(i * size, j * size, choice([True, False]))
    return grid


def link(iterable):
    """
    Gives each instance a neighbor attribute which is a dictionary that contains all
    the neighbors. Really proud of making it so that it doesn't freak out because the edge
    cells don't have certain neighbors
    :param iterable: a multi-dimensional LIST whose elements are only instances of the
    Cell class
    :return: Multi-dimensional LIST whose elements are only instances of the
    Cell class but each cell NOW has a neighbor attribute which is a dictionary containing
    you guessed it all their neighboors
    """

    for i in range(len(iterable)):
        for j in range(len(iterable[i])):
            row_above = i - 1
            same_row = i
            row_below = i + 1

            right_col = j + 1
            same_col = j
            left_col = j - 1

            neighbors = {
                'top': [row_above, same_col],
                'top right': [row_above, right_col],
                'right': [same_row, right_col],
                'bottom right': [row_below, right_col],
                'bottom': [row_below, same_col],
                'bottom left': [row_below, left_col],
                'left': [same_row, left_col],
                'top left': [row_above, left_col]
            }
            for k, v in neighbors.items():
                if any(_ < 0 for _ in v) or any(_ >= len(iterable[0]) for _ in v):
                    pass
                else:
                    iterable[i][j].neighbors[k] = iterable[v[0]][v[-1]]
    return iterable


def main(width=800, height=800):
    """
    Draws the window and cells
    :return: game window to watch Conway's game of life happen
    """
    # set constants
    width = width
    height = height
    size = 10
    white = (255, 255, 255)
    black = (0, 0, 0)
    # create grid
    grid = make_grid(width, height, size)
    # debugging
    print(f"Rows: {len(grid)}, Cols: {len(grid[0])}")
    # init  game and make window
    pygame.init()
    win = pygame.display
    surface = win.set_mode((width, height))
    # link cells
    grid = link(grid)
    # Game  Loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # makes black background
        surface.fill(black)
        # for each cell if alive draw it
        for row in grid:
            for cell in row:
                cell.live_or_die()
                if cell.currently_alive:
                    pygame.draw.rect(surface, white, (cell.x, cell.y, size, size), 1)
        # update the screen
        win.update()
        # for each cell update the state
        # had to do this separately because each cells state is dependent on it's neighbors
        for row in grid:
            for cell in row:
                cell.update()
    return


if __name__ == "__main__":
    main()
