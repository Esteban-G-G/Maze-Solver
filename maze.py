from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self._x1 = x1
        self._y1 = y1
        self._rows = num_rows
        self._cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self.__cells = []

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for col in range (self._cols):
            col_cells = []
            for row in range (self._rows):
                x1 = self._x1 + col * self._cell_size_x
                y1 = self._y1 + row * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y

                cell = Cell(self._win, x1, y1, x2, y2)
                col_cells.append(cell)
            self.__cells.append(col_cells)

        for col in range(self._cols):
            for row in range(self._rows):
                self.__draw_cell(col, row)

    def __draw_cell(self, i, j):
        cell = self.__cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.05)
    
    def __break_entrance_and_exit(self):
        #entrance has top left cell
        entrance = self.__cells[0][0]
        entrance.has_top_wall = False
        self.__draw_cell(0,0)

        #exit bottom right cell
        exit_cell = self.__cells[self._cols - 1][self._rows - 1]
        exit_cell.has_bottom_wall = False
        self.__draw_cell(self._cols -1, self._rows -1)

    def __reset_cells_visited(self):
        for col in self.__cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self.__solve_r(0,0)
    
    def __solve_r(self, i, j):
        self._animate()

        current = self.__cells[i][j]
        current.visited = True

        if i == self._cols - 1 and j == self._rows -1:
            return True
        
        directions = [
            (-1, 0, "left", "has_left_wall"),
            (1, 0, "right", "has_right_wall"),
            (0, -1, "up", "has_top_wall"),
            (0,1, "down", "has_bottom_wall"),
        ]

        for di, dj, _, wall_attr in directions:
            ni,nj = i + di, j + dj
            if 0 <= ni < self._cols and 0 <= nj < self._rows:
                neighbor = self.__cells[ni][nj]
                if not getattr(current, wall_attr) and not neighbor.visited:
                    current.draw_move(neighbor)
                    if self.__solve_r(ni, nj):
                        return True
                    current.draw_move(neighbor, undo = True)
        return False

    