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
comp_paddle = Paddle(x_position=-350, y_position=0)
ball = Ball()

screen.listen()
screen.onkey(user_paddle.go_up, "Up")
screen.onkey(user_paddle.go_down, "Down")
screen.onkey(comp_paddle.go_up, "w")
screen.onkey(comp_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    # Update animation since screen.tracer is 0
    screen.update()
    time.sleep(0.10)
    ball.move()

    # Detect when ball hits top or bottom
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with user_paddle
    if ball.distance(user_paddle) < 50 and ball.xcor() > 320 or ball.distance(comp_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect user_paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        # game_is_on = False

    # Detect comp_paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        # game_is_on = False

screen.exitonclick()

