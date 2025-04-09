# Bryanna Wilson
# 4/9/2025
# P2HW1
# This program calculates and displays travel expenses with improved formatting.

# Prompt user for inputs
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas_expense = float(input("How much do you think you will spend on gas? "))
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
food_expense = float(input("Last, how much do you need for food? "))

# Calculate total expenses and remaining balance
total_expenses = gas_expense + accommodation_expense + food_expense
remaining_balance = budget - total_expenses

# Display results with formatted output
print("\n------------Travel Expenses------------")
print(f"Location:               {destination}")
print(f"Initial Budget:         ${budget:.2f}")
print(f"Fuel:                   ${gas_expense:.2f}")
print(f"Accommodation:          ${accommodation_expense:.2f}")
print(f"Food:                   ${food_expense:.2f}")
print("---------------------------------------")
print(f"Remaining Balance:      ${remaining_balance:.2f}")
