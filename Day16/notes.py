# import turtle
# timmy = turtle.Turtle()
# my_screen = turtle.Screen()

# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(300)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

table.align = 'l'

print(table)




