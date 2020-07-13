import turtle

t = turtle.Turtle()
t.shape("turtle")
x = []
y = []

x.append(int(input("x1 입력 : ")))
y.append(int(input("y1 입력 : ")))
x.append(int(input("x2 입력 : ")))
y.append(int(input("y2 입력 : ")))
x.append(int(input("x3 입력 : ")))
y.append(int(input("y3 입력 : ")))


t.goto(x[0],y[0])
t.goto(x[1],y[1])
t.goto(x[2],y[2])


