from graphics import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)
    '''
    box = Cell(win)
    box.draw(0, 0, 100, 100)
    box2 = Cell(win)
    box2.draw(100, 100, 200, 200)
    box.draw_move(box2, True)
    '''
    maze = Maze(0, 0, 10, 10, 50, 50, win)
    maze._create_cells()

    win.wait_for_close()
    

main()