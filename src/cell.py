from graphics import Line, Point


class Cell:
    def __init__(self, x1, x2, y1, y2, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
    
    def draw(self, f_color):
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