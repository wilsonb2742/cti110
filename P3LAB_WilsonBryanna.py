# P3LAB
# Wilson
# 4/23/2025
# This program takes a float amount in dollars and calculates the most efficient combination of dollars, quarters, dimes, nickels, and pennies.

# Get the amount of money from the user
amount = float(input("Enter a money amount: $ "))

# Convert to cents (integer)
cents = int(round(amount * 100))

if cents == 0:
    print("No change")
else:
    # Dictionary to store coin names and their values in cents
    coins = {
        "dollar": 100,
        "quarter": 25,
        "dime": 10,
        "nickel": 5,
        "penny": 1
    }

 # Loop through each coin and calculate how many of each is needed
    for coin_name, coin_value in coins.items():
        count = cents // coin_value
        cents %= coin_value  # Get the remaining cents after this coin

        if count == 1:
            print(f"{count} {coin_name}")
        elif count > 1:
            # Make 'penny' plural as 'pennies', not 'pennys'
            if coin_name == "penny":
                print(f"{count} pennies")
            else:
                print(f"{count} {coin_name}s")
