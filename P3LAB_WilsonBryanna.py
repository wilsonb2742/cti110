# P3LAB
# Wilson
# 4/23/2025
# This program takes a float amount in dollars and calculates the most efficient combination of dollars, quarters, dimes, nickels, and pennies.

amount = float(input("Enter a money amount: $ "))
cents = int(round(amount * 100))

if cents == 0:
    print("No change")
else:
    dollars = cents // 100
    cents = cents % 100
    if dollars == 1:
        print("1 dollar")
    elif dollars > 1:
        print(f"{dollars} dollars")

    quarters = cents // 25
    cents = cents % 25
    if quarters == 1:
        print("1 quarter")
    elif quarters > 1:
        print(f"{quarters} quarters")

    dimes = cents // 10
    cents = cents % 10
    if dimes == 1:
        print("1 dime")
    elif dimes > 1:
        print(f"{dimes} dimes")

    nickels = cents // 5
    cents = cents % 5
    if nickels == 1:
        print("1 nickel")
    elif nickels > 1:
        print(f"{nickels} nickels")

    pennies = cents
    if pennies == 1:
        print("1 penny")
    elif pennies > 1:
        print(f"{pennies} pennies")

