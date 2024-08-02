#!/usr/bin/python3
from cell import Cell
from graphics import *


def main():
    win = Window(800, 600)

    cell1 = Cell(500, 550, 500, 550, win)
    cell2 = Cell(70, 80, 70, 80, win, has_left_wall=False, has_right_wall=False)
    cell3 = Cell(20, 30, 20, 30, win, has_top_wall=False, has_bottom_wall=False)
    cell4 = Cell(70, 80, 90, 100, win, has_right_wall=False, has_top_wall=False)
    
    cell1.draw("white")
    cell2.draw("white")
    cell3.draw("white")
    cell4.draw("White")

    cell1.draw_move(cell4)
    cell2.draw_move(cell3, True)

    win.wait_for_close()


main()