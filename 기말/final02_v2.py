
from tkinter import *

def plus_calc():
    num = int(e1.get())
    global total
    total = total + num
    l2['text']=str(total)

def minus_calc():
    num = int(e1.get())
    global total
    total = total - num
    l2['text']=str(total)

def reset_calc():
    global total
    total = 0
    l2['text']=str(total)
    e1.option_add

def b4_calc():
    num = int(e1.get())
    global total
    total = total * num
    l2['text']=str(total)

def b5_calc():
    num = int(e1.get())
    global total
    total = total // num
    l2['text']=str(total)

def b6_calc():
    num = int(e1.get())
    global total
    total = total % num
    l2['text']=str(total)
    e1.option_add

total = 0

window = Tk()

l1 = Label(window, text = '현재 합계:')
l1.grid(row=0,column=0)

l2 = Label(window)
l2.grid(row=0,column=1)

e1 = Entry(window)
e1.grid(row=1,columnspan=3)

b1= Button(window, text = '더하기(+)', command=plus_calc)
b2= Button(window, text = '빼기(-)', command=minus_calc)
b3= Button(window, text = '초기화', command=reset_calc)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)

b4= Button(window, text = '곱하기(*)', command=b4_calc)
b5= Button(window, text = '나누기(//)', command=b5_calc)
b6= Button(window, text = '나머지(%)', command=b6_calc)
b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)

window.mainloop()
