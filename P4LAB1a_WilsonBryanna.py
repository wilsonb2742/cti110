# Wilson
# 4/30/25
# P4LAB1a
# This program uses turtle graphics to draw a square and a triangle using loops.

import turtle

# Set up turtle
t = turtle.Turtle()
t.pensize(2)
t.speed(2)

# Draw square using a for loop
for _ in range(4):
    t.forward(100)
    t.left(90)

# Move to a different position for the triangle
t.penup()
t.goto(-50, -85)
t.pendown()

# Draw triangle using a while loop
sides = 0
while sides < 3:
    t.forward(100)
    t.left(120)
    sides += 1

# Keep window open
turtle.done()
