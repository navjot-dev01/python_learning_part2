print("="*15 + "Student Management System - Dashboard" + "="*15)


from tkinter import *
from tkinter import messagebox
import tkinter as tk

root=Tk()
root.geometry("600x400")
root.title("Student Management System")

# temporary storage for registered students
students = {}

# create a frame inside root
home_frame=Frame(root,bg="#E4E0E0")
login_frame=Frame(root,bg="#F1F5F9")
register_frame=Frame(root,bg="#FFFFFF")
dashboard_frame=Frame(root,bg="#F8FAFC")

for frame in (home_frame,login_frame,register_frame,dashboard_frame):
    frame.place(relheight=1,relwidth=1)
    
    # def show_home():
    #     home_frame.tkraise()

    # def show_register():
    #     register_frame.tkraise()    
    
    # def show_login():
    #     login_frame.tkraise()

    # def show_dashboard():
    #     dashboard_frame.tkraise()
# show_home()    

                                          #OR
    def show_frame(frame):
        frame.tkraise()                                      

show_frame(home_frame)

# Student Registration Function
def register_student():
    name = reg_name.get()
    email = reg_email.get()
    mobile = reg_mobile.get()
    password = reg_password.get()
    confirm_password = reg_confirm_password.get()

    if not (name and email and mobile and password and confirm_password):
        messagebox.showerror("Error", "All fields are required!")
        

    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        

    elif email in students:
        messagebox.showerror("Error", "Email already registered!")
        

    else:
        students[email] = [name, mobile, password]
        messagebox.showinfo("Success", "Registration successful!")
    #clear form
    reg_name.delete(0, END)
    reg_email.delete(0, END)
    reg_mobile.delete(0, END)
    reg_password.delete(0, END)
    reg_confirm_password.delete(0, END)
    show_frame(login_frame)

#student_login function
def login_student():
    email = login_email.get()
    password = login_password.get()

    if not (email and password):
        messagebox.showerror("Error", "All fields are required!")
        
    
    if email not in students:
        messagebox.showerror("Error","Email not found")

    if email not in students or students[email][2] != password:
        messagebox.showerror("Error", "Invalid email or password!")

    messagebox.showinfo("Success", f"Welcome {students[email][0]}! \n Email:{email}")

    #Update dashboard labels with student info
    lbl_name.config(text=f"Name: {students[email][0]}")
    lbl_email.config(text=f"Email: {email}")
    lbl_mobile.config(text=f"Mobile: {students[email][1]}")

    #clear form
    login_email.delete(0, END)
    login_password.delete(0, END)
    show_frame(dashboard_frame)

def logout():
    show_frame(home_frame)

# Home Page
tk.Label(home_frame,text="Home page",font=("Arial",20,"bold"),bg="#2E3442",fg="white").grid(row=0,column=0,pady=20,columnspan=2)
tk.Button(home_frame,text="Register page",command=lambda: show_frame(register_frame),bg="#0EA5E9",fg="white",width=20,height=2).grid(row=1,column=0,pady=10)
tk.Button(home_frame,text="Login page",command=lambda: show_frame(login_frame),bg="#0EA5E9",fg="white",width=20,height=2).grid(row=2,column=0,pady=10)


# Login Page
tk.Label(login_frame,text="Student Login",font=("Arial",20,"bold"),bg="#2E3442",fg="white").grid(row=0,column=0,pady=20,columnspan=2,sticky="nsew")
tk.Label(login_frame,text="Email",font=("Arial",12,"bold")).grid(row=1,column=0,pady=10)
login_email=tk.Entry(login_frame)
login_email.grid(row=1,column=1,pady=10)

tk.Label(login_frame,text="Password",font=("Arial",12,"bold")).grid(row=2,column=0,pady=10)
login_password=tk.Entry(login_frame,show="*")
login_password.grid(row=2,column=1,pady=10)

tk.Button(login_frame,text="Login",command= login_student,bg="#1E3A8A",fg="white").grid(row=3,column=0,pady=10,columnspan=2)
tk.Button(login_frame,text="Back",command=lambda: show_frame(home_frame),bg="#1E3A8A",fg="white").grid(row=4,column=0,pady=10,columnspan=2)

# Register Page
tk.Label(register_frame,text="Student Register",font=("Arial",20,"bold"),bg="#2E3442",fg="white").grid(row=0,column=0,pady=20,columnspan=2,sticky="nsew")
tk.Label(register_frame,text="Name",font=("Arial",12,"bold")).grid(row=1,column=0,pady=10,sticky="w")
reg_name=tk.Entry(register_frame)
reg_name.grid(row=1,column=1,pady=10)

tk.Label(register_frame,text="Email",font=("Arial",12,"bold")).grid(row=2,column=0,pady=10,sticky="w")
reg_email=tk.Entry(register_frame)
reg_email.grid(row=2,column=1,pady=10)

tk.Label(register_frame,text="Mobile Number",font=("Arial",12,"bold")).grid(row=3,column=0,pady=10,sticky="w")
reg_mobile=tk.Entry(register_frame)
reg_mobile.grid(row=3,column=1,pady=10)

tk.Label(register_frame,text="Password",font=("Arial",12,"bold")).grid(row=4,column=0,pady=10,sticky="w")
reg_password=tk.Entry(register_frame,show="*")
reg_password.grid(row=4,column=1,pady=10)

tk.Label(register_frame,text="Confirm Password",font=("Arial",12,"bold")).grid(row=5,column=0,pady=10,sticky="w")
reg_confirm_password=tk.Entry(register_frame,show="*")
reg_confirm_password.grid(row=5,column=1,pady=10)

tk.Button(register_frame,text="Register",command= register_student,bg="#0EA5E9",fg="white").grid(row=6,column=0,pady=10,columnspan=2)
tk.Button(register_frame,text="Back",command=lambda: show_frame(home_frame),bg="#0EA5E9",fg="white").grid(row=7,column=0,pady=10,columnspan=2)

# dashboard 
# Dashboard Page
tk.Label(dashboard_frame, text="Student Dashboard", font=("Arial", 16, "bold"), bg="#2E3442",fg="white").grid(row=0, column=0, pady=20, columnspan=2,sticky="nsew")

lbl_name = tk.Label(dashboard_frame, text="Name: ", font=("Arial", 12))
lbl_name.grid(row=1, column=0, sticky="w", padx=10, pady=5)

lbl_email = tk.Label(dashboard_frame, text="Email: ", font=("Arial", 12))
lbl_email.grid(row=2, column=0, sticky="w", padx=10, pady=5)

lbl_mobile = tk.Label(dashboard_frame, text="Mobile: ", font=("Arial", 12))
lbl_mobile.grid(row=3, column=0, sticky="w", padx=10, pady=5)

tk.Button(dashboard_frame, text="Logout", command=lambda: show_frame(home_frame),bg="#0EA5E9",fg="white").grid(row=4, column=0, pady=20, columnspan=2)


root.mainloop()