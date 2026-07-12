from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("600x400")
root.title("Student Management System")

# Create a frame inside root
home_frame=Frame(root,bg="lightblue")
about_frame=Frame(root,bg="lightpink")

for frame in (home_frame,about_frame):
    frame.place(relheight=1,relwidth=1)
    
    def show_home():
        home_frame.tkraise()

    def show_about():
        about_frame.tkraise()


#Add widgets inside the home frame
tk=Label(home_frame,text="home page",font=("Arial",20,"bold"),fg="blue").pack(pady=20)
tk=Button(home_frame,text="Go to About page",command=lambda: show_about()).pack(pady=10)

#Add widgets inside the about frame
tk=Label(about_frame,text="About page",font=("Arial",20,"bold"),fg="blue").pack(pady=20)
tk=Button(about_frame,text="Go to Home page",command=lambda: show_home()).pack(pady=10)

show_home()

root.mainloop()