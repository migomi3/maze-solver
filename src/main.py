#!/usr/bin/python3
from cell import Cell
from graphics import *
from maze import Maze


def main():
    num_rows = 16
    num_cols = 12
    margin = 20
    screen_x = 800
    screen_y = 600

    win = Window(800, 600)
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()


main()