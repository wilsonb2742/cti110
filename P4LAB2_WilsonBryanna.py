# Wilson
# 4/30/25
# P4LAB2
# This program displays a multiplication table for non-negative integers and repeats based on user input.

run_again = "yes"

while run_again.lower() == "yes":
    number = int(input("Enter a non-negative integer: "))
    
    if number < 0:
        print("This program does not handle negative numbers")
    else:
        print(f"\nMultiplication table for {number}:\n")
        for i in range(1, 13):  # For loop for 1 to 12
            print(f"{number} x {i} = {number * i}")

    print()  # Line break for clarity
    run_again = input("Would you like to run the program again? (yes/no): ")

print("Exiting program...")
