from turtle import Turtle, Screen
import turtle
import random


def move_forward(names):
    for name in names:
        name.forward(random.randint(5, 50))


def move_backward():
    tim.backward(10)


def rotate_cc():
    tim.right(10)


def rotate_cw():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.goto(0, 0)
    tim.pendown


def create_turtles(names):
    for name in names:
        name = Turtle()


def goto_start(names, xstart, ystart, yinc):
    ycor = ystart
    for name in names:
        name.penup()
        name.goto(xstart, ycor)
        ycor += yinc


def change_appearance(names):
    counter = 0
    for name in names:
        # name.shape("turtle")
        name.color(colors[counter])
        counter += 1


def set_speed(names):
    for name in names:
        name.speed(random.randint(0, 10))


def get_turtle_pos(names):
    xcor = 0
    for name in names:
        current_xcor = name.xcor()
        if current_xcor > xcor:
            xcor = current_xcor
    return xcor


# create_turtles(turtle_names)

is_race_on = False
colors = ["red", "orange", "yellow", "green", "purple"]

tim = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
ron = Turtle(shape="turtle")
sue = Turtle(shape="turtle")
monika = Turtle(shape="turtle")

turtle_names = [tim, tom, ron, sue, monika]

turtle_colors = [
    (224, 144, 95),
    (82, 192, 231),
    (239, 77, 118),
    (217, 239, 248),
    (121, 227, 185),
    (251, 71, 31),
    (237, 226, 99),
    (54, 88, 146),
]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# turtle.colormode(255)
# turtle.setworldcoordinates(-100, -150, 400, 150)
change_appearance(turtle_names)
goto_start(turtle_names, -230, -100, 40)
# set_speed(turtle_names)

if user_bet:
    is_race_on = True
pos = -230

while is_race_on:
    for turtle in turtle_names:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle has won the game.")
            else:
                print(f"You have lost! The {winning_color} turtle has won the game.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# while pos < 250:
#     move_forward(turtle_names)
#     pos = get_turtle_pos(turtle_names)

# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=rotate_cc)
# screen.onkey(key="d", fun=rotate_cw)
# screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
