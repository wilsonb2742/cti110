# Bryanna Wilson
# 4/9/2025
# P2LAB1 - Circle Calculations
# This program calculates and displays the diameter, circumference, and area of a circle based on the radius entered by the user.

import math

# Get the radius from the user
radius = float(input("What is the radius of the circle? "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display results with appropriate formatting
print("\nCircle Calculations:")
print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")
