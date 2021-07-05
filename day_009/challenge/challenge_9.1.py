# 9.1 Grading Program

# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

"""
eg - output : '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding',
'Draco': 'Acceptable', 'Neville': 'Fail'}'
"""

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# Create an empty dictionary called student_grades.
student_grades = {}

# Write your code below to add the grades to student_grades.👇


for key in student_scores:
    score = student_scores[key]
    if 90 < score <= 100:
        student_grades[key] = "Outstanding"
    elif 80 < score <= 90:
        student_grades[key] = "Exceeds Exceptions"
    elif 70 < score <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)