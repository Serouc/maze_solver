from graphics import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)

    maze = Maze(10, 10, 10, 10, 50, 50, win)
    maze._create_cells()

    win.wait_for_close()
    

main()