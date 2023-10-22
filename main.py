from turtle import Screen
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

screen.listen()
screen.onkey(user_paddle.go_up, "Up")
screen.onkey(user_paddle.go_down, "Down")
screen.onkey(comp_paddle.go_up, "w")
screen.onkey(comp_paddle.go_down, "s")
screen.onkey(screen.bye, "x")


game_is_on = True
while game_is_on:
    # Update animation since screen.tracer is 0
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect when ball hits top or bottom
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with user_paddle
    if ball.distance(user_paddle) < 50 and ball.xcor() > 320 or ball.distance(comp_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect comp_paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_user_score()
        # game_is_on = False

    # Detect user_paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_comp_score()
        # game_is_on = False


screen.exitonclick()

