from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.geometry("400x400")


vertical = IntVar()



vertical = Scale(root, from_=100 , to=0)
horizontal = Scale(root, from_=0 , to=100, orient = HORIZONTAL)
vertical.pack()
horizontal.pack()



def slide():
	global my_label
	global vertical
	my_label = Label(root, text = vertical.get()).pack()


my_button = Button(root, text = "click me",command = slide).pack()
my_label = Label(root, text = vertical.get()).pack()

mainloop()