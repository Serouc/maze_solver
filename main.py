from graphics import *
from cell import *
from maze import *

def main():
    sc_height = input("Enter screen height:")
    sc_width = input("Enter sc_width:")
    cols = input("Enter number of columns:")
    rows = input("Enter number of rows:")
    win = Window(800, 600)
    maze = Maze(1, 1, 10, 10, 50, 50, win)
    win.set_draw_command(maze.start_drawing)
    win.set_solve_command(maze.solve)
    win.wait_for_close()
    

main()