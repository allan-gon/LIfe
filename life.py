import pygame, sys, time
from pygame.locals import *
from my_class import Cell

# x = int(input('How many blocks left to right?\n'))
# y = int(input("How many blocks vertically?\n"))

SIZE = 50

# row 1
one = Cell(400,400,False)
two = Cell(450,400,True)
three = Cell(500,400,False)
# row 2
four = Cell(400,450,False)
five = Cell(450,450,True)
six = Cell(500,450,False)
# row 3
seven = Cell(400,500,False)
eight = Cell(450,500,True)
nine = Cell(500,500,False)

# manually link them up
one.link(right=two,down=four,br=five)
two.link(right=three,br=six,down=five,bl=four,left=one)
three.link(down=six,bl=five,left=two)
four.link(up=one,tr=two,right=five,br=eight,down=seven)
five.link(up=two,tr=three,right=six,br=nine,down=eight,bl=seven,left=four,tl=one)
six.link(up=three,down=nine,bl=eight,left=five,tl=two)
seven.link(up=four,tr=five,right=eight)
eight.link(up=five,tr=six,right=nine,left=seven,tl=four)
nine.link(up=six,left=eight,tl=five)

cells = [
    [one,two,three],
    [four,five,six],
    [seven,eight,nine]
]

pygame.init()

win = pygame.display
surface = win.set_mode((1000,1000))

BLACK=(0,0,0)
BLUE=(0,0,255)

run = True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    # reset the screen
    surface.fill(BLACK)
    win.update()
    # pause
    time.sleep(.1)
    # draw
    for row in cells:
        for cell in row:
            if cell.will_be_alive == True:
                pygame.draw.rect(surface,BLUE,(cell.x,cell.y,SIZE,SIZE),3)
            # check who's alive
            cell.live_or_die()
    for row in cells:
        for cell in row:
            cell.update()
    win.update()
    # pause
    time.sleep(.1)