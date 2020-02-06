#GUI.py

#Import Librarys
# import tkinter
from tkinter import *

root = Tk()

entry_widget = Entry(root, width = 50) #boarderwidth optional [makes look debossed]
entry_widget.pack()
entry_widget.insert(0,'Enter your name here')

def myClick():
	out_string = 'Hi ' + entry_widget.get()
	myLabel = Label(root,text=out_string)
	myLabel.pack()

#create button widget
my_button = Button(root, text='Submit',padx=50, pady = 5, command = myClick, fg='blue') #NB DONT put in parenthasis for called functions
#fg = text colour - use hex colour codes
#bg = background colour - use hex colour codes

#position
my_button.pack()

#create loop
root.mainloop()