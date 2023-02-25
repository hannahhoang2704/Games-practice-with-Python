from turtle import Turtle, Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)


player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.created_car()
    car_manager.car_move()







screen.exitonclick()