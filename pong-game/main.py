from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.hit()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit()
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.restart()
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.restart()
    ball.move_right()


screen.exitonclick()
