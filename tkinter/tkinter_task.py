# Q1. Student Information Form
# Create a GUI application that accepts the following details from the user:

#     Student Name
#     Roll Number
#     Course
# Add a button. When the button is clicked, show_info all entered information in a message box.
import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Student Information Form")

tk.Label(root ,text="Student Name").grid(row=0, column=0, padx=10,pady=5)
name_entry=tk.Entry(root,width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root ,text="Roll Number").grid(row=1, column=0, padx=10,pady=5)
rollno_entry=tk.Entry(root,width=30)
rollno_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root ,text="course").grid(row=2, column=0, padx=10,pady=5)
course_entry=tk.Entry(root,width=30)
course_entry.grid(row=2, column=1, padx=10, pady=5)

def showinfo():
    info=(f"Name:{name_entry.get()}\nRoll Number:{rollno_entry.get()}\nCourse:{course_entry.get()}")
    messagebox.showinfo("Student Information",info)

tk.Button(root,text="Submit",command=showinfo).grid(row=3,column=1,pady=10)

root.mainloop()
    
# Q2. Course Registration System
# Create a GUI application that allows students to select courses using checkboxes.
# Available Courses:

#     Python
#     Java
#     Data Science
#     Machine Learning
#     Web Development
# When the user clicks the button, show_info all selected courses in a message box.

root.title("Course Registration System")

var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()
var4=tk.IntVar()
var5=tk.IntVar()

tk.Checkbutton(root,text="Python",variable=var1).grid(row=0,column=0,sticky=tk.W)
tk.Checkbutton(root,text="Java",variable=var2).grid(row=1,column=0,sticky=tk.W)
tk.Checkbutton(root,text="Data Science",variable=var3).grid(row=2,column=0,sticky=tk.W)
tk.Checkbutton(root,text="Machine Learning",variable=var4).grid(row=3,column=0,sticky=tk.W)
tk.Checkbutton(root,text="Web Development",variable=var5).grid(row=4,column=0,sticky=tk.W)

def show_courses():
    selected = []
    if var1.get(): selected.append("Python")
    if var2.get(): selected.append("Java")
    if var3.get(): selected.append("Data Science")
    if var4.get(): selected.append("Machine Learning")
    if var5.get(): selected.append("Web Development")
    messagebox.showinfo("Selected Courses", ", ".join(selected))

tk.Button(root, text="Submit", command=show_courses).grid(row=5, column=0, pady=10)

root.mainloop()


# Q3. Feedback Collector
# Create a feedback system where users can rate a training session using radio buttons.
# Ratings:

#     Excellent
#     Good
#     Average
#     Poor
# When the user clicks , show_info the selected rating using messagebox.
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Feedback Collector")

rating_var = tk.StringVar(value=" ")

tk.Radiobutton(root, text="Excellent", variable=rating_var, value="Excellent").pack(anchor="w")
tk.Radiobutton(root, text="Good", variable=rating_var, value="Good").pack(anchor="w")
tk.Radiobutton(root, text="Average", variable=rating_var, value="Average").pack(anchor="w")
tk.Radiobutton(root, text="Poor", variable=rating_var, value="Poor").pack(anchor="w")

def show_rating():
    messagebox.showinfo("Feedback", f"Selected Rating: {rating_var.get()}")

tk.Button(root, text="Submit", command=show_rating).pack(pady=10)
root.mainloop()



# Q4. Employee Details Manager
# Create a GUI form that accepts:

#     Employee Name
#     Employee ID
#     Department
# When the user clicks the button, show_info all employee information inside a Text widget.
import tkinter as tk

root = tk.Tk()
root.title("Employee Details Manager")

tk.Label(root, text="Employee Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Employee ID").grid(row=1, column=0, padx=10, pady=5)
id_entry = tk.Entry(root, width=30)
id_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Department").grid(row=2, column=0, padx=10, pady=5)
dept_entry = tk.Entry(root, width=30)
dept_entry.grid(row=2, column=1, padx=10, pady=5)

text_box = tk.Text(root, height=5, width=40)
text_box.grid(row=4, column=0, columnspan=2,padx=10, pady=10)

def show_employee():
    info = f"Name: {name_entry.get()}\nID: {id_entry.get()}\nDepartment: {dept_entry.get()}"
    text_box.insert(tk.END, info + "\n")

tk.Button(root, text="Submit", command=show_employee).grid(row=3, column=1, pady=10)

root.mainloop()


# Q5. Country Selection Application
# Create a GUI application containing a Combobox with the following countries:

#     India
#     Canada
#     Australia
#     Germany
#     Japan

# When the user clicks the button, show_info the country in the message box.
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Country Selection")

countries = ["India", "Canada", "Australia", "Germany", "Japan"]

combo = ttk.Combobox(root, values=countries)
combo.set("Select Country")
combo.pack(pady=10)

def show_country():
    messagebox.showinfo("Selected Country", f"You selected: {combo.get()}")

tk.Button(root, text="Submit", command=show_country).pack(pady=10)

root.mainloop()


# Q6. Login Window
# Create a Login Form containing:

#     Username
#     Password

# Requirements:

#     Password should be hidden using the appropriate Entry widget property.
#     If Username = and Password = , show_info "Login Successful".
#     Otherwise show_info "Invalid Credentials".
#     You can use the messagebox to show_info
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Window")

tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=5)
user_entry = tk.Entry(root, width=30)
user_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=5)
pass_entry = tk.Entry(root, width=30, show="*")
pass_entry.grid(row=1, column=1, padx=10, pady=5)

def login():
    if user_entry.get() == "admin" and pass_entry.get() == "1234":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid Credentials")

tk.Button(root, text="Login", command=login).grid(row=2, column=1, pady=10)

root.mainloop()

