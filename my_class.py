class Cell:

    def __init__(self,x,y,alive):
        self.x = x
        self.y = y
        self.currently_alive = alive
        self.neighbors = {}
        self.will_be_alive = None

    def link(self,up=None,tr=None,right=None,br=None,down=None,bl=None,left=None,tl=None):
        self.neighbors['up'] = up
        self.neighbors['top right'] = tr
        self.neighbors['right'] = right
        self.neighbors['bottom right'] = br
        self.neighbors['down'] = down
        self.neighbors['bottom left'] = bl
        self.neighbors['left'] = left
        self.neighbors['top left'] = tl
        pass

    def live_or_die(self):
        alive_neighbors = 0
        for i in self.neighbors:
            if self.neighbors[i] != None:
                if self.neighbors[i].currently_alive:
                    alive_neighbors += 1
        if self.currently_alive and (alive_neighbors in [2,3]):
            self.will_be_alive = True
        elif self.currently_alive and (2 > alive_neighbors > 3):
            self.will_be_alive = False
        elif not self.currently_alive and alive_neighbors == 3:
            self.will_be_alive = True
        else:
            self.will_be_alive = False
        return

    def update(self):
        self.currently_alive = self.will_be_alive
        return