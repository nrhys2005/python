import random
import turtle
t = turtle.Turtle()
t.shape('turtle')

def drawStar(x, y, size ,color ):
    t.up()
    t.goto(x, y)
    t.down()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(0,5,1):
        t.forward(size)
        t.right(144)
    t.end_fill()

turtle.Screen().bgcolor("black")

colors=['green','blue', 'red','orange',
        'skyblue','white','yellow', 'purple']
n_colors = len(colors)

t.speed(100)

for i in range(0,100):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    s = random.randint(5,20)

    c = random.randint(0,)
    drawStar(x, y, s, colors[c])


