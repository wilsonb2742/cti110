# Wilson
# 4/30/25
# P4HW2
# Description: This program calculates gross pay for multiple employees.
# It continues to prompt for employee information until "Done" is entered,
# calculates regular and overtime pay, and displays a summary table per employee.
# At the end, it also shows totals for all employees.

'''
Pseudocode:
1. Initialize totals: total_overtime_pay, total_regular_pay, total_gross_pay, employee_count = 0
2. Prompt for first employee name
3. While name is not "Done":
    a. Ask for hours worked and pay rate
    b. Calculate overtime and regular pay
    c. Calculate gross pay
    d. Print breakdown
    e. Update totals
    f. Prompt for next name
4. After loop, print totals
'''

# Totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# First prompt
employee_name = input('Enter employee\'s name or "Done" to terminate: ')

while employee_name.lower() != "done":
    hours_worked = float(input(f'How many hours did {employee_name} work? '))
    pay_rate = float(input(f'What is {employee_name}\'s pay rate? '))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    print(f'\nEmployee name: {employee_name}\n')
    print("Hours Worked   Pay Rate    Overtime   Overtime Pay    RegHour Pay    Gross Pay")
    print("-------------------------------------------------------------------------------")
    print(f"{hours_worked:<14.2f}{pay_rate:<11.2f}{overtime_hours:<11.2f}"
          f"{overtime_pay:<15.2f}{regular_pay:<14.2f}{gross_pay:<.2f}\n")

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Ask for next employee
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# After loop
print(f'\nTotal number of employees entered: {employee_count}')
print(f'Total amount paid for overtime: ${total_overtime_pay:.2f}')
print(f'Total amount paid for regular hours: ${total_regular_pay:.2f}')
print(f'Total amount paid in gross: ${total_gross_pay:.2f}')
