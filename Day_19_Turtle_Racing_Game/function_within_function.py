from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(100)
screen.listen() # have to bind a function which will be triggered after pressing a button
screen.onkey(move_forward,"1")
# Here i used a function within a function



screen.exitonclick()
