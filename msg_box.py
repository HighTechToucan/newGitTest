from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image



root = Tk()
root.title = 'frame windows'
root.iconbitmap('icon.ico')



frame1 = LabelFrame(root, text = 'this is my frame1', padx=10,pady=10)
frame2 = LabelFrame(root, text = 'this is my frame2', padx=10,pady=10)
frame3 = LabelFrame(root, text = 'this is my frame3', padx=10,pady=10)
frame1.grid(column = 0, row =0)
frame2.grid(column = 1, row =0)
frame3.grid(column = 2, row =0)

def popup_info():
	messagebox.showinfo('Title','Message')
	#INFORMATION ONLY :      showinfo, showwarning, showerror

def popup_question():
	response = messagebox.askyesno('Title','Message')
	Label(frame1, text=response).pack()
	#RESPONSE :      askokcancel, askyesno (RETURNS 1 / 0) askquestion (RETURNS 'Yes' / 'No')
	if response == 1:
		Label(frame2, text='clicked yes').pack()
	else : 
		Label(frame2, text='clicked no').pack()

Button(frame1,text = 'popup',command=popup_info).pack()
Button(frame1,text = 'popup',command=popup_question).pack()





# b= Button(frame1, text = 'b1')
# b.pack()
# b2= Button(frame2, text = 'b2')
# b2.pack()
# b3= Button(frame3, text = 'b3')
# b3.pack()

root.mainloop()