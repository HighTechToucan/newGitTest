#GUI.py

#Import Librarys
from tkinter import *

global f_num
global operation
f_num=0
operation=''

root = Tk()
root.title("Simple Calc")

entry_widget = Entry(root, width = 35, borderwidth =5) #boarderwidth optional [makes look debossed]
entry_widget.grid(row=0,column=0,columnspan=3, padx = 10, pady = 10)

def button_click(number):
	# entry_widget.delete(0, END)
	current_val=entry_widget.get()
	entry_widget.delete(0, END)
	entry_widget.insert(0,str(current_val) + str(number))
	return
def button_clear():
	entry_widget.delete(0, END)
	global f_num
	f_num = 0
	return
def button_plus():	
	global f_num
	global operation
	f_num = int(entry_widget.get())
	operation = '+'
	entry_widget.delete(0, END)
	return
def button_sub():	
	global f_num
	global operation
	f_num = int(entry_widget.get())
	operation = '-'
	entry_widget.delete(0, END)
	return
def button_mul():	
	global f_num
	global operation
	f_num = int(entry_widget.get())
	operation = '*'
	entry_widget.delete(0, END)
	return
def button_div():	
	global f_num
	global operation
	f_num = int(entry_widget.get())
	operation = '/'
	entry_widget.delete(0, END)
	return
def button_equal():
	current_val=entry_widget.get()
	entry_widget.delete(0, END)
	if operation == '+':
		entry_widget.insert(0, f_num + int(current_val)),
	elif operation == '-':
		entry_widget.insert(0, f_num - int(current_val)),
	elif operation =='*':
		entry_widget.insert(0, f_num * int(current_val)),
	elif operation == '/':
		entry_widget.insert(0, f_num / int(current_val))

	return

#Create_Widgets
button_1 = Button(root, text='1',padx= 40, pady =10,command=lambda: button_click(1))
button_2 = Button(root, text='2',padx= 40, pady =10,command=lambda: button_click(2))
button_3 = Button(root, text='3',padx= 40, pady =10,command=lambda: button_click(3))
button_4 = Button(root, text='4',padx= 40, pady =10,command=lambda: button_click(4))
button_5 = Button(root, text='5',padx= 40, pady =10,command=lambda: button_click(5))
button_6 = Button(root, text='6',padx= 40, pady =10,command=lambda: button_click(6))
button_7 = Button(root, text='7',padx= 40, pady =10,command=lambda: button_click(7))
button_8 = Button(root, text='8',padx= 40, pady =10,command=lambda: button_click(8))
button_9 = Button(root, text='9',padx= 40, pady =10,command=lambda: button_click(9))
button_0 = Button(root, text='0',padx= 40, pady =10,command=lambda: button_click(0))
button_add = Button(root, text='+',padx= 39, pady =10,command=button_plus)
button_equal = Button(root, text='=',padx= 135, pady =10,command=button_equal)
button_clear = Button(root, text='Clear',padx= 29, pady =10,command=button_clear)
button_subtract = Button(root, text='-',padx= 40, pady =10,command=button_sub)
button_multiply = Button(root, text='*',padx= 40, pady =10,command=button_mul)
button_divide = Button(root, text='/',padx= 40, pady =10,command=button_div)

#Position Widgets
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_subtract.grid(row=4,column=2)

button_clear.grid(row=5,column=0)
button_multiply.grid(row=5,column=1)
button_divide.grid(row=5,column=2)

button_equal.grid(row=6,column=0,columnspan=3)

#create loop
root.mainloop()