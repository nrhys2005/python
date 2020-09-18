import turtle

def f(x):
    t.goto(x,(x**2+1)/100)

t = turtle.Turtle()

t.forward(250)
t.backward(250)
t.left(90)
t.forward(250)
t.bk(250)


for x in range(150):
    f(x)
