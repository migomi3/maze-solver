import time
from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
    
    def _create_cells(self):
        self._cells = []

        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self._win))

                self._draw_cell(i, j)
        
        self._break_entrance_and_exit()
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
    
        x = self._x1 + j * self._cell_size_x
        y = self._y1 + i * self._cell_size_y

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
