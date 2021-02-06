from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=7, stretch_len=1)
        self.goto(position)

    # Set the up and down direction of the paddles
    def up(self):
        update_PosY = self.ycor() + 20
        posX = self.xcor()
        self.goto(x=posX, y=update_PosY)

    def down(self):
        update_PosY = self.ycor() - 20
        posX = self.xcor()
        self.goto(x=posX, y=update_PosY)


