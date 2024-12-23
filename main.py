from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "yellow", "blue", "purple", "black", "pink"]
all_turtle = []

y = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 30
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"You have won. The winning turtle is {turtle.pencolor()}")
            else:
                print(f"You have lose. The winning turtle is {turtle.pencolor()}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# def move_forwards():
#     tim.forward(10)
#     print(tim.heading())
# def move_backwards():
#     tim.backward(10)
#
# def restart_game():
#     tim.reset()
#
# def move_clockwise():
#     tim.seth(tim.heading() + 10)
#     print(tim.heading())
#
# def move_counter_clockwise():
#     tim.seth(tim.heading() - 10)
#     print(tim.heading())
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=move_clockwise)
# screen.onkey(key="d", fun=move_counter_clockwise)
# screen.onkey(key="c", fun=restart_game)

screen.exitonclick()
