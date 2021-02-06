from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.title("A3AJAGBE PING PONG GAME")
screen.bgcolor("firebrick")
screen.tracer(0)

right_paddle = Paddle((450, 0))
left_paddle = Paddle((-460, 0))

ball = Ball()

# Liston for key press
screen.listen()
screen.onkey(right_paddle.up, 'i')
screen.onkey(right_paddle.down, 'm')
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "z")

game_start = True
while game_start:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 420 or ball.distance(left_paddle) < 50 and ball.xcor() < -440:
        ball.bounce_x()

    # Detect when paddle misses
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.reset()


# Stay running until exited
screen.exitonclick()
