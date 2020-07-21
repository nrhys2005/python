infile = open("data.txt", "r")
outfile = open("output.txt","a")

print("입력 파일 이름 : data.txt")
print("출력 파일 이름 : output.txt")
num_sum = 0
count = 0
for line in infile:
    line = line.rstrip()
    num_sum += float(line)
    count+=1
outfile.write("합계="+str(num_sum)+"\n")
outfile.write("평균="+str(num_sum/count))
outfile.close()
infile.close()


from tkinter import *
import pickle
phone_book = {}


window = Tk()
label1 = Label(window,text="이름")
label2 = Label(window,text="전화번호")
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
edit_name = Entry(window)
edit_phone = Entry(window)
edit_name.grid(row=0,column=1,columnspan=6)
edit_phone.grid(row=1,column=1,columnspan=6)

def b1_click():
    name = edit_name.get()
    phone = edit_phone.get()
    phone_book[name] = phone
    file = open("phone_book.dat","wb")
    pickle.dump(phone_book,file)
    file.close()
    edit_name.delete(0,END)
    edit_phone.delete(0,END)
def b2_click():
    
def b3_click():
def b4_click():
def b5_click():
def b6_click():
    file = open( "phone_book.dat", "rb" )
    global phone_book
    phone_book = pickle.load( file )

b1 = Button(window, text="추가",command=b1_click)
b2 = Button(window, text="처음",command=b2_click)
b3 = Button(window, text="다음",command=b3_click)
b4 = Button(window, text="이전",command=b4_click)
b5 = Button(window, text="마지막",command=b5_click)
b6 = Button(window, text="파일 읽기",command=b6_click)

b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
b4.grid(row=2,column=3)
b5.grid(row=2,column=4)
b6.grid(row=2,column=5)

window.mainloop()
