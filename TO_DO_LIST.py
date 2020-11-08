#TO DO LIST DATA BASE AREA

#Import  Sections

from tkinter import *
from tkinter import messagebox
import pickle


#Create Window

root=Tk()
root.title("Office Desk ")
root.geometry('350x421')
root.config(bg='floral white')
root.resizable(width=False,height=False)
#Create Frame

top_frame=Frame(root,width=50,height=20)
top_frame.pack(side=TOP)

right_frame=Frame(root,width=50,height=300,bg='seashell')
right_frame.pack(side=RIGHT)

bottom_frame=Frame(root,bg='seashell')
bottom_frame.pack(side=BOTTOM)

#Create Label

label_top=Label(top_frame,text="OFFICE DESK AREA \n User:AFLAH SEDHIQUE(codeLog:14651)",font=('arial',10,'bold'),bg="papayawhip")
label_top.grid(row=0,column=0)

#Create Display Area

equation=StringVar()
task_input=Entry(right_frame,bg='seashell',width=20,textvariable=equation)
task_input.grid(row=0,column=0,ipady=10)


info_equation=StringVar()
info_input=Entry(right_frame,bg="linen",width=20,textvariable=info_equation)
info_input.grid(row=5,column=0,ipady=5)
#List Box

list_box=Listbox(root,width=35,height=18)
list_box.configure(bg='seashell')
list_box.pack()


#Function Declaration-1

def add_task():
    task = task_input.get()
    if task !="":
        list_box.insert(END, task)
        task_input.delete(0, END)
    else:
        messagebox.showinfo(title="Task Prompt",message="Please Type A Task.")

def delete_task():
    try:
        task_select = list_box.curselection()[0]
        list_box.delete(task_select)

    except:
        messagebox.showinfo(title='Delete Prompt',message='Please Select A Task')

#Other Utility Functions

expression=""

def log_out():
    global expression
    info_equation.set("LOGED OUT")
    equation.set("CLOSED!!!!!!")
    expression=""

def shut_down():
    root.destroy()

def log_in():
    global expression
    info_equation.set("Loged In :(14651)")
    equation.set("")
    expression=""

def close_access():
    global expression
    equation.set("ACCESS CLOSED")
    info_equation.set('')
    expression=''

def star_meeting():
    global expression
    messagebox._show(title='Meeting.',message='Access Will Be Closed')
    info_equation.set("MEETING STARTED!!!")


def on_conference():
    global expression
    messagebox.showinfo(title='On Call',message='On AIR!!')
    equation.set("On Conference:")
    info_equation.set("14651:On Call")
    expression=""

def office_desk():
    global expression
    messagebox.showinfo(title='Office Desk',message='Office Desk On Call')
    info_equation.set("Office Desk: On Call")

def end_c():
    global expression
    messagebox.showinfo(title='End',message='C/C ENDED!')
    equation.set("")
    info_equation.set("")
    expression=''



#Function Declaration-2
def save_task():
    task_save=list_box.get(0,list_box.size())
    pickle.dump(task_save,open("memoryblock.dat",'wb'))
    list_box.delete(0,END)

def load_task():
    task_load=pickle.load(open('memoryblock.dat','rb'))
    list_box.delete(0,END)

    for task_load in task_load:
        list_box.insert(END,task_load)






#Button List

button_1=Button(right_frame,text='Add Task',bg='cornsilk',command=lambda :add_task())
button_1.grid(row=1,column=0,pady=8)

button_2=Button(right_frame,text='Save Task',bg='cornsilk',command=lambda :save_task())
button_2.grid(row=2,column=0,pady=8)

button_3=Button(right_frame,text='Delete Task',bg='cornsilk',command=lambda :delete_task())
button_3.grid(row=3,column=0,pady=8)

button_4=Button(right_frame,text='Load Tasks',bg='cornsilk',command=lambda :load_task())
button_4.grid(row=4,column=0,pady=8)

# Other Utility Buttons

button_5=Button(bottom_frame,text='Office Desk',bg='rosy brown',font=('verdana',8,'bold'),command=lambda :office_desk())
button_5.grid(row=0,column=0,padx=4)

button_6=Button(bottom_frame,text='Log Out',bg='rosy brown',font=('verdana',10,'bold'),command=lambda :log_out())
button_6.grid(row=0,column=1)

button_7=Button(bottom_frame,text='Shut Down',bg='rosy brown',bd=4,font=('verdana',10,'bold'),command=lambda :shut_down())
button_7.grid(row=1,column=1,pady=4)

button_8=Button(bottom_frame,text='Log in',bg='rosy brown',bd=4,font=('verdana',10,'bold'),command=lambda :log_in())
button_8.grid(row=1,column=0,pady=4)

button_9=Button(right_frame,text='Start Meeting',bg='rosy brown',bd=4,relief='sunken',command=lambda :star_meeting())
button_9.grid(row=7,column=0,pady=4)

button_10=Button(right_frame,text='Close Access',bg='rosy brown',bd=4,relief='sunken',command=lambda :close_access())
button_10.grid(row=6,column=0,pady=4)

button_11=Button(right_frame,text='On Conference',bg='rosy brown',bd=4,width=15,relief='ridge',command=lambda :on_conference())
button_11.grid(row=8,column=0,pady=4)

button_12=Button(right_frame,text='END(c/c)',bg='rosy brown',bd=4,width=10,font=("couriernew",9,'bold'),relief='ridge',command=lambda :end_c())
button_12.grid(row=9,column=0)



























#MAIN LOOP
root.mainloop()