# P3HW1
# 4/23/2025
# Wilson
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Print results
print("\n------------Results------------")
print("Lowest Grade:      ", format(min(grades), '.1f'))
print("Highest Grade:     ", format(max(grades), '.1f'))
print("Sum of Grades:     ", format(sum(grades), '.1f'))
print("Average:           ", format(sum(grades)/len(grades), '.2f'))

# Determine letter grade for average
if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print('--------------------------------------')
print(f'Your grade is: {letter_grade}')





