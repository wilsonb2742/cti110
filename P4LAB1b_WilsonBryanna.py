# Wilson
# 4/30/25
# P4LAB1b
# This program uses turtle graphics to draw my initials (BW) using lines.

import turtle

# Set up turtle
t = turtle.Turtle()
t.pensize(5)
t.color("purple")
t.speed(2)

# Draw 'B'
t.penup()
t.goto(-100, 0)
t.pendown()
t.left(90)
t.forward(100)
t.right(90)
t.circle(-25, 180)
t.left(180)
t.circle(-25, 180)

# Draw 'W'
t.penup()
t.goto(50, 100)     # Starting point (top-left of W)
t.pendown()
t.goto(65, 0)       # Down-right to first valley
t.goto(80, 100)     # Up-right to middle peak
t.goto(95, 0)       # Down-right to second valley
t.goto(110, 100)    # Up-right to end        

# Finish
turtle.done()
