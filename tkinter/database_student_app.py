print("="*15 + "Student Management System - Dashboard" + "="*15)


from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3 # pip install sqlite3


# Database connection
conn=sqlite3.connect('students.db')
c=conn.cursor()

# create table

c.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        mobile TEXT NOT NULL,
        password TEXT NOT NULL
    )
""")

conn.commit()

#--------------------------------TKINTER ROOT---------------------------
root=Tk()
root.geometry("600x400")
root.title("Student Management System")

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
    #     register_content.tkraise()    
    
    # def show_login():
    #     login_frame.tkraise()

    # def show_dashboard():
    #     dashboard_frame.tkraise()
# show_home()    

                                          #OR
def show_frame(frame):
    frame.tkraise()                                      

# ------------------------Student Registration Function--------------------
def register_student():
    name = reg_name.get()
    email = reg_email.get()
    mobile = reg_mobile.get()
    password = reg_password.get()
    confirm_password = reg_confirm_password.get()

    if not (name and email and mobile and password and confirm_password):
        messagebox.showerror("Error", "All fields are required!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return
    try:
        
        c.execute(""" INSERT INTO students(
                  name,email,mobile,password) VALUES(?,?,?,?)""",
                  (name,email,mobile,password))
        conn.commit()
    except sqlite3.IntegrityError:
        return "Username already exists"
    


    messagebox.showinfo("Success", "Registration successful!")
    #clear form
    reg_name.delete(0, END)
    reg_email.delete(0, END)
    reg_mobile.delete(0, END)
    reg_password.delete(0, END)
    reg_confirm_password.delete(0, END)
    show_frame(login_frame)

    
#---------------------------student_login function-----------------------
def login_student():
    email = login_email.get()
    password = login_password.get()

    if not (email and password):
        messagebox.showerror("Error", "All fields are required!")
        return
    
    c.execute("""SELECT name,email,mobile FROM students WHERE email=? AND password=?""",(email,password))
    student=c.fetchone()
    if student:
        lbl_name.config(text="Name:"+ student[0])
        lbl_email.config(text="Email:"+student[1])
        lbl_mobile.config(text="Mobile:"+student[2])
        #clear form
        login_email.delete(0, END)
        login_password.delete(0, END)
        show_frame(dashboard_frame)
    else:
        messagebox.showerror("Error","Invalid Email or password")

# --------------------------------Logout Function------------------------------------------
def logout():
    show_frame(home_frame)


# -----------------------------------------Home Page------------------------------------------

    
# HOME- Center Frame
home_content = Frame(home_frame, bg="white", bd=2, relief="ridge")
home_content.place(relx=0.5, rely=0.5, anchor="center")

# home content Heading
Label(
    home_content,
    text="Student Management System",
    font=("Segoe UI", 24, "bold"),
    fg="#1E3A8A",
    bg="white"
).grid(row=0, column=0, pady=(20, 30), padx=50)

# home content- Register Button
Button(home_content,text="Register",font=("Segoe UI", 14, "bold"),bg="#0EA5E9",fg="white",width=20,height=2,
       cursor="hand2",command=lambda: show_frame(register_frame)).grid(row=1, column=0, pady=10)

# home content- Login Button
Button(
    home_content,
    text="Login",
    font=("Segoe UI", 14, "bold"),
    bg="#2563EB",
    fg="white",
    width=20,
    height=2,
    cursor="hand2",
    command=lambda: show_frame(login_frame)).grid(row=2, column=0, pady=10)

# home content-Exit Button
Button(
    home_content,
    text="Exit",
    font=("Segoe UI", 14, "bold"),
    bg="#EF4444",
    fg="white",
    width=20,
    height=2,
    cursor="hand2",
    command=root.destroy
).grid(row=3, column=0, pady=(10, 20))



#---------------------------------------- LOGIN PAGE -------------------------------------

login_content = Frame(
    login_frame,
    bg="white",
    bd=2,
    relief="ridge",
    padx=35,
    pady=25
)
login_content.place(relx=0.5, rely=0.5, anchor="center")

# Heading
tk.Label(
    login_content,
    text="Student Login",
    font=("Segoe UI", 22, "bold"),
    bg="white",
    fg="#1E3A8A"
).grid(row=0, column=0, columnspan=2, pady=(0, 30))

label_font = ("Segoe UI", 12, "bold")
entry_font = ("Segoe UI", 11)

# Email
tk.Label(
    login_content,
    text="Email",
    font=label_font,
    bg="white",
    fg="#374151"
).grid(row=1, column=0, padx=(0, 30), pady=10, sticky="w")

login_email = tk.Entry(login_content, font=entry_font, width=28)
login_email.grid(row=1, column=1, padx=10, pady=10)

# Password
tk.Label(
    login_content,
    text="Password",
    font=label_font,
    bg="white",
    fg="#374151"
).grid(row=2, column=0, padx=(0, 30), pady=10, sticky="w")

login_password = tk.Entry(
    login_content,
    font=entry_font,
    show="*",
    width=28
)
login_password.grid(row=2, column=1, padx=10, pady=10)

# Login Button
tk.Button(
    login_content,
    text="Login",
    font=("Segoe UI", 12, "bold"),
    bg="#2563EB",
    fg="white",
    width=18,
    command=login_student
).grid(row=3, column=0, columnspan=2, pady=(20, 10))

# Back Button
tk.Button(
    login_content,
    text="Back",
    font=("Segoe UI", 12, "bold"),
    bg="#64748B",
    fg="white",
    width=18,
    command=lambda: show_frame(home_frame)
).grid(row=4, column=0, columnspan=2, pady=10)



#---------------------------------------------- Register Page----------------------------------------------


register_content=Frame(
    register_frame,
    bg="White",
    bd=2,
    relief="ridge",
    padx=35,
    pady=25 
)
register_content.place(relx=0.5,rely=0.5,anchor="center")

# register content - Heading
tk.Label(
    register_content,
    text="Student Registration",
    font=("Segoe UI", 22, "bold"),
    bg="white",
    fg="#1E3A8A"
).grid(row=0, column=0, columnspan=2, pady=(0,25))

label_font = ("Segoe UI", 12, "bold")
entry_font = ("Segoe UI", 11)

tk.Label(register_content, text="Name", font=label_font,bg="white", fg="#374151",width=18).grid(row=1, column=0, padx=(0,90), pady=10, sticky="e")
reg_name = tk.Entry(register_content, font=entry_font, width=28)
reg_name.grid(row=1, column=1, padx=10, pady=10,sticky="w")


tk.Label(register_content,text="Email",font=label_font,bg="white", fg="#374151",width=18).grid(row=2,column=0,pady=10,padx=(0,90),sticky="e")
reg_email=tk.Entry(register_content,font=entry_font,width=28)
reg_email.grid(row=2,column=1,pady=10,padx=10,sticky="w")

tk.Label(register_content,text="Mobile Number",font=label_font,bg="white", fg="#374151",width=18).grid(row=3,column=0,pady=10,padx=(0,50),sticky="e")
reg_mobile=tk.Entry(register_content,font=entry_font,width=28)
reg_mobile.grid(row=3,column=1,pady=10,padx=10,sticky="w")

tk.Label(register_content,text="Password",font=label_font,bg="white", fg="#374151",width=18).grid(row=4,column=0,pady=10,padx=(0,75),sticky="e")
reg_password=tk.Entry(register_content,font=entry_font,show="*",width=28)
reg_password.grid(row=4,column=1,pady=10,padx=10,sticky="w")

tk.Label(register_content,text="Confirm Password",font=label_font,bg="white", fg="#374151",width=18).grid(row=5,column=0,pady=10,padx=(0,40),sticky="e")
reg_confirm_password=tk.Entry(register_content,font=entry_font,show="*",width=28)
reg_confirm_password.grid(row=5,column=1,pady=10,padx=10,sticky="w")

# Register Button
tk.Button(
    register_content,
    text="Register",
    font=("Segoe UI", 12, "bold"),
    bg="#2563EB",
    fg="white",
    width=18,
    command=register_student
).grid(row=6, column=0, columnspan=2, pady=(20,10))     # pady=(top,bottom)

# Back Button
tk.Button(
    register_content,
    text="Back",
    font=("Segoe UI", 12, "bold"),
    bg="#64748B",
    fg="white",
    width=18,
    command=lambda: show_frame(home_frame)
).grid(row=7, column=0, columnspan=2, pady=10)


# ------------------------------------------------- Dashboard Page----------------------------------------------
dashboard_content=Frame(
    dashboard_frame,
    bg="White",
    bd=2,
    relief="ridge",
    padx=40,
    pady=30
)
dashboard_content.place(relx=0.5,rely=0.5,anchor="center")

tk.Label(
    dashboard_content,
    text="Student Dashboard",
    font=("Segoe UI", 22, "bold"),
    bg="white",
    fg="#1E3A8A"
).grid(row=0, column=0, columnspan=2, pady=(0,20))

lbl_name = tk.Label(dashboard_content, text="Name: ", font=("Segoe UI", 12))
lbl_name.grid(row=1, column=0, sticky="w", padx=10, pady=5)

lbl_email = tk.Label(dashboard_content, text="Email: ", font=("Segoe UI", 12))
lbl_email.grid(row=2, column=0, sticky="w", padx=10, pady=5)

lbl_mobile = tk.Label(dashboard_content, text="Mobile: ", font=("Segoe UI", 12))
lbl_mobile.grid(row=3, column=0, sticky="w", padx=10, pady=5)

tk.Button(dashboard_content, text="Logout", command=lambda: show_frame(home_frame),bg="#0EA5E9",fg="white").grid(row=4, column=0, pady=20, columnspan=2)

show_frame(home_frame)
root.mainloop()
conn.close()