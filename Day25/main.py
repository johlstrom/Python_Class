# with open("Day25\\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("Day25\\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("Day25\\weather_data.csv")
# # #print(type(data))
# # print(data["temp"].max())

# # data_dict = data.to_dict()
# # # print(data_dict)

# # temp_list = data["temp"].to_list()
# # # print(temp_list)

# # average = sum(temp_list) / len(temp_list)
# # print(average)
# # print(data.condition)

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

import pandas
data = pandas.read_csv("Day25\\2018_Central_Park_Squirrel_Census.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Day25\\SquirrelCount.csv")
