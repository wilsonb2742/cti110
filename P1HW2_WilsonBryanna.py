# Bryanna Wilson
# 4/2/2025
# P1HW2 - Budget Travel Program
# This program calculates the remaining budget after expenses for a trip based on user inputs.

# Pseudocode:
# 1. Ask the user to input their budget.
# 2. Ask the user to input the travel destination.
# 3. Ask the user to input the amount they will spend on gas.
# 4. Ask the user to input the amount they will spend on accommodation.
# 5. Ask the user to input the amount they will spend on food.
# 6. Add the expenses (gas, accommodation, and food).
# 7. Subtract the total expenses from the budget.
# 8. Display the results with the destination and remaining budget.

# Step 3: Ask user for their budget
budget = float(input("Enter your budget: $"))

# Step 4: Ask user for travel destination
destination = input("Enter your travel destination: ")

# Step 5: Ask user for amount they will spend on gas
gas_expense = float(input("Enter amount to spend on gas: $"))

# Step 6: Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Enter amount to spend on accommodation: $"))

# Step 7: Ask user for amount they will spend on food
food_expense = float(input("Enter amount to spend on food: $"))

# Step 8: Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Step 9: Subtract expenses from budget
remaining_budget = budget - total_expenses

# Step 10: Display results
print("\n------ Trip Budget Summary ------")
print(f"Travel Destination: {destination}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
