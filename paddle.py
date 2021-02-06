from turtle import Turtle


class Paddle:

    def __init__(self):
        self.right = Turtle("square")
        self.right_paddle()
        self.left = Turtle("square")
        self.left_paddle()

    def right_paddle(self):
        """This function sets the right paddle"""
        self.right.penup()
        self.right.shapesize(stretch_wid=7, stretch_len=1)
        self.right.goto(x=470, y=0)

    def left_paddle(self):
        """This function sets the left paddle"""
        self.left.penup()
        self.left.shapesize(stretch_wid=7, stretch_len=1)
        self.left.goto(x=-480, y=0)

    # Set the up and down direction of the right paddle
    def right_up(self):
        update_PosY = self.right.ycor() + 20
        posX = self.right.xcor()
        self.right.goto(x=posX, y=update_PosY)

    def right_down(self):
        update_PosY = self.right.ycor() - 20
        posX = self.right.xcor()
        self.right.goto(x=posX, y=update_PosY)

    # Set the up and down direction of the left paddle
    def left_up(self):
        update_PosY = self.left.ycor() + 20
        posX = self.left.xcor()
        self.left.goto(x=posX, y=update_PosY)

    def left_down(self):
        update_PosY = self.left.ycor() - 20
        posX = self.left.xcor()
        self.left.goto(x=posX, y=update_PosY)

