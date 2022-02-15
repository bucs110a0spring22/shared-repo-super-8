"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()
t.shape('turtle')
sides = 6

for i in range(sides):
    t.forward(75)
    t.left(360/sides)

