from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.shape("circle")
        self.color("snow")
        self.move_x = 10
        self.move_y = 10

    def move(self):
        update_posX = self.xcor() + self.move_x
        update_posY = self.ycor() + self.move_y
        self.goto(x=update_posX, y=update_posY)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
