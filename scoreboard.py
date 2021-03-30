from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.write("Press SPACE to start the game", align="center", font=FONT)
        self.level = 1
        self.start_game_flag = False

    def start_game(self):
        self.start_game_flag = True
        self.show_score()

    def show_score(self):

        self.clear()
        self.goto(-260, 250)
        self.write("level: " + str(self.level), align="left", font=FONT)

    def show_result(self):
        self.goto(0, 10)
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=4,stretch_len=20)
        self.stamp()
        self.color("white")
        self.goto(0, 0)
        self.write("Your final level is " + str(self.level) + " !", align="center", font=FONT)