from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze
    
def main():
    win = Window(800, 600)

    #defining points
    p1 = Point(100, 100)
    p2 = Point(300, 100)
    p3 = Point(300, 300)
    p4 = Point(100, 300)

    # defining lines
    top = Line(p1,p2)
    right = Line(p2, p3)
    bottom = Line(p3, p4)
    left = Line(p4, p1)

    #draw a rectangle
    win.draw_line(top, "red")
    win.draw_line(right, "green")
    win.draw_line(bottom, "blue")
    win.draw_line(left, "black")

    # Draw four different cell variations
    c1 = Cell(win, 100, 100, 150, 150)
    c2 = Cell(win, 160, 100, 210, 150)
    c3 = Cell(win, 100, 160, 150, 210)
    c4 = Cell(win, 160, 160, 210, 210)

    # Kock out a few walls
    c2.has_left_wall = False
    c3.has_top_wall = False
    c4.has_right_wall = False
    c4.has_bottom_wall = False

    c1.draw()
    c2.draw()
    c3.draw()
    c4.draw()

    c1.draw_move(c2)
    c2.draw_move(c1, undo=True)

    maze = Maze(50,50,10,10,40,40, win)
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()