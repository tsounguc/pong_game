from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        for index in range(5):
            self.shape("square")
            self.penup()
            self.color("white")
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.goto(x_position, y_position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

