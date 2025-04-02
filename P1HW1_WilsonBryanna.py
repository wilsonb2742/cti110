# Bryanna Wilson
# 4/2/2025
# P1HW1 - Mathematical Expressions
# This program calculates the exponent of two user inputs and performs addition and subtraction with three user inputs.

# Step 1: Exponentiation calculation
print("-----Calculating Exponents-----")  # Title for exponentiation section

base = int(input("Enter an integer as the base value: "))  # User inputs base value
exponent = int(input("Enter an integer as the exponent: "))  # User inputs exponent value
result = base ** exponent  # Calculates base raised to exponent

# Displays result in correct format
print(str(base) + " raised to the power of " + str(exponent) + " is " + str(result) + " !!")

# Step 2: Addition and subtraction calculation
print("\n-----Addition and Subtraction-----\n")  # Title for addition/subtraction section

num1 = int(input("Enter a starting integer: "))  # First integer input
num2 = int(input("Enter an integer to add: "))  # Second integer input
num3 = int(input("Enter an integer to subtract: "))  # Third integer input

sum_result = num1 + num2  # Adds first two numbers
final_result = sum_result - num3  # Subtracts third number from sum

# Displays result in correct format
print(str(num1) + " + " + str(num2) + " - " + str(num3) + " equals " + str(final_result))