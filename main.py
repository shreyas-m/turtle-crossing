from turtle import Screen
import time, player, car_manager, scoreboard, random

screen = Screen()
screen.screensize(600, 600)
screen.tracer(0)
screen.listen()

player = player.Player()
score = scoreboard.Scoreboard()
cars = [car_manager.CarManager()]

screen.onkey(player.move, "Up")

is_game_on = True
while is_game_on:
    time.sleep(.1)
    screen.update()
    if random.randint(0, 10) == 9:
        cars.append(car_manager.CarManager())
    for i, car in enumerate(cars):
        car.move()

    # Detect player reaches finish line
    if player.ycor() >= 280:
        score.score_point()
        player.reset_position()
        car_manager.speedup()

    # Detect car collision
    for i, car in enumerate(cars):
        if (car.ycor()-20 < player.ycor() < car.ycor()+20 and car.xcor()-40 < player.xcor() < car.xcor()+40
                and player.distance(car) < 40):
            is_game_on = False
            score.game_over()

screen.exitonclick()
