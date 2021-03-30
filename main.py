import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(scoreboard.start_game, "space")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if scoreboard.start_game_flag:
        car_manager.create_cars()
        car_manager.move_cars()
        player.showturtle()

    if player.distance(player.xcor(), 300) < 30:
        player.go_original_position()
        scoreboard.level += 1
        car_manager.car_speed *= 1.1
        scoreboard.show_score()

    for car in car_manager.car_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.show_result()


screen.exitonclick()



