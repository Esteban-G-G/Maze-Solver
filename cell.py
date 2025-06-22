from line import Line
from point import Point

class Cell:
    def __init__(self, win, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self._win = win

        self._top = Line(Point(x1, y1), Point(x2, y1))
        self._bottom = Line(Point(x1, y2), Point(x2, y2))
        self._left = Line(Point(x1, y1), Point(x1, y2))
        self._right = Line(Point(x2, y1), Point(x2, y2))

    def draw(self):
        if self._win is None:
            return
        
        color = "black"
        bg_color = "#d9d9d9"

        self._win.draw_line(self._top, color if self.has_top_wall else bg_color)
        self._win.draw_line(self._right, color if self.has_right_wall else bg_color)
        self._win.draw_line(self._left, color if self.has_left_wall else bg_color)
        self._win.draw_line(self._bottom, color if self.has_bottom_wall else bg_color)

    def draw_move(self, to_cell, undo = False):
        color = "purple" if undo else "red"
        x1 = (self._x1 + self._x2) // 2
        y1 = (self._y1 + self._y2) // 2
        x2 = (to_cell._x1 + to_cell._x2) // 2
        y2 = (to_cell._y1 + to_cell._y2) // 2

        self._win.draw_line(Line(Point(x1,y1), Point(x2,y2)), color)