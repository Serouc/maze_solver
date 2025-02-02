from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("aMAZing")
        self.canvas = Canvas(self.__root, width = width, height = height)
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
            )

class Cell():
    def __init__(self, x1, y1, x2, y2, canvas):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = canvas
        self.center = Point(
            self._x1 + (self._x2 - self._x1)/2, 
            self._y1 + (self._y2 - self._y1)/2
        )
    
    def draw(self, color):
        bottom_left = Point(self._x1, self._y2)
        top_left = Point(self._x1, self._y1)
        bottom_right = Point(self._x2, self._y2)
        top_right = Point(self._x2, self._y1)
        if self.has_left_wall:
            Line(top_left, bottom_left).draw(self._win, color)
        if self.has_bottom_wall:
            Line(bottom_left, bottom_right).draw(self._win, color)
        if self.has_right_wall:
            Line(bottom_right, top_right).draw(self._win, color)
        if self.has_top_wall:
            Line(top_left, top_right).draw(self._win, color)
    
    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        Line(self.center, to_cell.center).draw(self._win, color)

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

    def _create_cells(self):
        self._cells = []
        x1 = self._x1
        y1 = self._y1
        for i in range(self._num_cols):
            col = []
            y2 = y1 + self._cell_size_y
            for i in range(self._num_rows):
                x2 = x1 + self._cell_size_x
                col.append(Cell(x1, y1, x2, y2, self._win))
                x1 = x2
            self._cells.append(col)
            x1 = self._x1
            y1 = y2

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