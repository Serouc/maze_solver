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