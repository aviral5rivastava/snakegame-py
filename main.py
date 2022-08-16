from turtle import Screen, Turtle

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")


class Snake:
    def __init__(self):
        self.all_bits = []
        for i in range(0, 3):
            bit = Turtle("square")
            bit.color("white")
            self.all_bits.append(bit)
        x = -10
        for bit in self.all_bits:
            bit.goto(x, 0)
            x += 10


snake = Snake()
screen.exitonclick()
