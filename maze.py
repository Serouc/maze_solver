from graphics import *

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