#!/usr/bin/python3
from graphics import Line, Point, Window


def main():
    win = Window(800, 600)
    p1 = Point(30, 200)
    p2 = Point(800, 60)
    line = Line(p1, p2)
    win.draw_line(line, "Red")
    win.wait_for_close()


main()