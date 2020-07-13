import turtle
import math

t = turtle.Turtle()
t.shape("turtle")

x1 = int(input("첫번째 원의 x좌표: "))
y1 = int(input("첫번째 원의 y좌표: "))
r1 = int(input("첫번째 원의 반지름: "))
x2 = int(input("두번째 원의 x좌표: "))
y2 = int(input("두번째 원의 y좌표: "))
r2 = int(input("두번째 원의 반지름: "))

dis = math.sqrt(float(((x1-x2)**2+(y1-y2)**2)))

t.up()
t.goto(x1,y1-r1)
t.down()
t.circle(r1)

t.up()
t.goto(x2,y2-r2)
t.down()
t.circle(r2)

if(r1<r2):
    if(dis + r1< r2):
        t.write("두번째 원 내부에 첫번재 원이 있습니다.")
    elif(dis < r1+r2):
        t.write("2개의 원이 겹쳐있습니다.")
    else:
        t.write("2개의 원이 겹치지 않습니다.")
else:
    if(dis + r2< r1):
        t.write("첫번째 원 내부에 두번째 원이 있습니다.")
    elif(dis < r1+r2):
        t.write("2개의 원이 겹쳐있습니다.")
    else:
        t.write("2개의 원이 겹치지 않습니다.")
