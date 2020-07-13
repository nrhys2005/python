import turtle
import math

t = turtle.Turtle()
t.shape("turtle")

for i in range(360):
    sine = math.sin((math.pi * i) / 180.0)
    t.goto(i, sine * 100)


