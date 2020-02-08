from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import os

root = Tk()
root.title('Orig_window')
# root.iconbitmap('icon.ico')
location = os.getcwd()
# print(location)
# 'C:\\Users\\ts299\\Documents\\GitHub\\newGitTest"
# 
def open ():
	global my_image
	root.filename = filedialog.askopenfilename(initialdir = os.path.join(location,"images"),title = "Select file",filetypes = (("all Files","*.*"),("python","*.py"),("excel files","*.xlsx")))
	my_image_label.gridforget()
	my_label = Label(root, text = root.filename).pack()
	my_image = ImageTk.PhotoImage(Image.open(root.filename))
	my_image_label = Label(image=my_image).pack()


btn = Button(root,command = open).pack()
# def open():
# 	top = Toplevel()
# 	top.title('New_window')
# 	top.iconbitmap('icon.ico')
# 	lbl = Label(top,text='test').pack()
# 	btn2 = Button(top,text='close window', command=top.destroy).pack()
# btn = Button(root, text='open second',command = open).pack()

mainloop()