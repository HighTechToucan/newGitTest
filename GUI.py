#GUI.py

#Import Librarys
# import tkinter
from tkinter import *

root = Tk()

# Create a Label widget
myLabel = Label(root, text = 'Hello World!')
myLabel2 = Label(root, text = 'My name is TBC')

# #Shoving it onto the screen
# myLabel.pack()

myLabel.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

#create loop
root.mainloop()