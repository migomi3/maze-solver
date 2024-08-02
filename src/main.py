#!/usr/bin/python3
from cell import Cell
from graphics import *


def main():
    win = Window(800, 600)

    cell1 = Cell(50, 60, 50, 60, win)
    cell2 = Cell(70, 80, 70, 80, win, has_left_wall=False, has_right_wall=False)
    cell3 = Cell(20, 30, 20, 30, win, has_top_wall=False, has_bottom_wall=False)
    cell4 = Cell(70, 80, 90, 100, win, has_right_wall=False, has_top_wall=False)
    
    cell1.draw("Red")
    cell2.draw("Blue")
    cell3.draw("Green")
    cell4.draw("White")

    win.wait_for_close()


main()