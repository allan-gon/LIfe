class Cell:
    """
    A cell is a container i built to more easily get at a squares position, aliveness, and
    neighbors for Conway's Game of Life
    """
    def __init__(self, x, y, alive):
        """
        Instantiates a Cell object
        :param x: int, x position on the window
        :param y: int, y position on the window
        :param alive: Boolean, whether or not a cell is alive during this state
        """
        self.x = x
        self.y = y
        self.currently_alive = alive
        self.neighbors = {}
        self.will_be_alive = None

    def live_or_die(self):
        """
        Figures out if the cell will eb alive in the next state
        :return:
        """
        alive_neighbors = 0
        for i in self.neighbors:
            if self.neighbors[i].currently_alive:
                alive_neighbors += 1
        if self.currently_alive and (alive_neighbors in [2, 3]):
            self.will_be_alive = True
        elif self.currently_alive and ((alive_neighbors < 2) or (alive_neighbors > 3)):
            self.will_be_alive = False
        elif not self.currently_alive and alive_neighbors == 3:
            self.will_be_alive = True
        return

    def update(self):
        """
        Changes currently alive to will be alive. So updates the cell's liveliness for the
        next state
        :return:
        """
        self.currently_alive = self.will_be_alive
        return
