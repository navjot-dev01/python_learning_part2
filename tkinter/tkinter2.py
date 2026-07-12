from tkinter import Listbox
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("Button Events")
root.geometry("600x400")

# -------------------------Handclicking Events--------------------------

def click_handler():
    print("Button Clicked")
    messagebox.showinfo("Button Clicked")
   
btn=tk.Button(root,text="Click Me",command=click_handler)
btn.configure(fg="white",bg="red",font=("Arial",20,"bold"))           #changes the button’s properties after creation.
btn.pack()

# --------taking the input and then presenting the message-----
label=tk.Label(root,text="Enter your name")
label.pack()
entry=tk.Entry(root)
entry.pack()

def click_handler():
    messagebox.showinfo("Data Saved Successfully",entry.get())

btn=tk.Button(root,text="Click Me",command=click_handler)
btn.configure(fg="white",bg="red",font=("Arial",20,"bold"))

btn.pack()

# Scroll bar in the listbox

root.title("Scroll Bar")
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox=tk.Listbox(root,yscrollcommand=scrollbar.set,height=5)

listbox.insert(1,"Python")
listbox.insert(2,"Java")
listbox.insert(3,"C++")
listbox.insert(4,"C#")
listbox.insert(5,"Python")
listbox.insert(6,"Java")
listbox.insert(7,"Ruby")
listbox.insert(8,"Java Script")
listbox.pack(side=tk.LEFT,fill=tk.BOTH)     #Places the listbox on the left side of the window.
                                         # fill=tk.BOTH → expands both horizontally and verticall
scrollbar.config(command=listbox.yview)

# ---------------- Creating the menu----------------------- 

root.title("My First Menu")
menu=tk.Menu(root)
root.config(menu=menu)     # Attaches the menubar to your window (root).


filemenu=tk.Menu(menu)      # Creates a submenu called File.
menu.add_cascade(label="File",menu=filemenu) # Adds it to the menubar with the label “File”.

filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)

# Adding the edit menu
editmenu=tk.Menu(menu)
menu.add_cascade(label='Edit',menu=editmenu)

editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
editmenu.add_separator()
editmenu.add_command(label='Exit',command=root.destroy)

# Adding the help menu
helpmenu=tk.Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)

helpmenu.add_command(label='About')
helpmenu.add_command(label='Help')

# Combobox # imported from the ttk(themeded tkinter) library
from tkinter import ttk

root.title("Combobox")

label=tk.Label(root,text="Select your country",font=('Arial',15,"bold")).pack()
country=tk.StringVar()

combobox=ttk.Combobox(root,textvariable=country,values=("India","USA","UK","Canada","Australia"))
combobox.pack(pady=5)


combobox.set("India")
combobox.bind("<<ComboboxSelected>>",lambda e:print(country.get()))
# "<<ComboboxSelected>>" → this is a special event in Tkinter.
# It happens when the user picks an item from the Combobox list.


# Scaling (Sliders)
root.title("Scaling")

scale=tk.Scale(root,from_=0,to=100,orient=tk.HORIZONTAL)
scale2=tk.Scale(root,from_=0,to=100,orient=tk.VERTICAL)

scale.pack()
scale2.pack()

root.mainloop()