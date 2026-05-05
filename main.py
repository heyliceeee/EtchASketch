from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    """
    turtle move forward 10 steps
    """
    tim.forward(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards) # when click in w key, turtle move forward
screen.onkey(key="s", fun=move_backwards) # when click in s key, turtle move backward
screen.onkey(key="a", fun=move_counter_clockwise) # when click in a key, turtle move counter-clockwise
screen.onkey(key="d", fun=move_clockwise) # when click in d key, turtle move clockwise
screen.onkey(key="c", fun=clear_drawing) # when click in c key, clear draw

screen.exitonclick() # screen close only if you click him