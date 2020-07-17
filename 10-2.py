from tkinter import *

window = Tk()
num = 0
label1 = Label(window,text="현재 합계: ")
label2 = Label(window,text=str(num))
label1.grid(row=0,column=0)
label2.grid(row=0,column=2)

edit_num =  Entry(window)
edit_num.grid(row=1,column=0,columnspan=3)

def b1_click():
    global num
    num+=int(edit_num.get())
    label2 = Label(window,text=str(num))
    label2.grid(row=0,column=2)

def b2_click():
    global num
    num-=int(edit_num.get())
    label2 = Label(window,text=str(num))
    label2.grid(row=0,column=2)

def b3_click():
    global num
    num=0
    label2 = Label(window,text=str(num))
    label2.grid(row=0,column=2)

b1 = Button(window, text="더하기(+)",command=b1_click)
b2 = Button(window, text="빼기(0)",command=b2_click)
b3 = Button(window, text="초기화",command=b3_click)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)

window.mainloop()
