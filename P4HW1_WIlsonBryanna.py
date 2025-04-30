# Bryanna WIlson
# 04/30/2025
# P4HW1
# This program collects test scores, removes the lowest one, calculates the average,
# and displays the letter grade based on that average.

# Pseudocode:
# 1. Ask how many scores the user wants to enter.
# 2. Use a loop to collect that many scores with validation.
# 3. Store scores in a list.
# 4. Drop the lowest score from the list.
# 5. Calculate average of remaining scores.
# 6. Display the lowest score, modified list, average, and letter grade.


num_scores = int(input("How many scores do you want to enter? "))


score_list = []
count = 0

while count < num_scores:
    score_input = float(input("Enter score #" + str(count + 1) + ": "))
    if score_input >= 0 and score_input <= 100:
        score_list.append(score_input)
        count += 1
    else:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100.")


lowest = min(score_list)
score_list.remove(lowest)
total = 0
i = 0


while i < len(score_list):
    total += score_list[i]
    i += 1

average = total / len(score_list)


if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'


print("\n------------Results------------")
print("Lowest Score:", lowest)
print("Modified List:", score_list)
print("Scores Average: {:.2f}".format(average))
print("Grade:", grade)
print("---------------------------------")
