import csv
import pandas

with open("weather_data.csv") as weather_data_file:
    weather_data = csv.reader(weather_data_file)
    temperature = []
    fields = next(weather_data)
    for row in weather_data:
        temp = int(row[1])
        temperature.append(temp)

print(temperature)

# Using Pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()

print(f"\nUsing Pandas: {temp_list}\n")

# average temperature

average_temp = 0
for temp in temp_list:
    average_temp += temp
average_temp /= len(temp_list)
print(average_temp)

# average temperature using pandas
average = data["temp"].mean()
print(f"\nUsing Pandas: {average}\n")
max_temp = data["temp"].max()
print(f"max temp: {max_temp}\n")

# Get the data in column
# print(data["temp"])
# print(data.temp)

# Get the data in row
# print(data[data.day == "Monday"])

# Priniting out max temperature row
max_temp_row = data[data.temp == max_temp]
print(max_temp_row)

# Converting monday temp celsius to fahrenheit
# Formula: (°C * 1.8) + 32 = °F
monday = data[data.day == "Monday"]
celsius = monday.temp
print(f"\ncelusius: {celsius}")

fahrenheit = (celsius * 1.8) + 32
print(f"\nfahrenheit: {fahrenheit}°F")

# Creating the  data frame
student_score = {
    "students": ["Mark Zuckerberg", "Elon Musk", "Jeff Bezos"],
    "score": [75, 65, 85]
}
student_score_data = pandas.DataFrame(student_score)
student_score_data.to_csv("student_score.csv")