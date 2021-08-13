import pandas as pd

squirrel_data = pd.read_csv("squirrel_data.csv")
fur_color = squirrel_data["Primary Fur Color"].to_list()

color_list = {
    "Fur Color": ['Black', 'Cinnamon', 'Gray'],
    "Count": [0, 0, 0]
}

for num in range(0, len(color_list["Fur Color"])):
    color = color_list["Fur Color"][num]
    color_count = fur_color.count(color)
    color_list["Count"][num] = color_count

fur_color_count = pd.DataFrame(color_list)
fur_color_count.to_csv("squirrel_count.csv")