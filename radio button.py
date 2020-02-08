from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title = 'frame windows'
root.iconbitmap('icon.ico')

RadioButton(root,text="Option 1",variable=r,value=1).pack()
RadioButton(root,text="Option 2",variable=r,value=2).pack()




root.mainloop()