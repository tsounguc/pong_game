from turtle import Turtle

COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.comp_score = 0
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.comp_score} - {self.user_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_user_score(self):
        self.user_score += 1
        self.update_scoreboard()

    def increase_comp_score(self):
        self.comp_score += 1
        self.update_scoreboard()
