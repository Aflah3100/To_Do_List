#TO DO LIST DATA BASE AREA

#Import  Sections

from tkinter import *
from tkinter import messagebox
import pickle


#Create Window

root=Tk()
root.title("Office Desk ")
root.geometry('350x400')
root.config(bg='floral white')

#Create Frame

top_frame=Frame(root,width=50,height=20)
top_frame.pack(side=TOP)

right_frame=Frame(root,width=50,height=20)
right_frame.pack(side=RIGHT)

bottom_frame=Frame(root)
bottom_frame.pack(side=BOTTOM)

#Create Label

label_top=Label(top_frame,text="OFFICE DESK AREA \n User:AFLAH SEDHIQUE(codeLog:14651)",font=('arial',10,'bold'),bg="papayawhip")
label_top.pack()

#Create Display Area

task_input=Entry(right_frame,bg='seashell',width=20)
task_input.pack(ipady=20)

#List Box

list_box=Listbox(root,width=35,height=19)
list_box.configure(bg='seashell')
list_box.pack()













#MAIN LOOP
root.mainloop()