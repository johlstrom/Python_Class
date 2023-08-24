import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed(0)
current_heading = tim.heading()

while current_heading < 360:
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(current_heading + 1)
    current_heading += 1
    
screen = t.Screen()
screen.exitonclick()