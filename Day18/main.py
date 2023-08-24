import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.hideturtle()
tim.penup()

color_list = [(246, 242, 234), (247, 242, 244), (240, 246, 242), (239, 242, 246), (196, 166, 119), (140, 81, 58), (219, 201, 141), (61, 94, 117), (162, 151, 57), (137, 162, 180), (127, 35, 25), (70, 39, 32), (54, 116, 86), (189, 97, 80), (147, 177, 150), (21, 90, 69), (163, 144, 158), (32, 59, 75), (108, 77, 82), (225, 178, 165), (179, 204, 177), (123, 30, 33), (68, 35, 38), (28, 81, 87), (91, 145, 126), (19, 68, 57), (47, 64, 82), (172, 96, 99), (214, 181, 184), (182, 192, 203)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()