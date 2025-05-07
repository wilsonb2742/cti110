# Wilson Bryanna
# 5/7/2025
# P5LAB
# This program acts like a self-checkout, calculating the change due and displaying the coin breakdown.

import random

def disperse_change(change):
    """Takes a float value and prints out the coin breakdown to return the correct change."""
    print(f"Change is: ${change:.2f}")  # state the change amount

    cents = round(change * 100)  # convert dollars to cents to avoid rounding errors

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    if dollars: print(f"Dollars: {dollars}")
    if quarters: print(f"Quarters: {quarters}")
    if dimes: print(f"Dimes: {dimes}")
    if nickels: print(f"Nickels: {nickels}")
    if pennies: print(f"Pennies: {pennies}")

def main():
    # Generate amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed}")

    # Get user input
    while True:
        try:
            cash_given = float(input("How much cash will you put in the self-checkout? "))
            if cash_given < amount_owed:
                print("That's not enough money. Please enter an amount equal to or greater than what you owe.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Calculate change
    change = round(cash_given - amount_owed, 2)

    # Display the change
    disperse_change(change)

# Call the main function
main()
