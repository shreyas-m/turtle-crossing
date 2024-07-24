from turtle import Turtle
import random

COLOR = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

speed = STARTING_MOVE_DISTANCE


def speedup():
        global speed
        speed += MOVE_INCREMENT


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 3)
        self.color(random.choice(COLOR))
        self.penup()
        self.goto(360, random.randint(-260, 280))

    def move(self):
        global speed
        new_x = self.xcor() - speed
        self.goto(new_x, self.ycor())
