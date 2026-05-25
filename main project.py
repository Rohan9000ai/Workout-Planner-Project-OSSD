import tkinter as tk
from tkinter import messagebox
import sqlite3

conn=sqlite3.connect("user.db")
cursor=conn.cursor()

create_table="""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT,
    height integer Not null,
    weight integer Not null
)"""

cursor.execute(create_table)
conn.commit()
conn.close()

def login():
    global email_entry,password_entry,currunt_height,currunt_weight,currunt_name
    e=email_entry.get()
    p=password_entry.get()
    conn=sqlite3.connect("user.db")
    cursor=conn.cursor()

    select="select * from users where email=? and password=?"
    cursor.execute(select,(e,p))
    result=cursor.fetchone()
    conn.commit()
    conn.close()

    if result:
        currunt_name=result[3]
        currunt_height=result[4]
        currunt_weight=result[5]
        messagebox.showinfo("Success","Login successful")
        main_window()
    else:
        messagebox.showerror("Error","Invalid email or password")

    
    

def sign_up():
    global email_entry_input,password_entry_input,h_entry,w_entry,name_entry_k
    if email_entry_input.get()=="" or password_entry_input.get()=="" or h_entry.get()=="" or w_entry.get()==""or name_entry_k.get()=="":
        messagebox.showerror("Error","Please Enter all fields")
        return

    e=email_entry_input.get()
    p=password_entry_input.get()
    h=h_entry.get()
    w=w_entry.get()
    n=name_entry_k.get()
    conn=sqlite3.connect("user.db")
    cursor=conn.cursor()
    insert="insert into users(email,password,height,weight,name) values(?,?,?,?,?)"
    cursor.execute(insert,(e,p,h,w,n))

    conn.commit()
    conn.close()
    messagebox.showinfo("Success","Account created successfully")
    login_window()


def login_window():
    global email_entry,password_entry,name_entry,age_entry
    for widget in root.winfo_children():
        widget.destroy()

    f=tk.Frame(root,width=600,height=600,bg="dark blue")
    f.pack(fill=tk.BOTH)
    img=tk.Label(f,text="Image",font="arial 20 bold",bg="dark blue",fg="white")
    img.pack(pady=40)
    create=tk.Label(f,text="Welcome Back",font="arial 20 bold",bg="dark blue",fg="white")
    create.pack()
    des=tk.Label(f,text="Login to countinue your journey",font="arial 10",bg="dark blue",fg="white")
    des.pack(pady=10)

    root.title("Login Form")
    f1=tk.Frame(root,width=400,height=480,bg="white")
    f1.pack(fill=tk.BOTH,expand=True)
    email=tk.Label(f1,text="Email Address:",font="arial 11 bold",bg="white")
    email.grid(row=0,column=0,pady=5,padx=30)
    email_entry=tk.Entry(f1,font="arial 15",bg="light gray",borderwidth=4,width=30,justify="center")
    email_entry.grid(row=1,column=1,pady=5,padx=30,columnspan=2)
    password=tk.Label(f1,text="Password:",font="arial 11 bold",bg="white")
    password.grid(row=2,column=0,pady=5,padx=30)
    password_entry=tk.Entry(f1,font="arial 15",bg="light gray",borderwidth=4,show="*",width=31,justify="center")
    password_entry.grid(row=3,column=1,pady=5,padx=30)
    age=tk.Label(f1,text="Age:",font="arial 11 bold",bg="white")
    age.grid(row=4,column=0,pady=5,padx=30)
    age_entry=tk.Entry(f1,font="arial 15",bg="light gray",borderwidth=4,width=30,justify="center")
    age_entry.grid(row=5,column=1,pady=5,padx=30)
    tk.Label(f1,text="",bg="white").grid(row=6,column=0,pady=5,padx=30)


    login_btn=tk.Button(f1,font="arial 13",bg="dark blue",fg="white",width=40,pady=6,text="Log in",command=login)
    login_btn.grid(row=7,column=1,pady=12,padx=20,columnspan=2)
    new=tk.Button(f1,font="arial 13",bg="dark blue",fg="white",width=40,pady=6,text="Create Account",command=sign_up_window)
    new.grid(row=8,column=1,pady=12,padx=20,columnspan=2)


