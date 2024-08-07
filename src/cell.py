from graphics import Line, Point


class Cell:
    def __init__(self, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, x2, y1, y2, f_color="White"):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        #top-left to bottom-left clockwise
        p1 = Point(self._x1, self._y1)
        p2 = Point(self._x2, self._y1)
        p3 = Point(self._x2, self._y2)
        p4 = Point(self._x1, self._y2)

        if self.has_left_wall:
            l = Line(p1, p4)
            self._win.draw_line(l, f_color)
        
        if self.has_top_wall:
            l = Line(p1, p2)
            self._win.draw_line(l, f_color)
        
        if self.has_right_wall:
            l = Line(p2, p3)
            self._win.draw_line(l, f_color)
        
        if self.has_bottom_wall:
            l = Line(p4, p3)
            self._win.draw_line(l, f_color)
        
    def draw_move(self, to_cell, undo=False):
        x1 = (self._x1 + self._x2) / 2
        y1 = (self._y1 + self._y2) / 2
        x2 = (to_cell._x1 + to_cell._x2) / 2
        y2 = (to_cell._y1 + to_cell._y2) / 2
        
        start_point = Point(x1, y1)
        end_point = Point(x2, y2)

        path = Line(start_point, end_point)
        
        color = "red"

        if undo:
            color = "gray"

        self._win.draw_line(path, color)