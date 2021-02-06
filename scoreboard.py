from turtle import Turtle
FONT = ("Arial", 70, "bold")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("snow")
        self.goto(x=0, y=275)
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()

    def increase_right_score(self):
        """This function increases the right score"""
        self.right_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_left_score(self):
        """This function increases the left score"""
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        """This function updates the scoreboard"""
        self.goto(-100, 200)
        self.write(f"{self.left_score}", align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.right_score}", align=ALIGN, font=FONT)
