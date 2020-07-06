import turtle
t=turtle.Pen()
t.shape("turtle")
#굵기
t.pensize(20)

#노랑색 원
t.up()
t.goto(-80,-100)
t.down()
t.color("yellow")
t.circle(80)
t.up()
#노랑색 원
t.goto(80,-100)
t.down()
t.color("green")
t.circle(80)
t.up()
#파랑색 원
t.goto(-150,0)
t.down()
t.color("blue")
t.circle(80)
t.up()
#검정색 원
t.goto(0,0)
t.down()
t.color("black")
t.circle(80)
t.up()
#빨강색 원
t.goto(150,0)
t.down()
t.color("red")
t.circle(80)
t.up()

#turtle 지우기
t.hideturtle()
