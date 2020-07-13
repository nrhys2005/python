import turtle

t = turtle.Turtle()
t.shape("turtle")

color = []
color.append(input("색상 입력 : "))
color.append(input("색상 입력 : "))
color.append(input("색상 입력 : "))

t.fillcolor(color[0])
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
    
t.goto(100,0)
t.down()
t.fillcolor(color[1])
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()

t.goto(200,0)
t.down()
t.fillcolor(color[2])
t.begin_fill()
t.circle(50)
t.end_fill()
