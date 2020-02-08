from tkinter import * 
from tkinter import filedialog

root = Tk()
root.title("Target Word Analysis")
root.iconbitmap('HTT.ico')

filepath=""
searchterm=""

frame1 = LabelFrame(root, text = "Select File", pady=10, padx =10)
frame2 = LabelFrame(root, text = "Enter Target Term", pady=10, padx =10)
frame3 = LabelFrame(root, text = "Review & Submit", pady=10, padx =10)

def openfile():
	global address_label
	global searchterm
	global filepath
	global frame3_label
	filepath=filedialog.askopenfilename(initialdir="/", title = "Select 'Wordsmith Concordance' Excel Document", filetypes = (("MS Excel files","*.xlsx"),("all Files","*.*"))   )
	address_label.grid_forget()
	address_label = Label(frame1, text = filepath ,relief=SUNKEN, borderwidth =1, bg="white")
	address_label.grid(column = 0, row =1,padx=1, sticky = W+E)
	if not searchterm == "" : 
		frame3_label = Label(frame3, text = "Searching '{}'' for the string '{}'".format( filepath,searchterm))
		frame3_label.grid(column=0,row=0)
		go_button = Button(frame3, text="Submit")
		go_button.grid(column=0, row=1)

def getsearchterm(searchterm_in):
	global searchterm
	global filepath
	global frame3_label
	searchterm = searchterm_in
	if not filepath == "" :
		frame3_label = Label(frame3, text = "Searching '{}'' for the string '{}'".format( filepath,searchterm))
		frame3_label.grid(column=0,row=0)
		go_button = Button(frame3, text="Submit")
		go_button.grid(column=0, row=1)


frame1_title = Label(frame1, text = "'Wordsmith Concordance' Excel Document Filepath:",anchor = W)
frame1_title.grid(column = 0, row =0,sticky=W)
address_label = Label(frame1, text = "" ,relief=SUNKEN, borderwidth =1, bg="white")
address_label.grid(column = 0, row =1 ,padx=1, sticky = W+E)
address_button = Button(frame1, text = "Open",command=openfile, anchor = E)
address_button.grid(column=1,row=1, sticky = E)

search_entry = Entry(frame2)
search_entry.grid(column = 0, row = 1)
search_entry_button = Button(frame2, text="apply", command=lambda: getsearchterm(search_entry.get()), anchor = W)
search_entry_button.grid(column=1,row=1,sticky=W)

go_button = Button(frame3, text="Submit", state=DISABLED)
go_button.grid(column=0, row=1)

copyright_label = Label(root, text="Copyright High Tech Toucan 2020",anchor=E)


frame1.grid(column = 0, row = 0,sticky = W+E)
frame2.grid(column = 0, row = 1,sticky = W+E)
frame3.grid(column = 0, row = 3,sticky = W+E)
copyright_label.grid(column=0,row=4, sticky = E)


mainloop()