from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title = 'frame windows'
root.iconbitmap('icon.ico')

r = IntVar()
r.set("2")
# r.get()






Modes = [
('Peperoni','Peperoni'),
('Cheese','Cheese'),
('Onion','Onion'),
]

pizza = StringVar()
# pizza.set('')


frame1 = LabelFrame(root)
frame2 = LabelFrame(root)
frame1.grid(column = 0, row =0)
frame2.grid(column = 1, row =0)

for text,mode in Modes :
	Radiobutton(frame1,text = text, variable = pizza, value = mode).pack(anchor = W)  #command = lambda: clicked(pizza.get())

def clicked(val_in):
	# myLabel = Label(root,text=str(r.get()))
	myLabel = Label(frame2,text=str(val_in))
	myLabel.pack()

# Radiobutton(root,text="Option 1",variable=r,value=1,command = lambda: clicked(r.get())).pack()
# Radiobutton(root,text="Option 2",variable=r,value=2, command = lambda: clicked(r.get())).pack()
myLabel = Label(frame2,text=pizza.get())
myLabel.pack()

myButton = Button(frame1, text='click', command = lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()