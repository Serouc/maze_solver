from graphics import *

class Cell():
    def __init__(self, canvas = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = canvas

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        bottom_left = Point(self._x1, self._y2)
        top_left = Point(self._x1, self._y1)
        bottom_right = Point(self._x2, self._y2)
        top_right = Point(self._x2, self._y1)
        if self.has_left_wall:
            line = Line(top_left, bottom_left)
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(bottom_right, top_right)
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(top_left, top_right)
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        start_center = Point(
            self._x1 + (self._x2 - self._x1)/2, 
            self._y1 + (self._y2 - self._y1)/2
        )
        end_center = Point(
            to_cell._x1 + (to_cell._x2 - to_cell._x1)/2, 
            to_cell._y1 + (to_cell._y2 - to_cell._y1)/2
        )

        color = "red"
        if undo:
            color = "gray"
        
        line = Line(start_center, end_center)
        self._win.draw_line(line, color)