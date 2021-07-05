import colorgram

colors = colorgram.extract('hirst_spot_painting.png', 30)
color_palette = []
for index in range(len(colors)):
    rgb_color = colors[index].rgb
    red = rgb_color.r
    green = rgb_color.g
    blue = rgb_color.b
    new_color = (red, green, blue)
    color_palette.append(new_color)