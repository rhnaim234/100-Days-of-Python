from turtle import Turtle, Screen
import random
screen = Screen()
is_game_on = False
screen.setup(width=800, height=600)
screen.bgcolor("sky blue")
user_bet=screen.textinput(title="Make your bet", prompt="which color will win?")
colors = ["red", "green", "blue", "yellow", "purple"]
y_positions = [-200, -100, 0, 100, 200]
all_turtles = []

for i in range(5):
    tim=Turtle()
    tim.shape("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-390,y_positions[i])
    all_turtles.append(tim)
if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 370:
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You won! The winning color is {winning_color}")
            else:
                print(f"You lost! The winning color is {winning_color}")
            is_game_on = False
        run_distance=random.randint(0, 10)
        turtle.forward(run_distance)

screen.exitonclick()