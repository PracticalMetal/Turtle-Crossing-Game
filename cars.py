from turtle import Turtle, Screen
import turtle
import random

# generating random colours for the car
turtle.colormode(255)


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.randint(1, 255), random.randint(
            1, 255), random.randint(1, 255))
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.setheading(180)

    def move_car(self):
        self.fd(10)
