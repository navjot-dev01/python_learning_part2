# creating the calculator app 

from tkinter import Widget
from tkinter import *

# function add the values to the entry
def press(num):
    current=display.get()
    display.delete(0,END)
    display.insert(0,current+str(num))

# function to calculate the result
def equal():
    try:
        expression=display.get()
        result=eval(expression)
        display.delete(0,END)           #Delete everything from the first character to the last character.
        display.insert(0,result)        #Insert the result at the beginning of the Entry box.
    except:
        display.delete(0,END)
        display.insert(0,"Error")

# function to clear the display
def clear():
    display.delete(0,END)

def plusminus():
    current = display.get()
    if current:
        value = float(current)
        value = int(value) if value.is_integer() else value
        display.delete(0, END)
        display.insert(0, -value)

def percentage():
    current=display.get()
    if current:
        value = float(current)/100
        value = int(value) if value.is_integer() else value
        display.delete(0,END)
        display.insert(0, value)

def clear_entry():
    expression = display.get()
    while expression and expression[-1].isdigit():
        expression = expression[:-1]
    display.delete(0, END)
    display.insert(0, expression)

def backspace():
    current=display.get()
    value=current[:-1]
    display.delete(0,END)
    display.insert(0,value)

def reciprocal():
    current = display.get()
    if current:
        value = float(current)
        display.delete(0, END)
        display.insert(0, 1/value) 

def square():
    current = display.get()
    if current:
        value = float(current)
        display.delete(0, END)
        display.insert(0, value*value)

def sqroot():
    current = display.get()
    if current:
        value = float(current)
        display.delete(0, END)
        display.insert(0, value**0.5)
#--------------------Creating frame------------------------
root=Tk()
root.title("Calculator")
root.geometry("320x450")
root.configure(bg="#1e1e1e")


display=Entry(root,font=("Arial",20,"bold"),bd=2,insertwidth=4,width=14,justify="right",bg="#1e1e1e",
                fg="white",)
display.grid(row=0,column=0,columnspan=4,pady=10)
# row1
btnper= Button(root,text="%",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=percentage)
btnper.grid(row=1,column=0)

btnCE=Button(root,text="CE",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=clear_entry)
btnCE.grid(row=1,column=1)

btnC= Button(root,text="C",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=clear)
btnC.grid(row=1,column=2)

btnx= Button(root,text="⌫",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=backspace)
btnx.grid(row=1,column=3)

#row 2
btn1divx=Button(root,text="1/x",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=reciprocal)
btn1divx.grid(row=2,column=0)

btnxsq2=Button(root,text="x²",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=square)
btnxsq2.grid(row=2,column=1)

btnsqroot=Button(root,text="√x",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=sqroot)
btnsqroot.grid(row=2,column=2)

btndivide=Button(root,text="÷",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press("/"))
btndivide.grid(row=2,column=3)

#row3
btn7=Button(root,text="7",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press(7))
btn7.grid(row=3,column=0)

btn8=Button(root,text="8",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press(8))
btn8.grid(row=3,column=1)

btn9=Button(root,text="9",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press(9))
btn9.grid(row=3,column=2)

btnX=Button(root,text="X",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press("*"))
btnX.grid(row=3,column=3)

#row4
btn4=Button(root,text="4",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press(4))
btn4.grid(row=3,column=0)

btn5=Button(root,text="5",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press(5))
btn5.grid(row=3,column=1)

btn6=Button(root,text="6",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press(6))
btn6.grid(row=3,column=2)

btnmin=Button(root,text="-",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press("-"))
btnmin.grid(row=3,column=3)

#row5
btn1=Button(root,text="1",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press(1))
btn1.grid(row=5,column=0)

btn2=Button(root,text="2",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press(2))
btn2.grid(row=5,column=1)

btn3=Button(root,text="3",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press(3))
btn3.grid(row=5,column=2)

btnplus=Button(root,text="+",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press("+"))
btnplus.grid(row=5,column=3)

#row6
btnplusmin=Button(root,text="+/-",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=plusminus)
btnplusmin.grid(row=6,column=0)

btnzero=Button(root,text="0",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press(0))
btnzero.grid(row=6,column=1)

btndot=Button(root,text=".",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=lambda:press("."))
btndot.grid(row=6,column=2)

btnequal=Button(root,text="=",width=5,height=2,font=("Arial",18,"bold"),bd=1,command=equal)
btnequal.grid(row=6,column=3)

root.mainloop()