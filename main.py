from turtle import Screen

from ball import Ball
from paddle import Paddle
import time

screen = Screen()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
# Removes default animation
screen.tracer(0)


user_paddle = Paddle(x_position=350, y_position=0)
computer_paddle = Paddle(x_position=-350, y_position=0)
ball = Ball()

screen.listen()
screen.onkey(user_paddle.go_up, "Up")
screen.onkey(user_paddle.go_down, "Down")
screen.onkey(computer_paddle.go_up, "w")
screen.onkey(computer_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    # Update animation since screen.tracer is 0
    screen.update()
    time.sleep(0.10)
    ball.move()

    # Detect when ball hits top or bottom
    if ball.ycor() < -290 or ball.ycor() > 290:
        ball.bounce()

screen.exitonclick()

