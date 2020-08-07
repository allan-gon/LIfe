# What it does
Makes Conway's game of life with pygame

# How to use it
There is a single dependency, pygame so either pi install that
in the environment or use Pipenv and simply cd into the directory
where this repo is located call pip shell, pip update and it should
install dependencies for you *I think*

To actually see stuff happen run the demo.py file. So for example
in the terminal say python demo.py and you can see a random starting
state on Conway's Game of Life play out

# Known issues
If height > width it breaks.

If a non square so height != width the right most cells are just
always dead

So if altering the code make sure that width == height 