def sign_up_window():
    global email_entry_input,password_entry_input,h_entry,w_entry,name_entry_k
    for widget in root.winfo_children():
        widget.destroy()

    f=tk.Frame(root,width=600,height=600,bg="dark blue")
    f.pack(fill=tk.BOTH)
    img=tk.Label(f,text="Image",font="arial 20 bold",bg="dark blue",fg="white")
    img.pack(pady=40)
    create=tk.Label(f,text="Create Account",font="arial 20 bold",bg="dark blue",fg="white")
    create.pack()
    des=tk.Label(f,text="Start your fitness journey today",font="arial 10",bg="dark blue",fg="white")
    des.pack(pady=10)
    f1=tk.Frame(root,width=400,height=480,bg="white")
    f1.pack(fill=tk.BOTH)

    root.title("Sign Up Form")
    name=tk.Label(f1,text="Full Name:",font="arial 11 bold",bg="white")
    name.grid(row=0,column=0,pady=5,padx=10)
    name_entry_k=tk.Entry(f1,font="arial 15",bg="light gray",borderwidth=4,width=30,justify="center")
    name_entry_k.grid(row=1,column=1,pady=5,padx=20)
    email=tk.Label(f1,text="Email Address:",font="arial 11 bold",bg="white")
    email.grid(row=2,column=0,pady=5,padx=20)
    email_entry_input=tk.Entry(f1,font="arial 15",bg="light gray",borderwidth=4,width=30,justify="center")
    email_entry_input.grid(row=3,column=1,pady=5,padx=20)
    password=tk.Label(f1,text="Password:",font="arial 11 bold",bg="white")
    password.grid(row=4,column=0,pady=5,padx=20)
    password_entry_input=tk.Entry(f1,font="arial 15",bg="light gray",borderwidth=4,show="*",width=30,justify="center")
    password_entry_input.grid(row=5,column=1,pady=5,padx=20)

    h=tk.Label(f1,text="height(cm)",font="arial 11",bg="white")
    h.grid(row=6,column=0,pady=15,padx=20)
    h_entry=tk.Entry(f1,font="arial 15",bg="light gray",borderwidth=4,width=25,justify="center")
    h_entry.grid(row=7,column=0,pady=5,padx=20)
    w=tk.Label(f1,text="weight(kg)",font="arial 11",bg="white")
    w.grid(row=6,column=1,pady=15,padx=20)
    w_entry=tk.Entry(f1,font="arial 15",bg="light gray",borderwidth=4,width=25,justify="center")
    w_entry.grid(row=7,column=1,pady=5,padx=20)

    complete=tk.Button(f1,font="arial 13",bg="dark blue",fg="white",width=40,pady=6,text="create account",command=sign_up)
    complete.grid(row=8,pady=10,padx=50,columnspan=2)
    not_account=tk.Button(f1,font="arial 13",bg="dark blue",fg="white",width=40,pady=6,text="Already have an account ,Login!",command=login_window)
    not_account.grid(row=9,pady=10,padx=50,columnspan=2)


def main_window():
    global name_entry,currunt_height,currunt_weight,currunt_name,age_entry
    n=currunt_name
    h=currunt_height
    w=currunt_weight
    ag=age_entry.get()
    for widgets in root.winfo_children():
        widgets.destroy()

    root.title("main window")
    root.maxsize(900, 600)
    f=tk.Frame(root,width=400,height=20,bg="light gray")
    f.pack(fill=tk.BOTH,side=tk.TOP)
    out=tk.Button(f,text="Logout",font="arial 10",bg="light gray",fg="red",width=10,pady=5,command=login_window)
    out.pack(side=tk.RIGHT,padx=5)
    feed=tk.Button(f,text="Feedback",font="arial 10",bg="light gray",fg="black",width=10,pady=5,command=feedback_window)
    feed.pack(side=tk.RIGHT,padx=5)
    f1=tk.Frame(root,width=700,height=300,bg="white",borderwidth=3,relief="groove")
    f1.pack(fill=tk.BOTH)
    tk.Label(f1,text=f"hey {n}",font="arial 20 bold",bg="white",fg="black",width=24,pady=7).pack(pady=10)

    f2=tk.Frame(f1,width=100,height=30,bg="light gray")
    f2.pack(pady=7,side=tk.LEFT,padx=10)
    tk.Label(f2,text="Height:",font="arial 8",bg="light gray",fg="black",width=70,pady=5).grid(row=0,column=0)
    tk.Label(f2,text=f"{h} cm",font="arial 15",bg="light gray",fg="black").grid(row=1,column=0)

    f3=tk.Frame(f1,width=100,height=30,bg="light gray")
    f3.pack(pady=7,side=tk.LEFT,padx=20)
    tk.Label(f3,text="Weight:",font="arial 8",bg="light gray",fg="black",width=70,pady=5).grid(row=0,column=0)
    tk.Label(f3,text=f"{w} kg",font="arial 15",bg="light gray",fg="black").grid(row=1,column=0)
    
    f4=tk.Frame(root,width=100,height=30,bg="white",borderwidth=3,relief="groove")
    f4.pack(fill=tk.BOTH)
    f5=tk.Frame(f4,width=100,height=30,bg="light gray")
    f5.pack(pady=7,padx=10)
    tk.Label(f5,text="Age:",font="arial 8",bg="light gray",fg="black",width=170,pady=5,justify="center").grid(row=0,column=0)
    tk.Label(f5,text=f"{ag}",font="arial 15",bg="light gray",fg="black").grid(row=1,column=0)

    #add scrapped data here

    f6=tk.Frame(root,width=100,height=50,bg="white",borderwidth=3,relief="groove")
    f6.pack(fill=tk.BOTH,side=tk.BOTTOM)
    fat_lose=tk.Button(f6,text="Fat Loss",font="arial 10",bg="light blue",fg="dark blue",width=50,pady=50,command=fat_loss_window)
    fat_lose.pack(pady=10,side=tk.LEFT,padx=30)
    muscle_gain=tk.Button(f6,text="Muscle Gain",font="arial 10",bg="light green",fg="dark green",width=50,pady=50,command=muscle_gain_window)
    muscle_gain.pack(pady=10,side=tk.LEFT,padx=30)


    


def feedback_window():
    pass

def fat_loss_window():
    pass

def muscle_gain_window():
    pass




root=tk.Tk()
root.geometry("700x700")
root.maxsize(700,700)
root.title("Sign Up Form")
sign_up_window()

root.mainloop()   
