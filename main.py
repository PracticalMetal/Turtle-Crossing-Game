from turtle import Turtle, Screen
from cars import Cars
import random
import time


def move_turtle():
    turtle.fd(10)


def level_update(l):
    screen_level.clear()
    screen_level.write(f"Level: {l}", font=("Arial", 16, "normal"))


# setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)


# setting the turtle which will allow to play the game
turtle = Turtle("turtle")
turtle.penup()
turtle.setheading(90)
turtle.goto(x=0, y=-280)

# generating random cars opm the initial screen
random_cars = []
for i in range(20):
    new_car = Cars()
    new_car.goto(random.randrange(-280, 280, 80),
                 random.randrange(-210, 250, 80))
    random_cars.append(new_car)


# generating level
level = 1
screen_level = Turtle()
screen_level.hideturtle()
screen_level.penup()
screen_level.goto(-260, 260)


# game mechanism
game_is_on = True
sleep_time = 0.4

screen.listen()
screen.onkey(fun=move_turtle, key="Up")
random_x_cor = [320, 360, 400, 440, 480, 520]

while game_is_on:
    level_update(level)
    screen.update()
    time.sleep(sleep_time)
    random_chance = random.randint(1, 3)
    if random_chance == 1:
        new_car = Cars()
        new_car.goto(300, random.randint(-250, 250))
        random_cars.append(new_car)
    for random_car in random_cars:
        if turtle.distance(random_car) < 30:
            game_is_on = False
            screen.update()
    for random_car in random_cars:
        random_car.fd(20)

    # checking for level up
    if turtle.ycor() >= 280:
        level += 1
        turtle.goto(x=0, y=-280)
        sleep_time /= 2


screen.exitonclick()
