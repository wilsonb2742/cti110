# Bryanna Wilson
# 4/9/2025
# P2HW2
# This program asks the user to input test grades for 6 modules,
# stores them in a list, and displays the lowest, highest, total, and average grades.

'''
Pseudocode:
1. Prompt user to enter grade for Module 1
2. Prompt user to enter grade for Module 2
3. Prompt user to enter grade for Module 3
4. Prompt user to enter grade for Module 4
5. Prompt user to enter grade for Module 5
6. Prompt user to enter grade for Module 6
7. Store all 6 grades in a list
8. Display:
   - Lowest Grade
   - Highest Grade
   - Sum of Grades
   - Average of Grades (rounded to 2 decimal places)
'''

# User input for each module
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Store in list
grades = [module1, module2, module3, module4, module5, module6]

# Output results
print("\n------------Results------------")
print("Lowest Grade:      ", format(min(grades), '.1f'))
print("Highest Grade:     ", format(max(grades), '.1f'))
print("Sum of Grades:     ", format(sum(grades), '.1f'))
print("Average:           ", format(sum(grades)/len(grades), '.2f'))
print("-------------------------------")
