from tkinter import*
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk () #spawn app
GUI.title ('game savings')
GUI.geometry ('400x400')

##############
def Button1 () :
       text = 'now have 600 gem'
       messagebox.showinfo('inv',text)
FB1= LabelFrame(GUI)
FB1.place(x=200,y= 200)
B1 = ttk.Button (GUI,text='day 1',command = Button1)
B1.pack (ipadx =15,ipady=15)

##############
def Button2 () :
       text = 'now have 750 gem'
       messagebox.showinfo('inv',text)

FB1 = LabelFrame(GUI)
FB1.place(x=100,y=400)
B2 = ttk.Button (FB1,text='day 2',command=Button2)
B2.pack (ipadx =40,ipady=40)
###############

##############
def Button3 () :
       text = 'now have 800 gem'
       messagebox.showinfo('inv',text)

FB1 = LabelFrame(GUI)
FB1.place(x=100,y=300)
B3 = ttk.Button (FB1,text='day 3',command=Button3)
B3.pack (ipadx =40,ipady=40)
#########################
def Button4 () :
       text = 'now have 920 gem'
       messagebox.showinfo('inv',text)

FB1 = LabelFrame(GUI)
FB1.place(x=300,y=300)
B4 = ttk.Button (FB1,text='day 4',command=Button4)
B4.pack (ipadx =40,ipady=40)

def Button5 () :
       text = 'now have 500 gem'
       messagebox.showinfo('inv',text)

FB1 = LabelFrame(GUI)
FB1.place(x=300,y=400)
B5 = ttk.Button (FB1,text='day 1',command=Button5)
B5.pack (ipadx =40,ipady=40)

GUI.mainloop ()

