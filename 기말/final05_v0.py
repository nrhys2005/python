from tkinter import *
import time
import random

WIDTH = 800
HEIGHT = 400

class Ball:				
    def __init__(self, canvas, color, size, x, y, xspeed, yspeed):	
        self.canvas = canvas		# 캔버스 객체
        self.color = color		# Ball의 색상
        self.size = size		# Ball의 크기
        self.x = x			# Ball의 x좌표
        self.y = y			# Ball의 y좌표
        self.xspeed = xspeed		# Ball의 수평방향 속도
        self.yspeed = yspeed		# Ball의 수직방향 속도
        self.id = canvas.create_oval(x, y, x+size, y+size, fill=color)

    def move(self):			# Ball을 이동시키는 함수
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        (x1, y1, x2, y2) = self.canvas.coords(self.id)	# 공의 현재 위치를 얻는다.
        (self.x, self.y) = (x1, y1)
        if x1 <= 0 or x2 >= WIDTH:  # 공의 x좌표가 음수이거나 x좌표가 오른쪽 경계를 넘으면
            self.xspeed = - self.xspeed		# 속도의 부호를 반전시킨다. 
        if y1 <= 0 or y2 >= HEIGHT:  # 공의 x좌표가 음수이거나 x좌표가 오른쪽 경계를 넘으면
            self.yspeed = - self.yspeed		# 속도의 부호를 반전시킨다.

    def rect(self):
        return self.canvas.coords(self.id)


# 생성된 포탄을 저장하는 리스트
bullets = []


# 이벤트를 처리하는 함수
def fire(event):
    bullet = Ball(canvas, "red", 10, 150, 250, 10, 0)
    bullets.append( bullet )
    
# 윈도우를 생성한다. 
window = Tk()
##canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="midnightblue")
canvas.pack()
canvas.bind("<Button-1>", fire)	# 마우스 버튼 클릭 이벤트에 함수를 연결한다.

# 우리 우주선과 외계 우주선을 생성한다.
spaceship = Ball(canvas, "green", 100, 100, 200, 0, 0)

enemy = Ball(canvas, "red", 50, 500, 20, 0, 10)

# 5-2번 문제의 힌트:
# 충돌감지를 위한 사각형 R1과 사각형 R2의 중복테스트 함수
# R1: (x1, y1, x2, y2)
# R2: (x3, y3, x4, y4)
def isRectangleOverlap(R1, R2):
  if ((R1[0]>=R2[2]) or
      (R1[2]<=R2[0]) or
      (R1[3]<=R2[1]) or
     (R1[1]>=R2[3]) ):
     return False
  else:
    return True

# 리스트에 저장된 각각의 객체들을 이동시킨다. 
while True:
    for bullet in bullets:
        bullet.move()

        ## 5-2번 문제의 힌트:
        ## 포탄이 적과 충돌했는지 이 지점에서  테스트한다.
        ## 나중에 작성해야 되는 부분
        ## TODO TODO TODO
        ## TODO TODO TODO
        ## TODO TODO TODO
        ## TODO TODO TODO
        
        # 포탄이 화면을 벗어나면 삭제한다. 
        if (bullet.x+bullet.size) >= WIDTH: 
            canvas.delete(bullet.id)
            bullets.remove(bullet)
    enemy.move()
    window.update()
    time.sleep(0.03)
