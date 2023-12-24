''' Abriendo archivos CSV '''

## WITH READLINES
# with open("weather_data.csv", encoding="utf-8") as data_file:
#     data = data_file.readlines()
# print(data)

## WITH CSV
# import csv
# with open("weather_data.csv", encoding="utf-8") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
# print(temperature)

## WITH PANDAS
# import pandas
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# avg_temp_list = data["temp"].mean()
# max_temp_list = data["temp"].max()
# print(data)

# # Get data in column
# print(data["condition"])
# print(data.condition)

# # Get data in row
# print(data[data.temp == max_temp_list])
# monday = data[data.day == "Monday"]
# monday_temp_C = monday.temp
# monday_temp_F = (monday_temp_C * 9/5) + 32
# print(monday_temp_F)

# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

## EXERCISE OF SQUIRREL CENSUS DATA ANALYSIS
import pandas as pd
data = pd.read_csv(r"ProjectsPerDay\Day 025\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# grey = 0
# red = 0
# black = 0
# for color in data["Primary Fur Color"]:
#     if color == 'Cinnamon':
#         red += 1
#     elif color == 'Gray':
#         grey += 1
#     elif color == 'Black':
#         black += 1

grey = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey,red,black]
}
df = pd.DataFrame(data_dict)
df.to_csv("ProjectsPerDay\Day 025\squirrel_count.csv")
