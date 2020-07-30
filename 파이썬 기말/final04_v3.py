from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter import filedialog as fd

im = None
tk_img = None
fname = None
def do_open():
    global im, tk_img,fname
    fname= fd.askopenfilename()
    im= Image.open(fname)
    tk_img= ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

def do_quit():
    window.destroy()

def image_rotate():
    global im, tk_img
    im = im.rotate(45)
    tk_img= ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

def image_blur():
    global im, tk_img
    im = im.filter(ImageFilter.BLUR)
    tk_img= ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

def do_save():
    global im
    ftypes=[] 
    fname=fd.asksaveasfilename(initialdir="/",title="Select file",filetypes=(("Image file","png"),("All files","*")),defaultextension=".png")

def com1():
    global im, tk_img,fname
def com2():
    global im, tk_img,fname
    im= Image.open(fname)
    imageWithEdges = im.filter(ImageFilter.gaussianblur)
    tk_img= ImageTk.PhotoImage(imageWithEdges)
    canvas.create_image(250, 250, image=tk_img)
    window.update()
def com3():
    global im, tk_img,fname
    im= Image.open(fname)
    imageWithEdges = im.filter(ImageFilter.FIND_EDGES)
    tk_img= ImageTk.PhotoImage(imageWithEdges)
    canvas.create_image(250, 250, image=tk_img)
    window.update()
def com4():
    do_save()
    
window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

menubar= tk.Menu(window)
filemenu= tk.Menu(menubar)
ipmenu= tk.Menu(menubar)
filemenu.add_command(label="열기", command= do_open )
filemenu.add_command(label="저장", command= do_save )
filemenu.add_command(label="종료", command= do_quit )
ipmenu.add_command(label="영상회전", command=image_rotate )
ipmenu.add_command(label="영상흐리게", command=image_blur )
ipmenu.add_command(label="영상선명하게", command=com1 )
ipmenu.add_command(label="영상엣지검출", command=com2 )
ipmenu.add_command(label="취소", command=com3 )
ipmenu.add_command(label="완료", command=com4 )
menubar.add_cascade(label="파일", menu=filemenu)
menubar.add_cascade(label="영상처리", menu=ipmenu)

window.config(menu=menubar)
window.mainloop()
