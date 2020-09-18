from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import time
import random

WIDTH = 800
HEIGHT = 400

class Ball:				
    def __init__(self, canvas, color, size, x, y, xspeed, yspeed, img):	
        self.canvas = canvas		# 캔버스 객체
        self.color = color		# Ball의 색상
        self.size = size		# Ball의 크기
        self.x = x			# Ball의 x좌표
        self.y = y			# Ball의 y좌표
        self.xspeed = xspeed		# Ball의 수평방향 속도
        self.yspeed = yspeed		# Ball의 수직방향 속도
        self.id = canvas.create_oval(x, y, x+size, y+size, fill=color)
        self.imgid=canvas.create_image(x,y,anchor=NW, image=img)

    def move(self):			# Ball을 이동시키는 함수
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        self.canvas.move(self.imgid, self.xspeed, self.yspeed)
        
        (x1, y1, x2, y2) = self.canvas.coords(self.id)	# 공의 현재 위치를 얻는다.
        (self.x, self.y) = (x1, y1)
        if x1 <= 0 or x2 >= WIDTH:  # 공의 x좌표가 음수이거나 x좌표가 오른쪽 경계를 넘으면
            self.xspeed = - self.xspeed		# 속도의 부호를 반전시킨다. 
        if y1 <= 0 or y2 >= HEIGHT:  # 공의 x좌표가 음수이거나 x좌표가 오른쪽 경계를 넘으면
            self.yspeed = - self.yspeed		# 속도의 부호를 반전시킨다.

# 생성된 포탄을 저장하는 리스트
bullets = []

# 윈도우를 생성한다. 
window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='midnightblue')
canvas.pack()

im=Image.open('fire.png').resize((20,10))
bullet_img=ImageTk.PhotoImage(im)


# 이벤트를 처리하는 함수
def fire(event):
    bullets.append(Ball(canvas, "red", 10, 200, 250, 10, 0, img=bullet_img) )
    

canvas.bind("<Button-1>", fire)	# 마우스 버튼 클릭 이벤트에 함수를 연결한다.

# 우리 우주선과 외계 우주선을 생성한다.

im = Image.open('spacecraft.png').resize((100,100)).rotate(-90)
spaceship_img=ImageTk.PhotoImage(im)
spaceship=Ball(canvas, 'green', 100,100,200,0,0,img=spaceship_img)

im = Image.open('alien.png').resize((100,100))
enemy_image = ImageTk.PhotoImage(im)
enemy=Ball(canvas, 'red', 100,500,200,0,5,img=enemy_image)
# 리스트에 저장된 각각의 객체들을 이동시킨다. 
while True:
    for bullet in bullets:
        bullet.move()
        # 포탄이 화면을 벗어나면 삭제한다. 
        if (bullet.x+bullet.size) >= WIDTH: 
            canvas.delete(bullet.id)
            canvas.delete(bullet.imgid)
            bullets.remove(bullet)
    enemy.move()
    window.update()
    time.sleep(0.03)
