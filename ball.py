from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.shape("circle")
        self.color("snow")

    def move(self):
        update_posX = self.xcor() + 10
        update_posY = self.ycor() + 10
        self.goto(x=update_posX, y=update_posY)
