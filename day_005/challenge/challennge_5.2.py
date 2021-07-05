# 5.2 Highest Score

student_scores = input("Input a list of student scores : ").split()

student_scores = [int(student_score) for student_score in student_scores]

highest_score = 0
for student_score in student_scores:
    if highest_score < student_score:
        highest_score = student_score

print(highest_score)
