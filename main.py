from turtle import Turtle, Screen, mode

tim = Turtle()
screen = Screen()


def move_forwards():
    """
    turtle move forward 10 steps
    """
    tim.forward(10)
def move_backwards():
    """
    turtle move backward 10 steps
    """
    tim.backward(10)
def move_left():
    """
    turtle move left
    """
    tim.left(10)
def move_right():
    """
    turtle move right
    """
    tim.right(10)
def clear_drawing():
    """
    clear draw and put turtle in center
    """
    tim.clear() # clear the draw
    tim.penup() # no draw while go center
    tim.home() # turtle go center
    tim.pendown() # lets draw while move

screen.listen()
screen.onkey(move_forwards, "w") # when click in w key, turtle move forward
screen.onkey(move_backwards, "s") # when click in s key, turtle move backward
screen.onkey(move_left, "a") # when click in a key, turtle move left
screen.onkey(move_right, "d") # when click in d key, turtle move right
screen.onkey(clear_drawing, "c") # when click in c key, clear draw

screen.exitonclick() # screen close only if you click him