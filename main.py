from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


class Snake:
    def __init__(self):
        self.all_bits = []
        for i in range(0, 3):
            bit = Turtle("square")
            bit.color("white")
            bit.penup()
            self.all_bits.append(bit)
        x = -10
        for bit in self.all_bits:
            bit.goto(x, 0)
            x += 10

    # method added to move forward
    def mov_forward(self):
        for i in range(len(self.all_bits)-1, 0, -1):
            new_x = self.all_bits[i - 1].xcor()
            new_y = self.all_bits[i - 1].ycor()
            self.all_bits[i].goto(new_x, new_y)
        self.all_bits[0].forward(20)


snake = Snake()
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.25)
    snake.mov_forward()

screen.exitonclick()
