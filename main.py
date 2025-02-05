from graphics import *

def main():
    win = Window(800, 600)
    Cell(0, 0, 50, 50, win.canvas).draw("green")
    Cell(50, 50, 100, 100, win.canvas).draw("green")
    big_box = Cell(100, 100, 200, 200, win.canvas)
    big_box.has_bottom_wall = False
    big_box.draw("red")
    big_box2 = Cell(200, 200, 300, 300, win.canvas)
    big_box2.has_right_wall = False
    big_box2.draw("purple")
    big_box.draw_move(big_box2, undo = True)
    win.wait_for_close()

main()