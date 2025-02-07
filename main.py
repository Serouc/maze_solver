from graphics import *
from cell import *
from maze import *

def main():
    sc_width = int(input("Enter window width: "))
    sc_height = int(input("Enter window height: "))
    cols = int(input("Enter number of columns: "))
    rows = int(input("Enter number of rows: "))
    margin = 10
    draw_speed_modifier = (cols+rows)
    win = Window(sc_width, sc_height)
    maze = Maze(margin, margin, cols, rows, ((sc_width - 2*margin)/rows), ((sc_height - 2*margin)/cols), win, speed_mod = draw_speed_modifier)
    win.set_draw_command(maze.start_drawing)
    win.set_solve_command(maze.solve)
    win.wait_for_close()
    

main()