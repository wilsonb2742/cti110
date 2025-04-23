#Bryanna Wilson
#4/23/2025
#P3HW2
#This project is a payroll calculator that takes employee details, calculates pays, and displays a formatted summary of total compensation.

"""
Pseudocode:
-----------
1. Ask the user to enter the employee's name.
2. Ask the user to enter number of hours the employee worked this week.
3. Ask the user to enter employee's pay rate.
4. Check if the hours worked are more than 40.
5. If hours worked > 40:
    - Calculate overtime hours = hours worked - 40
    - Calculate overtime pay = overtime hours * (pay rate * 1.5)
    - Regular hours = 40
   Else:
    - Overtime hours = 0
    - Overtime pay = 0
    - Regular hours = hours worked
6. Calculate pay for regular hours = regular hours * pay rate
7. Calculate gross pay = regular pay + overtime pay
8. Display the results:
    - Employee name
    - Hours worked
    - Pay rate
    - Overtime hours
    - Overtime pay
    - Pay for regular hours
    - Gross pay
"""

# Get input from user
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Initialize overtime variables
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_hours = 40
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_hours = hours_worked

# Calculate regular and gross pay
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Output
print("---------------------------------------------")
print(f"Employee name: {employee_name}")
print() 
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'Overtime':<10}{'Overtime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
print("--------------------------------------------------------------------------------")
print(f"{hours_worked:<15.2f}{pay_rate:<10.2f}{overtime_hours:<10.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<10.2f}")
