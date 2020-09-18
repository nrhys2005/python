from tkinter import *
import pickle

window = Tk()

filename = 'phone_book.dat'
phone_book = {}

def do_add() :
    global phone_book
    name = e1.get()
    phone = e2.get()
    if name and phone : 
        phone_book[name]=phone
        outfile = open(filename,'wb')
        pickle.dump(phone_book, outfile)
        outfile.close()
    else :
        print ("에러: 입력이 제대로 되지 않음.")
    
def do_begin() :
    names = list(phone_book.keys())
    names.sort()
    if len(names) == 0 : 
        print ("에러: 내용이 없음.")
        return 
    e1.delete(0,END);
    e2.delete(0,END)
    e1.insert(0,names[0]);
    e2.insert(0,phone_book[names[0]])
    
def do_next() :
    names = list(phone_book.keys())
    names.sort()
    if len(names) == 0 : 
        print ("에러: 내용이 없음.")
        return 
    name=e1.get()
    if len(name) == 0 : 
        print ("에러: 이름에 내용이 없음.")
        return 
    i = names.index(name)
    if i == len(names)-1 :
        pass
    else :
        i += 1  
        e1.delete(0,END);
        e2.delete(0,END)
        e1.insert(0,names[i]);
        e2.insert(0,phone_book[names[i]])
    
def do_prev() :
    names = list(phone_book.keys())
    names.sort()
    if len(names) == 0 : 
        print ("에러: 내용이 없음.")
        return 
    name=e1.get()
    if len(name) == 0 : 
        print ("에러: 이름에 내용이 없음.")
        return 
    i = names.index(name)
    if i == 0 :
        pass
    else :
        i -= 1
        e1.delete(0,END);
        e2.delete(0,END)
        e1.insert(0,names[i]);
        e2.insert(0,phone_book[names[i]])       
    
def dO_final() :
    names = list(phone_book.keys())
    names.sort()
    e1.delete(0,END);
    e2.delete(0,END)
    e1.insert(0,names[-1]);
    e2.insert(0,phone_book[names[-1]])
    
def do_read() :
    global phone_book
    try: 
        infile = open(filename,'rb')
    except:
        print ("예러: 파일 오픈 실패:", filename)
    else :
        phone_book = pickle.load(infile)
        infile.close()
        do_begin()
        
l1 = Label(window, text='이름');
l2 = Label(window, text='전화번호')
l1.grid(row=0, column=0);
l2.grid(row=1, column=0)    

e1 = Entry(window, width =30);
e2 = Entry(window, width =30)
e1.grid(row=0,column=1,columnspan=5)
e2.grid(row=1,column=1,columnspan=5) 

b1 = Button(window, text='추가', command =do_add)
b2 = Button(window, text='처음', command = do_begin)
b3 = Button(window, text='이전', command = do_prev)
b4 = Button(window, text='다음', command = do_next)
b5 = Button(window, text='마지막', command = dO_final)
b6 = Button(window, text='파일읽기', command = do_read)

b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
b4.grid(row=2,column=3)
b5.grid(row=2,column=4)
b6.grid(row=2,column=5)

do_read()
window.mainloop()
