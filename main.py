from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=1000, height=600)
screen.title("A3AJAGBE PING PONG GAME")
screen.bgcolor("firebrick")
screen.tracer(0)

right_paddle = Paddle((450, 0))
left_paddle = Paddle((-460, 0))

# Liston for key press
screen.listen()
screen.onkey(right_paddle.up, 'i')
screen.onkey(right_paddle.down, 'm')
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "z")

game_start = True
while game_start:
    screen.update()

# Stay running until exited
screen.exitonclick()
