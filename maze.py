from graphics import *
from cell import *
import random


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = []

        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        if self._win:
            self._draw_next_cell()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)

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
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0:
                if not self._cells[i-1][j].visited:
                    to_visit.append((i-1, j))
            if i < self._num_cols - 1:
                if not self._cells[i+1][j].visited:
                    to_visit.append((i+1, j))
            if j > 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append((i, j-1))
            if j < self._num_rows - 1:
                if not self._cells[i][j+1].visited:
                    to_visit.append((i, j+1))
            
            if not to_visit:
                return
            else:
                next_cell = random.choice(to_visit)
                if next_cell[1] < j:
                    #going up
                    self._cells[i][j].has_top_wall = False
                    self._cells[next_cell[0]][next_cell[1]].has_bottom_wall = False
                    if self._win:
                        self._win.delete_line(self._cells[i][j].id_top)
                        self._win.delete_line(self._cells[next_cell[0]][next_cell[1]].id_bottom)
                if next_cell[1] > j:
                    #going down
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[next_cell[0]][next_cell[1]].has_top_wall = False
                    if self._win:
                        self._win.delete_line(self._cells[i][j].id_bottom)
                        self._win.delete_line(self._cells[next_cell[0]][next_cell[1]].id_top)
                if next_cell[0] < i:
                    #going left
                    self._cells[i][j].has_left_wall = False
                    self._cells[next_cell[0]][next_cell[1]].has_right_wall = False
                    if self._win:
                        self._win.delete_line(self._cells[i][j].id_left)
                        self._win.delete_line(self._cells[next_cell[0]][next_cell[1]].id_right)
                if next_cell[0] > i:
                    #going right
                    self._cells[i][j].has_right_wall = False
                    self._cells[next_cell[0]][next_cell[1]].has_left_wall = False
                    if self._win:
                        self._win.delete_line(self._cells[i][j].id_right)
                        self._win.delete_line(self._cells[next_cell[0]][next_cell[1]].id_left)
                print(next_cell)
                print(f"top: {self._cells[next_cell[0]][next_cell[1]].has_top_wall}")
                print(f"bottom: {self._cells[next_cell[0]][next_cell[1]].has_bottom_wall}")
                print(f"left: {self._cells[next_cell[0]][next_cell[1]].has_left_wall}")
                print(f"right: {self._cells[next_cell[0]][next_cell[1]].has_right_wall}")
                self._break_walls_r(next_cell[0], next_cell[1])
                