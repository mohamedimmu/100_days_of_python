# 3.2 BMI 2.0

weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in m : "))

bmi_result = round(weight / (height ** 2))

if bmi_result < 18.5:
    print(f"Your BMI is {bmi_result}, you are underweight.")
elif 18.5 < bmi_result < 25:
    print(f"Your Bmi is {bmi_result}, your are normal weight.")
elif 25 < bmi_result < 30:
    print(f"Your Bmi is {bmi_result}, your are slightly over weight.")
elif 25 < bmi_result < 30:
    print(f"Your Bmi is {bmi_result}, your are obese.")
else:
    print(f"Your BMI is {bmi_result}, your are clinically obese")

