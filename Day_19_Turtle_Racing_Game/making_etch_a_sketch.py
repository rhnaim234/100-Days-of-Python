from turtle import Turtle, Screen
screen=Screen()
tim=Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)
def move_left():
    tim.left(10)
def move_right():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")




screen.exitonclick()
