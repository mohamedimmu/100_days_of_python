# 5.1 Average Height

student_heights = input("Input a list of student heights : ").split()

student_heights = [int(student_height) for student_height in student_heights]

sum_of_height = 0
for student_height in student_heights:
    sum_of_height += student_height

average_height = round(sum_of_height/len(student_heights))
print(average_height)



