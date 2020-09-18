import turtle
import random

def draw_star(color, length, x, y):
    t.color(color,color)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for i in range(5):
        t.forward(length)
        t.right(144)
    t.end_fill()

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

color = ["white","green","skyblue","purple","blue", "yellow","orange"]
for i in range(10):
    c = color[random.randint(0,6)]
    length = random.randint(20,100)
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    draw_star(c, length, x, y)

    
