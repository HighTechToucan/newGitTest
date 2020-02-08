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
image_number = 0

#Functions
def Button_Commands ():
	global button_previous
	global button_advance
	global status_string
	
	status_string = Label(root, text = 'Image {} of {}'.format(image_number,len(img_list)),bd=1,relief=SUNKEN, anchor = W)

	if image_number == 0:
		button_previous = Button (root, text='<', state=DISABLED, anchor = E)
	else:
		button_previous = Button(root,text='<',command = lambda:back((image_number-1)), anchor = E)
	if image_number == len(img_list)-1:
		button_advance = Button (root, text='>', state=DISABLED, anchor = W)
	else:
		button_advance = Button(root,text='>',command = lambda:forward((image_number+1)), anchor = W)

	status_string.grid(row=2,column=1,columnspan=3,pady = 10, padx=10, sticky = W+E)
	my_label.grid(row=3, column=1,columnspan = 3)
	button_previous.grid(row=1,column=0)
	button_advance.grid(row=1,column=2)

def forward(image_number_in):
	global my_label
	global Button_Commands
	global image_number
	image_number = image_number_in % len(img_list)

	#Triggers
	my_label.grid_forget()
	my_label = Label(image=img_list[image_number])
	Button_Commands()

	#Position
	# my_label.grid(row=2, column=1,columnspan = 3)
	# button_previous.grid(row=1,column=0)
	# button_advance.grid(row=1,column=2)
	return

def back(image_number_in):
	global my_label
	global Button_Commands
	global image_number
	image_number = image_number_in  % len(img_list)

	#Triggers
	my_label.grid_forget()
	my_label = Label(image=img_list[image_number])
	Button_Commands()

	#Position
	# my_label.grid(row=2, column=1,columnspan = 3)
	# button_previous.grid(row=1,column=0)
	# button_advance.grid(row=1,column=2)
	return	



#Create_Widgets
my_label = Label(image=my_img1)
button_quit = Button(root, text='Exit Program', command = root.quit)
Button_Commands()

#Position Widgets
# my_label.grid(row=2, column=1,columnspan = 3)
# button_previous.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
# button_advance.grid(row=1,column=2)

#create loop
root.mainloop()