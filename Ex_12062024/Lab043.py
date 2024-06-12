# Write a program that calculates and displays the letter grade for a
# given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

score = int(input("Enter the score\n"))

# score >=90 and score <=100 -> A
# score >=80 and score <=89 -> B
# score >=70 and score <=79 -> C
# score >=60 and score <=69 -> D
# score >=0 and score <=59 -> F

if score >= 90 and score <= 100:
    print("Grade is A")
elif score >= 80 and score <= 90:
    print("Grade is B")
elif score >= 70 and score <= 80:
    print("Grade is C")
elif score >= 60 and score <= 70:
    print('Grade is D')
elif score >= 0 and score <= 59:
    print('Grade is F')
else:
    print("Invalid Score")











