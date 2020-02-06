#GUI.py

#Import Librarys
from tkinter import *
# import tkinter
from PIL import Image,ImageTk

#Setup Tkinter loop & Title
root = Tk()
root.title("")

#Set Icon
root.iconbitmap('icon.ico')

#Define Images
my_img1 = ImageTk.PhotoImage(Image.open("images/test.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/test2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/test3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/test4.png"))
img_list = [my_img1,my_img2,my_img3,my_img4]

#Functions
def forward(image_number):
	global my_label
	global button_advance
	global button_previous

	my_label.grid_forget()
	my_label = Label(image=img_list[image_number-1])
	# button_advance = Button(root,text='>',command = lambda:forward((image_number+1) % len(img_list) ) )
	# button_previous = Button(root,text='<',command = lambda:back((image_number-1) % len(img_list)))
	button_advance = Button(root,text='>',command = lambda:forward((image_number+1)))
	button_previous = Button(root,text='<',command = lambda:back((image_number-1)))
	if image_number == len(img_list):#len(img_list):
		button_advance = Button (root, text='>', state=DISABLED)
	# else:
	# 	button_advance = Button(root,text='>',command = lambda:forward((image_number+1) % len(img_list) ) )
	my_label.grid(row=2, column=1,columnspan = 3)
	button_previous.grid(row=1,column=0)
	button_advance.grid(row=1,column=2)

	return

def back(image_number):
	global my_label
	global button_advance
	global button_previous

	my_label.grid_forget()
	my_label = Label(image=img_list[image_number-1])
	# button_advance = Button(root,text='>',command = lambda:forward((image_number+1) % len(img_list) ) )
	# button_previous = Button(root,text='<',command = lambda:back((image_number-1) % len(img_list)))
	button_advance = Button(root,text='>',command = lambda:forward((image_number+1)))
	button_previous = Button(root,text='<',command = lambda:back((image_number-1)))
	if image_number == 1:#len(img_list):
		button_previous = Button (root, text='<', state=DISABLED)
	my_label.grid(row=2, column=1,columnspan = 3)
	button_previous.grid(row=1,column=0)
	button_advance.grid(row=1,column=2)

	return	


#Create_Widgets
my_label = Label(image=my_img1)
button_quit = Button(root, text='Exit Program', command = root.quit)
button_advance = Button(root,text='>',command = lambda:forward(2) )
button_previous = Button(root,text='<',command = lambda:back(),state=DISABLED)


#Position Widgets
my_label.grid(row=2, column=1,columnspan = 3)
button_previous.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_advance.grid(row=1,column=2)

#create loop
root.mainloop()