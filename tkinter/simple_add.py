# # Simple calculator with four operations
from tkinter import *

root=Tk()
# root.title("Simple Four ops Calculator")

# def add():
#     num1=int(entry1.get())
#     num2=int(entry2.get())
#     result=num1+num2
#     label.config(text="Result: "+str(result))

# def sub():
#     num1=int(entry1.get())
#     num2=int(entry2.get())
#     result=num1-num2
#     label.config(text="Result: "+str(result))

# def mul():
#     num1=int(entry1.get())
#     num2=int(entry2.get())
#     result=num1*num2
#     label.config(text="Result: "+str(result))

# def div():
#     num1=int(entry1.get())
#     num2=int(entry2.get())
#     result=num1/num2
#     label.config(text="Result: "+str(result))

# label1=Label(root,text="Enter first number")
# label1.pack()
# entry1=Entry(root)
# entry1.pack()

# label2=Label(root,text="Enter second number")
# label2.pack()
# entry2=Entry(root)
# entry2.pack()

# btn=Button(root,text="Add",command=add)
# btn.pack()

# btn1=Button(root,text="Subtract",command=sub)
# btn1.pack()

# btn2=Button(root,text="Multiply",command=mul)
# btn2.pack()

# btn3=Button(root,text="Divide",command=div)
# btn3.pack()

# label=Label(root,text="Result: ")
# label.pack()


# Student marks % age calculator
root.title("Persentage Calculator")
def calculate():
    m1=int(e1.get())
    m2=int(e2.get())
    m3=int(e3.get())
    marks=m1+m2+m3
    per=marks/300*100
    label1.config(text="Total Marks obtained "+str(marks)+"out of 300 ",fg="green",font=("Arial",20,"bold"))
    label2.config(text=" Percentage "+str(per)+"%",fg="green",font=("Arial",20,"bold"))
    
root=Tk()
root.title("Marks Calculator")

label1=Label(root,text="Enter marks of 3 subjects:")
label1.pack()

e1=Entry(root)
e1.pack()
e2=Entry(root)
e2.pack()
e3=Entry(root)
e3.pack()

btn=Button(root,text="Calculate",command=calculate)
btn.pack()
label1=Label(root,text="")
label1.pack()
label2=Label(root,text="")
label2.pack()

root.mainloop()
