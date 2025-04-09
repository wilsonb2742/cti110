# Bryanna Wilson
# 4/9/2025
# P2LAB2 
# This program calculates the number of gallons of gas needed for a given car model based on its MPG and a user-defined number of miles.

# Create the dictionary with car models as keys and their MPG as values
car_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get all the keys (car models) from the dictionary
keys = car_mpg.keys()

# Print all car models (keys)
print("Available car models:")
for car in keys:
    print(car)

# Prompt the user to enter a car model from the dictionary
selected_car = input("\nEnter a car model from the list above: ")

# Check if the car model is in the dictionary
if selected_car in car_mpg:
    mpg = car_mpg[selected_car]  # Get the MPG of the selected car
    
    # Display the MPG for the car
    print(f"\nThe MPG for {selected_car} is {mpg} miles per gallon.")
    
    # Prompt the user to enter the number of miles they will drive
    miles = float(input("\nEnter the number of miles you will drive: "))
    
    # Calculate the gallons of gas needed
    gallons_needed = miles / mpg
    
    # Display the gallons of gas needed, rounded to two decimal places
    print(f"\nGallons of gas needed: {gallons_needed:.2f}")
else:
    print("\nError: The car model you entered is not in the list.")
