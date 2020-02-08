from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Orig_window')
# root.iconbitmap('icon.ico')
def open():
	top = Toplevel()
	top.title('New_window')
	top.iconbitmap('icon.ico')
	lbl = Label(top,text='test').pack()
	btn2 = Button(top,text='close window', command=top.destroy).pack()


btn = Button(root, text='open second',command = open).pack()

mainloop()