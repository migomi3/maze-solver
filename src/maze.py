import random
import time
from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        self._cells = []

        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self._win))

                self._draw_cell(i, j)
        
        
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
    
        x = self._x1 + i * self._cell_size_x
        y = self._y1 + j * self._cell_size_y

        self._cells[i][j].draw(x, x + self._cell_size_x, y, y + self._cell_size_y)

        self._animate()

    def _animate(self):
        if self._win is None:
            return
        
        self._win.redraw()
        time.sleep(.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False

        self._draw_cell(0, 0)
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def _break_walls_r(self, i, j):
        curr = self._cells[i][j]
        curr.visited = True

        while True:
            to_visit = []

            #right cell
            if i + 1 < self.num_cols and not self._cells[i+1][j].visited:
                to_visit.append((i + 1, j))
            
            #bottom cell
            if j + 1 < self.num_rows and not self._cells[i][j+1].visited:
                to_visit.append((i, j + 1))
            
            #left cell
            if i - 1 >= 0 and not self._cells[i-1][j].visited:
                to_visit.append((i - 1, j))
            
            #top cell
            if j - 1 >= 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j - 1))

            

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            next_indx = random.randrange(len(to_visit))
            next = to_visit.pop(next_indx)
            next_cell = self._cells[next[0]][next[1]]

            #right cell
            if next[0] == i + 1:
                curr.has_right_wall = False
                next_cell.has_left_wall = False
            
            #left cell
            if next[0] == i - 1:
                curr.has_left_wall = False
                next_cell.has_right_wall = False
            
            #bottom cell
            if next[1] == j + 1:
                curr.has_bottom_wall = False
                next_cell.has_top_wall = False

            #top cell
            if next[1] == j - 1:
                curr.has_top_wall = False
                next_cell.has_bottom_wall = False

            self._break_walls_r(next[0], next[1])

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False