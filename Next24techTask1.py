#importing tkinter library as tk
import tkinter as tk
#import messagebox 
from tkinter import messagebox
#creating parent(ie.root)
root=tk.Tk()
root.geometry('500x450')
root.title("Registration Form")
root.configure(bg="#333333")

#creating a container to store all the widgets
frame=tk.Frame(bg="#333333")




#Creating entries
e1=tk.Entry(frame)
e2=tk.Entry(frame)
e3=tk.Entry(frame,show="*")
e4=tk.Entry(frame)
e5=tk.Entry(frame)

#Function is being created to provide functionality to the buttons ~register now and clear.
def display():
    messagebox.showinfo("Pass","Registered Successfully!")
    clear_screen()
def clear_screen():
    for widget in root.winfo_children():
        root.destroy()

#creating labels,setting colour,bg and font style and positioning it in the correct position using grid
tk.Label(frame,text="Registration  Form",bg="#333333",fg= "deeppink",font=("Poppins",16,"bold")).grid(row=0,column=7,pady=50,sticky='news')
tk.Label(frame,text="Name :",bg="#333333",font=("Poppins",9),fg="white").grid(row=3,column=5,pady=3)
tk.Label(frame,text=" Email ID: ",bg="#333333",font=("Poppins",9),fg="white").grid(row=4,column=5,pady=3)
tk.Label(frame,text=" Password :   ",bg="#333333",font=("Poppins",9),fg="white").grid(row=4,column=7,padx=0,pady=0,sticky='e')
tk.Label(frame,text="Age :",bg="#333333",font=("Poppins",9),fg="white").grid(row=5,column=5,pady=3)
tk.Label(frame,text="Phn.No :",bg="#333333",font=("Poppins",9),fg="white").grid(row=6,column=5,pady=3)

#positioning the entries(empty boxes) using grid
e1.grid(row=3,column=6,padx=0,pady=0)
e2.grid(row=4,column=6,padx=0,pady=0)
e3.grid(row=4,column=8,padx=0,pady=0)
e4.grid(row=5,column=6)
e5.grid(row=6,column=6)

gnd=tk.Label(frame,text="Gender :",bg="#333333",font=("Poppins",9),fg="white").grid(row=7,column=5)

#creating RadioButton for gender and positioning it in the correct position using grid
v=tk.IntVar()
tk.Radiobutton(frame,text="Male",bg="#333333",fg="skyblue",font=("Poppins",10),variable=v,value=1).grid(row=7,column=6)
tk.Radiobutton(frame,text="Female",bg="#333333",fg="lightpink",font=("Poppins",10),variable=v,value=2).grid(row=7,column=7)

#creating a Button and positioning it in the correct position using grid
btn=tk.Button(frame,text=" Register Now ",bg="deeppink",fg="white",font=("Poppins",9),command=display).grid(row=10,column=7,pady=42,padx=8)

#widgets stored in a container named frame occupies the center position when the page is maximised
frame.pack()

root.mainloop()

