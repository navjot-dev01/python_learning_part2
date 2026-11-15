import sqlite3
from tkinter import ttk,messagebox
import tkinter as tk

# data base connection
conn=sqlite3.connect("students.db")            # Connects to (or creates) students.db
c=conn.cursor()                                 # cursor() lets you run SQL commands

# make table
c.execute("""
    CREATE TABLE IF NOT EXISTS students(
          id INTEGER PRIMARYKEY AUTOINCREMENT,
          name TEXT NOT NULL,
          email TEXT NOT NULL,
          mobile TEXT NOT NULL,
          password TEXT NOT NULL
        )
""" )
conn.commit()                              # commit() saves changes.

# function
def add_student():
    add_window=tk.Toplevel(root)
    add_window.title("Add Students")
    add_window.geometry("400x500")
    add_window.resizable(0,0)

# create labels and entries
tk.Label(add_window,text="Name",font=("arial",12,"bold")).pack(pady=10)
name_entry = tk.Entry(add_window,width=30)
name_entry.pack(pady=5)

tk.Label(add_window,text="Email",font=("Arial",15,"bold")).pack(pady=10)
email_entry = tk.Entry(add_window,width=30)
email_entry.pack(pady=5)

tk.Label(add_window,text="Mobile",font=("Arial",15,"bold")).pack(pady=10)
mobile_entry = tk.Entry(add_window,width=30)
mobile_entry.pack(pady=5)

tk.Label(add_window,text="Password",font=("Arial",15,"bold")).pack(pady=10)
password_entry = tk.Entry(add_window,width=30,show="*")
password_entry.pack(pady=5)

def confirm_add():
        insert_student(name_entry, email_entry, mobile_entry, password_entry)
        add_window.destroy()

tk.Button(add_window,text="Add",width=10,height=2,command=confirm_add).pack(pady=10)
tk.Button(add_window,text="Cancel",width=10,height=2,command=add_window.destroy).pack(pady=10)

def insert_student(name_entry, email_entry, mobile_entry, password_entry):
    name = name_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()
    password = password_entry.get()

# Check if any field is empty
    if not name or not email or not mobile or not password:
        messagebox.showerror("Error","All fields are required")
        return

    # Insert the data into the table
    c.execute("INSERT INTO students (name,email,mobile,password) VALUES (?,?,?,?)",(name,email,mobile,password))
    conn.commit()

    # Clear the entries
    name_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    mobile_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)

    # Refresh the table
    refresh_table()    

# update data of student
def update_student():
     selected_item=table.selection()
     if not selected_item: 
          messagebox.showerror("Error","Please select a student to update")   
          return
     
name = table.item(selected_item[0])["values"][0]
email = table.item(selected_item[0])["values"][1]
mobile = table.item(selected_item[0])["values"][2]
password = table.item(selected_item[0])["values"][3]

update_window = tk.Toplevel(root)
update_window.title("Update Student")
update_window.geometry("400x500")
update_window.resizable(0,0)

tk.Label(update_window,text="Name",font=("Arial",15,"bold")).pack(pady=10)
name_entry = tk.Entry(update_window,width=30)
name_entry.insert(0,name)
name_entry.pack(pady=5)

tk.Label(update_window,text="Email",font=("Arial",15,"bold")).pack(pady=10)
email_entry = tk.Entry(update_window,width=30)
email_entry.insert(0,email)
email_entry.pack(pady=5)

tk.Label(update_window,text="Mobile",font=("Arial",15,"bold")).pack(pady=10)
mobile_entry = tk.Entry(update_window,width=30)
mobile_entry.insert(0,mobile)
mobile_entry.pack(pady=5)

tk.Label(update_window,text="Password",font=("Arial",15,"bold")).pack(pady=10)
password_entry = tk.Entry(update_window,width=30,show="*")
password_entry.insert(0,password)
password_entry.pack(pady=5)

def confirm_update():
        update_student_in_db(selected_item[0], name_entry, email_entry, mobile_entry, password_entry)
        update_window.destroy()

tk.Button(update_window,text="Update",width=10,height=2,command=confirm_update).pack(pady=10)
tk.Button(update_window,text="Cancel",width=10,height=2,command=update_window.destroy).pack(pady=10)
def update_student_in_db(selected_item, name_entry, email_entry, mobile_entry, password_entry):
    # Get the data from the entries
    name = name_entry.get()
    email = email_entry.get()
    mobile = mobile_entry.get()
    password = password_entry.get()

    # Check if any field is empty
    if not name or not email or not mobile or not password:
        messagebox.showerror("Error","All fields are required")
        return

    # Update the data in the table
    c.execute("UPDATE students SET name=?,email=?,mobile=?,password=? WHERE id=?",(name,email,mobile,password,int(selected_item)))
    conn.commit()

    # Refresh the table
    refresh_table()

#clear table
for item in table.get_children():
    table.delete(item)

def delete_student():
    selected_item = table.selection()
    if not selected_item:
        messagebox.showerror("Error","Please select a student to delete")
        return

    c.execute("DELETE FROM students WHERE id=?",(int(selected_item[0]),))
    conn.commit()
    refresh_table()    

def refresh_table():
    clear_table()
    c.execute("SELECT * FROM students")
    for row in c.fetchall():
        table.insert("", "end", iid=row[0], values=row[1:])


# ---------------- Main Window ---------------- #

root = tk.Tk()
root.title("Student Management System")
root.geometry("800x600")
root.resizable(0,0)

tk.Label(root,text="Student Details",font=("Arial",20,"bold")).pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=20)

table = ttk.Treeview(frame,columns=("Name","Email","Mobile","Password"),show="headings")

table.heading("Name",text="Name")
table.heading("Email",text="Email")
table.heading("Mobile",text="Mobile")
table.heading("Password",text="Password")

table.column("Name",width=100)
table.column("Email",width=100)
table.column("Mobile",width=100)
table.column("Password",width=100)

table.pack(side="left",fill="both",expand=True)

scrollbar = ttk.Scrollbar(frame,orient="vertical",command=table.yview)
scrollbar.pack(side="right",fill="y")
table.configure(yscrollcommand=scrollbar.set)

tk.Button(root,text="Add",width=10,height=2,command=add_student).pack(pady=10)
tk.Button(root,text="Update",width=10,height=2,command=update_student).pack(pady=10)
tk.Button(root,text="Delete",width=10,height=2,command=delete_student).pack(pady=10)
tk.Button(root,text="Clear",width=10,height=2,command=clear_table).pack(pady=10)
tk.Button(root,text="Exit",width=10,height=2,command=root.destroy).pack(pady=10)

refresh_table()
root.mainloop()        


