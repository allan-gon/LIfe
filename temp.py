from my_class import Cell
from time import sleep
from random import choice
import pygame


def make_grid(win_x, win_y, size):
    """
    Create a multi-dimensional array full of instances off the Cell class
    :param win_x: desired window's x pixels
    :param win_y: desired window's y pixels
    :param size:
    :return: multi-dimensional array full of instances off the Cell class
    """
    rows = int(win_y / size)
    cols = int(win_x / size)
    grid = []
    for i in range(rows):
        temp_row = []
        for j in range(cols):
            temp_row.append(0)
        grid.append(temp_row)
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = Cell(i * size, j * size, choice([True, False]))
    return grid


def link(iterable):
    """
    Links up each cell with their neighbors
    :param iterable: a multi-dimensional array whose elements are only instances of the
    Cell class
    :return: Multi-dimensional array whose elements are only instances of the
    Cell class but each cell has their neighbors now
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
                    # print(f"Key: {k}, Value: {v}")
                    iterable[i][j].neighbors[k] = iterable[v[0]][v[-1]]
    return iterable


def main():
    # set constants
    width = 600
    height = 600
    size = 10
    white = (255, 255, 255)
    black = (0, 0, 0)
    # create grid
    grid = make_grid(width, height, size)
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
        surface.fill(black)
        win.update
        for row in grid:
            for cell in row:
                cell.live_or_die()
                if cell.currently_alive:
                    pygame.draw.rect(surface, white, (cell.x, cell.y, size, size), 1)
        win.update()
        for row in grid:
            for cell in row:
                cell.update()
        sleep(.2)
    return

if __name__ == "__main__":
    main()
