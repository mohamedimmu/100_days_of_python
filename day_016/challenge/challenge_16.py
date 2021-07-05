# 16.1 Creating ASCII table

from prettytable import PrettyTable

x = PrettyTable()
x.add_column("Pokemon Names", ["Charmeleon", "Watortle", "Pikachu", "Vulpix", "Ivysaur", "Charizard", "Squirtle"])
x.add_column("Types", ["Fire", "Water", "Electric", "Fire", "Grass, Poison", "Fire, Flying", "Water"])
x.align = "l"  # 0 - left, 1 - centre, 2 - right
print(x)
