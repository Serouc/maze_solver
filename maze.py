from graphics import *
from cell import *
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = []

        for i in range(self._num_cols):
            col = []
            for i in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        if self._win:
            self._draw_next_cell()
        self._break_entrance_and_exit()

    def _draw_next_cell(self, i=0, j=0):
        if i < len(self._cells):
            self._draw_cell(i, j)
            if j + 1 < len(self._cells[i]):
                self._win.delay(50, lambda: self._draw_next_cell(i, j+1))
            else:
                self._win.delay(50, lambda: self._draw_next_cell(i+1, 0))
        

    def _draw_cell(self, i, j):
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)

    def _break_entrance_and_exit(self):
        if not self._cells:
            return

        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        
        if self._win:
            self._win.delete_line(self._cells[0][0].id_top)
            self._win.delete_line(self._cells[-1][-1].id_bottom)
