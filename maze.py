from graphics import *
from cell import *
import random
import time


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None, speed_mod = 1):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._speed_mod = speed_mod
        if seed:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = []

        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                x1 = self._x1 + (i * self._cell_size_x)
                y1 = self._y1 + (j * self._cell_size_y)
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                col.append(Cell(x1, y1, x2, y2, self._win))
            self._cells.append(col)

    def start_drawing(self):
        if self._win:
            self._draw_next_cell()
        if self._cells:
            self._break_entrance_and_exit()
            self._break_walls(0,0)

    def _draw_next_cell(self, i=0, j=0):
        if i < len(self._cells):
            self._draw_cell(i, j)
            if j + 1 < len(self._cells[i]):
                self._win.delay(int(750/self._speed_mod), lambda: self._draw_next_cell(i, j+1))
            else:
                if i + 1 < len(self._cells):
                    self._win.delay(int(750/self._speed_mod), lambda: self._draw_next_cell(i+1, 0))
                else:
                    # Enable the solve button when maze is fully drawn
                    self._win._solve_button.config(state="normal")
        

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()

    def _break_entrance_and_exit(self):
        if not self._cells:
            return

        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        
        if self._win:
            self._win.delete_line(self._cells[0][0].id_top)
            self._win.delete_line(self._cells[-1][-1].id_bottom)
    
    def _break_walls(self, start_i, start_j):
        stack = [(start_i, start_j)]
        self._cells[start_i][start_j].visited = True
        while stack:
            i, j = stack[-1]

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
                stack.pop()
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
                self._cells[next_cell[0]][next_cell[1]].visited = True
                stack.append(next_cell)
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        self._reset_cells_visited()
        self._stack = [(0, 0)]
        self._cells[0][0].visited = True
        return self._solve_step()

    def _solve_step(self):
        if not self._stack:
            return False

        i, j = self._stack[-1]
        to_visit = []
        if i == self._num_cols - 1 and j == self._num_rows -1:
            self._stack = []
            return True
        
        if i > 0:
            if not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
        if i < self._num_cols - 1:
            if not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
        if j > 0:
            if not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
        if j < self._num_rows - 1:
            if not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
        
        if not to_visit:
            current = self._stack.pop()
            if self._stack:
                prev = self._stack[-1]
                self._cells[prev[0]][prev[1]].draw_move(self._cells[current[0]][current[1]], undo=True)
        else:
            weights = []
            for move in to_visit:
                x, y = move
                distance_to_goal = abs(x - (self._num_cols-1)) + abs(y - (self._num_rows-1))
                weight = 1.0 / (distance_to_goal + 1)
                weights.append(weight)
            next_cell = random.choices(to_visit, weights=weights, k=1)[0]
            self._cells[i][j].draw_move(self._cells[next_cell[0]][next_cell[1]])
            self._cells[next_cell[0]][next_cell[1]].visited = True
            self._stack.append(next_cell)

        return self._win.delay(int(1500/self._speed_mod), self._solve_step)