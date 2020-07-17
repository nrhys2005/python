from tkinter import *

window = Tk()
cm = 0.0
label1 = Label(window,text="인치를 센티미터로 변환하는 프로그램")
label2 = Label(window,text="인치를 입력하시오:")
label1.grid(row=0,column=0,columnspan=2)
label2.grid(row=1,column=0)

edit_num = Entry(window)
edit_num.grid(row=1,column=1)

label3 = Label(window,text="반환결과:")
label4 = Label(window,text=str(cm))
label3.grid(row=2,column=0)
label4.grid(row=2,column=1)
def b1_click():
    global cm
    cm = float(edit_num.get())*2.54
    label4 = Label(window,text=str(cm))
    label4.grid(row=2,column=1)
b1 = Button(window, text="변환!",command=b1_click)
b1.grid(row=3,column=1)

window.mainloop()
