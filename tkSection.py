 #import everything
from itertools import count
from tkinter import *       
 #creating empty window   
window=Tk()                    

def fun():
    print(e1_val.get())
    #miles=float(e1_val.get())*1.6
    t1.insert(END,e1_val.get())

b1=Button(window,text="Execute",command=fun)
b1.grid(row=0,column=0)

e1_val=StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()