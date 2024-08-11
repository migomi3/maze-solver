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
    
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()

        curr = self._cells[i][j]
        curr.visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        left_cell = None
        right_cell = None
        top_cell = None
        bottom_cell = None

        if i - 1 >= 0:
            left_cell = self._cells[i-1][j]
        if i + 1 < self.num_cols:
            right_cell = self._cells[i+1][j]
        if j - 1 >= 0:
            top_cell = self._cells[i][j-1]
        if j + 1  < self.num_rows:
            bottom_cell = self._cells[i][j+1]

        if left_cell is not None and not curr.has_left_wall and not left_cell.has_right_wall and not left_cell.visited:
            curr.draw_move(left_cell)
            result = self._solve_r(i-1, j)
            if result:
                return result
            else:
                curr.draw_move(left_cell, undo=True)
        
        if right_cell is not None and not curr.has_right_wall and not right_cell.has_left_wall and not right_cell.visited:
            curr.draw_move(right_cell)
            result = self._solve_r(i+1, j)
            if result:
                return result
            else:
                curr.draw_move(right_cell, undo=True)
        
        if top_cell is not None and not curr.has_top_wall and not top_cell.has_bottom_wall and not top_cell.visited:
            curr.draw_move(top_cell)
            result = self._solve_r(i, j-1)
            if result:
                return result
            else:
                curr.draw_move(top_cell, undo=True)

        if bottom_cell is not None and not curr.has_bottom_wall and not bottom_cell.has_top_wall and not bottom_cell.visited:
            curr.draw_move(bottom_cell)
            result = self._solve_r(i, j+1)
            if result:
                return result
            else:
                curr.draw_move(bottom_cell, undo=True)

        return False