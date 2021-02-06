from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=1000, height=600)
screen.title("A3AJAGBE PING PONG GAME")
screen.bgcolor("firebrick")

paddle = Paddle()

# Liston for key press
screen.listen()
screen.onkey(paddle.right_up, 'i')
screen.onkey(paddle.right_down, 'm')
screen.onkey(paddle.left_up, "w")
screen.onkey(paddle.left_down, "z")

# Stay running until exited
screen.exitonclick()
