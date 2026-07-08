# this .py file explains in file tkinter_basics.py

from tkinter import font        
import tkinter as tk            
from tkinter import *           
from tkinter import ttk         

#  1. labels

root = Tk(screenName=None, baseName='hello_world', className='My first app', useTk=1)
# using the normal tkinter
root=Tk()
labels=tk.Label(root,text="Hello World")
labels.pack()



# using the themed tkinter
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)
root.mainloop()

# 2. Buttons

root=Tk()
root.title("My first button")

tk.Button(root,text="Click me",bg="red",fg="white",font=("Arial",20, "bold")).pack()
tk.Button(root,text="Exit",command=root.destroy).pack()

root.mainloop()

# 3. Entry 

root=Tk()
root.title("My first Entry")

tk.Label(root,text="Enter your name", font=font.Font(family="Arial",size=20,weight="bold")).grid(row=0,column=0, padx=10, pady=10)

entry=tk.Entry(root,width=20,font=font.Font(family="Arial",size=15)).grid(row=0,column=1, padx=10, pady=10)


# 4. Check buttons

root=Tk()

# in the check buttons we can select the multiple options

root.title("My check buttons")

var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()

tk.Checkbutton(root,text="Python",variable=var1).grid(row=0,column=0,sticky=tk.W)
tk.Checkbutton(root,text="Java",variable=var2).grid(row=1,column=0,sticky=tk.W)
tk.Checkbutton(root,text="C++",variable=var3).grid(row=2,column=0,sticky=tk.W)

# 5. Radio buttons
# in the radio buttons we can select only one option ,if we select one option then no other option CAN GET SELECTED 
# if selected then previous option will be deselected


root=Tk()

root.title("My radio buttons")


var=tk.IntVar()

tk.Radiobutton(root,text="Python",variable=var,value=1,anchor=tk.W).grid(row=0,column=0,sticky=tk.W)
tk.Radiobutton(root,text="Java",variable=var,value=2,anchor=tk.W).grid(row=1,column=0,sticky=tk.W)
tk.Radiobutton(root,text="C++",variable=var,value=3,anchor=tk.W).grid(row=2,column=0,sticky=tk.W)

root=Tk()
root.title("Listbox")

listbox=tk.Listbox(root,height=5,width=20)
listbox.pack()

listbox.insert(1,"Python")
listbox.insert(2,"Java")
listbox.insert(3,"C++")
listbox.insert(4,"C#")
listbox.insert(5,"Python")

root.mainloop()