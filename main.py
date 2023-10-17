from turtle import Screen

from paddle import Paddle

screen = Screen()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
# Removes default animation
screen.tracer(0)


user_paddle = Paddle(x_position=350, y_position=0)
computer_paddle = Paddle(x_position=-350, y_position=0)
screen.listen()
screen.onkey(user_paddle.go_up, "Up")
screen.onkey(user_paddle.go_down, "Down")
screen.onkey(computer_paddle.go_up, "w")
screen.onkey(computer_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    # Update animation since screen.tracer is 0
    screen.update()

screen.exitonclick()
