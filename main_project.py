import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
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

root=tk.Tk()
root.geometry("700x700")
root.maxsize(700,700)
root.title("Sign Up Form")

def login():
    global email_entry,password_entry,currunt_height,currunt_weight,currunt_name,currunt_age,age_entry
    e=email_entry.get()
    p=password_entry.get()
    currunt_age=age_entry.get()
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
    opened_img = Image.open("dumbell.png")
    resized=opened_img.resize((120,90))
    photo = ImageTk.PhotoImage(resized)
    img=tk.Label(f,image=photo,font="arial 20 bold",bg="dark blue",fg="white")
    img.image = photo
    img.pack(pady=10)
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
    opened_img = Image.open("dumbell.png")
    resized=opened_img.resize((120,90))
    photo = ImageTk.PhotoImage(resized)
    img=tk.Label(f,image=photo,font="arial 20 bold",bg="dark blue",fg="white")
    img.image = photo
    img.pack(pady=7)
    create=tk.Label(f,text="Create Account",font="arial 20 bold",bg="dark blue",fg="white")
    create.pack()
    des=tk.Label(f,text="Start your fitness journey today",font="arial 10",bg="dark blue",fg="white")
    des.pack(pady=7)
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
    global name_entry,currunt_height,currunt_weight,currunt_name,age_entry,currunt_age
    n=currunt_name
    h=currunt_height
    w=currunt_weight
    ag=currunt_age
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
    tk.Label(f,text="Fitness App",font="arial 15 bold",bg="light gray",fg="black").pack(side=tk.LEFT,padx=10)
    f1=tk.Frame(root,width=700,height=300,bg="white")
    f1.pack(fill=tk.BOTH)
    tk.Label(f1,text=f"hey {n}",font="arial 20 bold",bg="white",fg="black",width=10,pady=7).pack(pady=10,side=tk.TOP)

    f2=tk.Frame(f1,width=100,height=30,bg="gray95")
    f2.pack(pady=7,side=tk.LEFT,padx=10)
    tk.Label(f2,text="Height:",font="arial 8",bg="gray95",fg="black",width=70,pady=5).grid(row=0,column=0)
    tk.Label(f2,text=f"{h} cm",font="arial 15",bg="gray95",fg="black").grid(row=1,column=0)

    f3=tk.Frame(f1,width=100,height=30,bg="gray95")
    f3.pack(pady=7,side=tk.LEFT,padx=18)
    tk.Label(f3,text="Weight:",font="arial 8",bg="gray95",fg="black",width=70,pady=5).grid(row=0,column=0)
    tk.Label(f3,text=f"{w} kg",font="arial 15",bg="gray95",fg="black").grid(row=1,column=0)

    f4=tk.Frame(root,width=100,height=30,bg="white")
    f4.pack(fill=tk.BOTH)
    f5=tk.Frame(f4,width=100,height=30,bg="gray95")
    f5.pack(pady=7,padx=10)
    tk.Label(f5,text="Age:",font="arial 8",bg="gray95",fg="black",width=170,pady=5).grid(row=0,column=0)
    tk.Label(f5,text=f"{ag} yrs",font="arial 15",bg="gray95",fg="black").grid(row=1,column=0)

    #add scrapped data here

    f6=tk.Frame(root,width=100,height=50,bg="white")
    f6.pack(fill=tk.BOTH,side=tk.BOTTOM)
    fat_lose=tk.Button(f6,text="Fat Loss\n Cardio & burn exersices",font="arial 13",bg="lightblue1",fg="blue4",width=40,pady=50,padx=10,command=fat_loss_window,anchor="w",justify="left")
    fat_lose.pack(pady=10,side=tk.LEFT,padx=30)
    muscle_gain=tk.Button(f6,text="Muscle Gain\n Strength & resistance exercises",font="arial 13",bg="aquamarine1",fg="dark green",width=50,pady=50,padx=10,command=muscle_gain_window,anchor="w",justify="left")
    muscle_gain.pack(pady=10,side=tk.LEFT,padx=30)


def feedback_window():
    for widgets in root.winfo_children():
         widgets.destroy()
    root.title("Give your Feedback")
    root.maxsize(900,600)
    f1 = tk.Frame(root, width=600, height=400, bg="white")
    f1.pack(fill=tk.BOTH, expand=True)
    header = tk.Frame(f1, bg="#1a1a6e", width=600)
    header.pack(fill=tk.X)
    label1 = tk.Label(header, text=" Feedback", font=("Arial", 16, "bold"), bg="#1a1a6e", fg="white")
    label1.pack(pady=18)
    sub = tk.Label(header, text="give your nobal thoughts!", font=("Arial", 9), bg="#1a1a6e", fg="#a0a8d0")
    sub.pack(pady=(0, 15))
    inner = tk.Frame(f1, bg="white")
    inner.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    tk.Label(inner, text="Category", font=("Arial", 9, "bold"), bg="white", fg="#555").grid(row=0, column=0, sticky="w", pady=(5,2))
    dropdown = tk.StringVar(value="General Feedback")
    menu = tk.OptionMenu(inner, dropdown, "General Feedback", "Bug Report", "Feature Request", "Other")
    menu.config(font=("Arial", 10), bg="white", width=30)
    menu.grid(row=1, column=0, sticky="w", pady=(0, 8))
    tk.Label(inner, text="Rating", font=("Arial", 9, "bold"), bg="white", fg="#555").grid(row=2, column=0, sticky="w", pady=(5,2))
    rating_frame = tk.Frame(inner, bg="white")
    rating_frame.grid(row=3, column=0, sticky="w")
    selected_rating = tk.IntVar(value=0)
    for i in range(1, 6):
        rb = tk.Radiobutton(rating_frame, text=str(i), variable=selected_rating, value=i,
                            font=("Arial", 10), bg="white", fg="#1a1a6e", selectcolor="#e8e8ff")
        rb.pack(side=tk.LEFT, padx=5)

    # Message
    tk.Label(inner, text="Message", font=("Arial", 9, "bold"), bg="white", fg="#555").grid(row=4, column=0, stick ="w", pady=(8,2))

    msg_entry = tk.Text(inner, font=("Arial", 10), width=42, height=4, bd=2, relief="solid")
    msg_entry.insert("1.0", "Write your feedback here...")
    msg_entry.config(fg="gray")
    msg_entry.grid(row=5, column=0, pady=(0, 15))
    def on_click(event):
        if msg_entry.get("1.0","end-1c") == "Write your feedback here...":
            msg_entry.delete("1.0","end-1c")
            msg_entry.config(fg="black")

    def foucus_on(event):
        if msg_entry.get("1.0","end-1c") == "":
            msg_entry.insert("wirte your feedback here...")
            msg_entry.config(fg="grey")
    msg_entry.bind("<FocusIn>", on_click)
    msg_entry.bind("<FocusOut>", foucus_on)

    def submitt():
        tk.messagebox.showinfo("submit", "submit successfuly")
        
    submit = tk.Button(inner, text=" Submit Feedback", font=("Arial", 11, "bold"),
                    bg="#1a1a6e", fg="white",command=submitt ,width=40, pady=7, cursor="hand2" , justify="center")
   

    submit.grid(row=6, column=0, pady=20,padx=20)


def fat_loss_window():
    for widgets in root.winfo_children():
        widgets.destroy()
    root.title("Fat loss window")
    root.maxsize(900, 600)
    frame1 = tk.Frame(root,width=400, height=400 , bg="white" , bd=1)
    frame1.pack(fill=tk.BOTH, expand=True)

    label1 = tk.Label(frame1, text="Fat Loss-gym_workout_planner", font=("Arial",14,"bold") , width=400)
    label1.pack(pady=5,padx=5)
    label2= tk.Label(frame1,text="Today's session:", font=("Arial",11,"bold"), bg="white")
    label2.pack(pady=(10,4),padx=20, anchor="w")

    par_label=tk.Frame(frame1,width=400,bg="white")
    par_label.pack(fill=tk.X, padx=10,pady=10)
    for i in range(3):
        par_label.columnconfigure(i,weight=1)

    item =[
        ("calories", "310kcal"),
        ("Duration","22min"),
        ("Exersice","4done")
    ]    
    for col,(title,value) in enumerate(item):
        sub_frame=tk.Frame(par_label,bg="#e0e0e0",relief=tk.RIDGE,bd=1)
        sub_frame.grid(pady=5,padx=5,row=0,column=col,sticky="nsew")

        tk.Label(sub_frame,text=title,bg="#e0e0e0",font=("Arial",11,"bold")).pack(pady=(5,0))
        tk.Label(sub_frame,text=value,bg="#e0e0e0",font=("Arial",11,"bold")).pack(pady=(0,5))
                                                                                
    label3=tk.Label(frame1,text="Exerscises and counters:" , font=("Arial",11,"bold"), bg="white").pack(
        pady=5,padx=20, anchor="w")



    canvas = tk.Canvas(frame1,bg="white", highlightthickness=0)
    scrollbar = tk.Scrollbar(frame1, orient="vertical" , command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right",fill="y")
    canvas.pack(side="left", fill="both",expand=True , pady=0, padx=0)

    scroll_frame = tk.Frame(canvas,bg="white")
    window = canvas.create_window((0,0),window=scroll_frame,anchor="nw")

    def on_canvas_resize(event):
        canvas.itemconfig(window,width=event.width)
    canvas.bind("<Configure>", on_canvas_resize)

    def on_frame_resize(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    scroll_frame.bind("<Configure>", on_frame_resize)

    def rotate(event):
        canvas.yview_scroll(int(-1* (event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>",rotate) 
        


    Exercises = [
        {"name": "Crunchers",      "type":"Reps",  "val": 24,   "timer":  False},
        {"name": "Jumping jacks",   "type": "Reps",  "val": 40,   "timer": False},
        {"name":  "Burpees",        "type":"Reps",   "val":15,    "timer": False},
        {"name":  "High knees",      "type":"Reps",   "val":30,    "timer": False},
        {"name":   "Plank",          "type": "Reps",   "val":90,   "timer": True},
        {"name":   "Mountain Climbers", "type":"Reps",  "val":20,   "timer":False},
    ]
    total ={}

    for ex in Exercises:
        row = tk.Frame(scroll_frame, bg="#ebe7de")
        row.pack(fill="x", pady=3,padx=14)

        sub_row=tk.Frame(row,bg="#ebe7de")
        sub_row.pack(pady=10,padx=13,side="left")

        tk.Label(sub_row, text=ex["name"], font=("Arial", 11,"bold"),bg="#ebe7de").pack(anchor="w")
        tk.Label(sub_row,text=ex["type"],font=("Arial",11,"bold"),bg="#ebe7de").pack(anchor="w")

        if ex["timer"]:
            frame4 = tk.Frame(row,bg="#e0e0e0")
            frame4.pack(side="right",pady=12,padx=15)

            btn = tk.Button(frame4, text="start", font = ("Arial", 9, "bold"), bg="green", fg="white")
            btn.pack(pady=4, padx=6, side= "left")

            btn1 = tk.Button(frame4, text="stop", font=("Arial", 9 ,"bold"), bg="blue", fg="white")
            btn1.pack(padx=6, pady=4, side="right")
        else:
            var = tk.IntVar(value=ex["val"])
            total[ex["name"]]=var
            frame5 = tk.Frame(row,bg="blue")
            frame5.pack(pady=10,padx=15 , side="right")

            btn2 = tk.Button(frame5,text="-", font=("Arial", 14,"bold"),bg="green",fg="white" , cursor="hand2"
                                ,command=lambda x=var: x.set(max(0,x.get()-1)))
            btn2.pack(side="left")

            tk.Label(frame5,textvariable=var,bg="#e0e0e0",fg="black", anchor="center",
                        font=("Arial", 14,"bold")).pack(side="left")
            btn3= tk.Button(frame5,text="+", font=("Arial",14,"bold"),bg="green",fg="white",
                            command=lambda x=var: x.set(x.get()+1))
            btn3.pack(pady=4,padx=4,side="right")
        def submit():
            tk.messagebox.showinfo( "submit","okay submitted")

    button= tk.Button(scroll_frame, text="submit", font=("Arial", 11, "bold"),command=submit ,relief="flat",width=20,  bg="green", fg="white")
    button.pack(pady=15) 


        
        

def muscle_gain_window():
    for widgets in root.winfo_children():
        widgets.destroy()
    root.title("select muscle window")
    root.maxsize(900, 600)
    f=tk.Frame(root,width=400,height=40,bg="white",pady=20)
    f.pack(fill=tk.BOTH,side=tk.TOP)
    back_btn=tk.Button(f,text="<-- back to main menu",font="arial 10 bold",bg="dark blue",fg="white",command=main_window,pady=10)
    back_btn.pack(side=tk.LEFT,padx=10)
    tk.Label(f,bg="white",text="                                                  ").pack(side=tk.LEFT,padx=20)
    tk.Label(f,text="Strength Training",font="arial 15",bg="white",fg="black").pack(side=tk.LEFT,padx=10)
    f1=tk.Frame(root,width=700,height=300,bg="white")
    f1.pack(fill=tk.BOTH,expand=True)
    title_frame=tk.Frame(f1,width=100,height=100,bg="lightblue1",borderwidth=2,pady=40)
    title_frame.pack(side=tk.TOP,fill=tk.BOTH)
    img_data = Image.open("dumbell.png")
    resized = img_data.resize((80, 80))
    photo = ImageTk.PhotoImage(resized)
    img_label = tk.Label(title_frame, image=photo, bg="lightblue1")
    img_label.image = photo
    img_label.pack(side=tk.LEFT, padx=20, pady=7)
    text_label = tk.Label(title_frame,text="Choose your muscle group\nSelect a muscle - we'll show you the best exercises for it!",font="arial 13",bg="lightblue1",fg="blue4",justify="left")
    text_label.pack(side=tk.LEFT, pady=5, padx=10, anchor="w")
    main_frame=tk.Frame(f1,width=700,height=500,bg="white")
    main_frame.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=20,pady=10)
    tk.Label(main_frame,text="Select Muscle Group",font="arial 11 bold",bg="white",fg="black").grid(row=0,column=0,pady=10,padx=20,sticky="w")

    chest_btn=tk.Button(main_frame,text="chest",font="arial 10",bg="light gray",fg="black",width=30,pady=40,command=chest_window)
    chest_btn.grid(row=1,column=0,pady=15,padx=22)

    chest_btn=tk.Button(main_frame,text="Abs",font="arial 10",bg="light gray",fg="black",width=30,pady=40,command=abs_window)
    chest_btn.grid(row=1,column=1,pady=15,padx=22)

    chest_btn=tk.Button(main_frame,text="Back",font="arial 10",bg="light gray",fg="black",width=30,pady=40,command=back_window)
    chest_btn.grid(row=1,column=2,pady=15,padx=22)

    chest_btn=tk.Button(main_frame,text="Arms",font="arial 10",bg="light gray",fg="black",width=30,pady=40,command=arms_window)
    chest_btn.grid(row=2,column=0,pady=15,padx=22)

    chest_btn=tk.Button(main_frame,text="Shoulder",font="arial 10",bg="light gray",fg="black",width=30,pady=40,command=shoulder_window)
    chest_btn.grid(row=2,column=1,pady=15,padx=22)

    chest_btn=tk.Button(main_frame,text="Legs",font="arial 10",bg="light gray",fg="black",width=30,pady=40,command=legs_window)
    chest_btn.grid(row=2,column=2,pady=15,padx=22)




def chest_window():
    for widgets in root.winfo_children():
        widgets.destroy()
    root.title("Chest muscle")
    root.maxsize(900, 600)
    f=tk.Frame(root,width=400,bg="white")
    f.pack(fill=tk.BOTH,side=tk.TOP)
    back_btn=tk.Button(f,text="<-- back to Select Muscles",font="arial 10 bold",bg="dark blue",fg="white",command=muscle_gain_window,pady=8)
    back_btn.pack(side=tk.LEFT,padx=10)
    tk.Label(f,bg="white",text="                                           ").pack(side=tk.LEFT,padx=20)
    tk.Label(f,text="Best Chest Exercises",font="arial 15",bg="white",fg="black").pack(side=tk.LEFT,padx=20)
    main_frame=tk.Frame(root,width=700,height=500,bg="white")
    main_frame.pack(fill=tk.BOTH,expand=True)

    f1=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f1.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data1=Image.open("completechest.png")
    resized1=image_data1.resize((70,70))
    photo1=ImageTk.PhotoImage(resized1)
    img_label1=tk.Label(f1,image=photo1,bg="light gray")
    img_label1.image=photo1
    img_label1.pack(side=tk.LEFT,padx=10)

    text=tk.Label(f1,text="Chest Dips\n\n3 sets- 10-15 reps .bodyweight\n targets complete chest but mainly trains upper chest and also trains the triceps muscles little bit",font="arial 11",bg="light gray",fg="black",justify="left")
    text.pack(side=tk.LEFT,padx=10)

    f2=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f2.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data2=Image.open("lowerchest.png")
    resized2=image_data2.resize((70,70))
    photo2=ImageTk.PhotoImage(resized2)
    img_label2=tk.Label(f2,image=photo2,bg="light gray")
    img_label2.image=photo2
    img_label2.pack(side=tk.LEFT,padx=10)

    text2=tk.Label(f2,text="Decline Dumbell Press\n\n3 sets- 10-12 reps Heavy weight\n Mainly targets lower chest and specially helps to gives the round shape to chest",font="arial 11",bg="light gray",fg="black",justify="left")
    text2.pack(side=tk.LEFT,padx=10)

    f3=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f3.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data3=Image.open("upperchest.png")
    resized3=image_data3.resize((70,70))
    photo3=ImageTk.PhotoImage(resized3)
    img_label3=tk.Label(f3,image=photo3,bg="light gray")
    img_label3.image=photo3
    img_label3.pack(side=tk.LEFT,padx=10)

    text3=tk.Label(f3,text="Incline Dumbell Press\n\n3 sets- 10-12 reps Heavy weight\n Mainly targets upper chest but also trains triceps muscle ",font="arial 11",bg="light gray",fg="black",justify="left")
    text3.pack(side=tk.LEFT,padx=10)

    f4=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f4.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data4=Image.open("midline_chest.png")
    resized4=image_data4.resize((70,70))
    photo4=ImageTk.PhotoImage(resized4)
    img_label4=tk.Label(f4,image=photo4,bg="light grey")
    img_label4.image=photo4
    img_label4.pack(side=tk.LEFT,padx=10)

    text4=tk.Label(f4,text="cable cross over\n\n3 sets- 10-12 reps Moderate weight\n targets inner chest give a 3D shape best if you have a chest muscle gap ",font="arial 11",bg="light gray",fg="black",justify="left")
    text4.pack(side=tk.LEFT,padx=10)


    f5=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f5.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data5=Image.open("upperchest.png")
    resized5=image_data5.resize((70,70))
    photo5=ImageTk.PhotoImage(resized5)
    img_label5=tk.Label(f5,image=photo5,bg="light grey")
    img_label5.image=photo5
    img_label5.pack(side=tk.LEFT,padx=10)

    text5=tk.Label(f5,text="Incline Dumbell Fly\n\n3 sets- 10-12 reps Moderate weight\n Mainly targets upper chest and also trains little bit of the front deltoids of shoulders ",font="arial 11",bg="light gray",fg="black",justify="left")
    text5.pack(side=tk.LEFT,padx=10)


    f6=tk.Frame(main_frame,bg="light gray",height=90,pady=5)
    f6.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data6=Image.open("completechest.png")
    resized6=image_data6.resize((70,70))
    photo6=ImageTk.PhotoImage(resized6)
    img_label6=tk.Label(f6,image=photo6,bg="light grey")
    img_label6.image=photo6
    img_label6.pack(side=tk.LEFT,padx=10)

    text6=tk.Label(f6,text="Chest Fly\n\n3 sets- 10-12 reps Moderate weight\n targets complete chest and helps to give rounded shape to chest little bit trains the triceps also",font="arial 11",bg="light gray",fg="black",justify="left")
    text6.pack(side=tk.LEFT,padx=10)


def back_window():
    for widgets in root.winfo_children():
        widgets.destroy()
    root.title("Back muscle")
    root.maxsize(900, 600)
    f=tk.Frame(root,width=400,bg="white")
    f.pack(fill=tk.BOTH,side=tk.TOP)
    back_btn=tk.Button(f,text="<-- back to Select Muscles",font="arial 10 bold",bg="dark blue",fg="white",command=muscle_gain_window,pady=8)
    back_btn.pack(side=tk.LEFT,padx=10)
    tk.Label(f,bg="white",text="                                           ").pack(side=tk.LEFT,padx=20)
    tk.Label(f,text="Best Back Exercises",font="arial 15",bg="white",fg="black").pack(side=tk.LEFT,padx=20)

    main_frame=tk.Frame(root,width=700,height=500,bg="white")
    main_frame.pack(fill=tk.BOTH,expand=True)

    f1=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f1.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data1=Image.open("butterfly.png")
    resized1=image_data1.resize((70,70))
    photo1=ImageTk.PhotoImage(resized1)
    img_label1=tk.Label(f1,image=photo1,bg="light gray")
    img_label1.image=photo1
    img_label1.pack(side=tk.LEFT,padx=10)

    text=tk.Label(f1,text="double pully lats pull down\n\n3 sets- 10-15 reps .weighted\n targets butterfly area of back and traps also if trains properly",font="arial 11",bg="light gray",fg="black",justify="left")
    text.pack(side=tk.LEFT,padx=10)

    f2=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f2.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data2=Image.open("lowerlats.png")
    resized2=image_data2.resize((70,70))
    photo2=ImageTk.PhotoImage(resized2)
    img_label2=tk.Label(f2,image=photo2,bg="light gray")
    img_label2.image=photo2
    img_label2.pack(side=tk.LEFT,padx=10)

    text2=tk.Label(f2,text="reverse grip lat pulldown\n\n3 sets- 10-12 reps Heavy weight\n targets lower lats of back and also trains biceps and little bit effect forarms also",font="arial 11",bg="light gray",fg="black",justify="left")
    text2.pack(side=tk.LEFT,padx=10)

    f3=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f3.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data3=Image.open("pullups.png")
    resized3=image_data3.resize((70,70))
    photo3=ImageTk.PhotoImage(resized3)
    img_label3=tk.Label(f3,image=photo3,bg="light gray")
    img_label3.image=photo3
    img_label3.pack(side=tk.LEFT,padx=10)

    text3=tk.Label(f3,text="Pull-ups\n\n3 sets- 10-12 reps .bodyweight\n targets all-back muscles but mainly targets the upperlats of back little bit biceps also",font="arial 11",bg="light gray",fg="black",justify="left")
    text3.pack(side=tk.LEFT,padx=10)

    f4=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f4.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data4=Image.open("tree.png")
    resized4=image_data4.resize((70,70))
    photo4=ImageTk.PhotoImage(resized4)
    img_label4=tk.Label(f4,image=photo4,bg="light grey")
    img_label4.image=photo4
    img_label4.pack(side=tk.LEFT,padx=10)

    text4=tk.Label(f4,text="back extension\n\n3 sets- 10-12 reps Moderate weight\n targets lower back (tree area),that is very necessary for deadlifs and heavy training",font="arial 11",bg="light gray",fg="black",justify="left")
    text4.pack(side=tk.LEFT,padx=10)


    f5=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f5.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data5=Image.open("upperlats.png")
    resized5=image_data5.resize((70,70))
    photo5=ImageTk.PhotoImage(resized5)
    img_label5=tk.Label(f5,image=photo5,bg="light grey")
    img_label5.image=photo5
    img_label5.pack(side=tk.LEFT,padx=10)

    text5=tk.Label(f5,text="dumbbell rowing\n\n3 sets- 10-12 reps Heavy weight\n targets upper-lats of back but also trains the rhomboids and lower lats of back ",font="arial 11",bg="light gray",fg="black",justify="left")
    text5.pack(side=tk.LEFT,padx=10)


    f6=tk.Frame(main_frame,bg="light gray",height=90,pady=5)
    f6.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data6=Image.open("upperlats.png")
    resized6=image_data6.resize((70,70))
    photo6=ImageTk.PhotoImage(resized6)
    img_label6=tk.Label(f6,image=photo6,bg="light grey")
    img_label6.image=photo6
    img_label6.pack(side=tk.LEFT,padx=10)

    text6=tk.Label(f6,text="wide grip lat pulldown \n\n3 sets- 10-12 reps Heavy weight\n Mainly targets upper lats of back but also trains the traps and middle back ",font="arial 11",bg="light gray",fg="black",justify="left")
    text6.pack(side=tk.LEFT,padx=10)

def abs_window():
    for widgets in root.winfo_children():
        widgets.destroy()
    root.title("Abs muscle")
    root.maxsize(900, 600)
    f=tk.Frame(root,width=400,bg="white")
    f.pack(fill=tk.BOTH,side=tk.TOP)
    back_btn=tk.Button(f,text="<-- back to Select Muscles",font="arial 10 bold",bg="dark blue",fg="white",command=muscle_gain_window,pady=8)
    back_btn.pack(side=tk.LEFT,padx=10)
    tk.Label(f,bg="white",text="                                           ").pack(side=tk.LEFT,padx=20)
    tk.Label(f,text="Best Abs Exercises",font="arial 15",bg="white",fg="black").pack(side=tk.LEFT,padx=20)

    #changes from here
    main_frame=tk.Frame(root,width=700,height=500,bg="white")
    main_frame.pack(fill=tk.BOTH,expand=True)

    f1=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f1.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data1=Image.open("fullabs.png")
    resized1=image_data1.resize((70,70))
    photo1=ImageTk.PhotoImage(resized1)
    img_label1=tk.Label(f1,image=photo1,bg="light gray")
    img_label1.image=photo1
    img_label1.pack(side=tk.LEFT,padx=10)

    text=tk.Label(f1,text="Full Abdominal Crunch\n\n3 sets- 10-15 reps .bodyweight\n targets complete abs upper,middle,lower all trains by this exercise but less effective ",font="arial 11",bg="light gray",fg="black",justify="left")
    text.pack(side=tk.LEFT,padx=10)

    f2=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f2.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data2=Image.open("lowerabs.png")
    resized2=image_data2.resize((70,70))
    photo2=ImageTk.PhotoImage(resized2)
    img_label2=tk.Label(f2,image=photo2,bg="light gray")
    img_label2.image=photo2
    img_label2.pack(side=tk.LEFT,padx=10)

    text2=tk.Label(f2,text="Lower Abdominal Crunch\n\n3 sets- 10-12 reps .bodyweight\n Mainly targets lower abdominal muscle that difficult to train but this exercise is very effective for this ",font="arial 11",bg="light gray",fg="black",justify="left")
    text2.pack(side=tk.LEFT,padx=10)

    f3=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f3.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data3=Image.open("sideabs.png")
    resized3=image_data3.resize((70,70))
    photo3=ImageTk.PhotoImage(resized3)
    img_label3=tk.Label(f3,image=photo3,bg="light gray")
    img_label3.image=photo3
    img_label3.pack(side=tk.LEFT,padx=10)

    text3=tk.Label(f3,text="twister\n\n3 set till max\n Mainly targets love handels of abdominal muscle it is also a best exercise for fatlose",font="arial 11",bg="light gray",fg="black",justify="left")
    text3.pack(side=tk.LEFT,padx=10)

    f4=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f4.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data4=Image.open("upperabs.png")
    resized4=image_data4.resize((70,70))
    photo4=ImageTk.PhotoImage(resized4)
    img_label4=tk.Label(f4,image=photo4,bg="light grey")
    img_label4.image=photo4
    img_label4.pack(side=tk.LEFT,padx=10)

    text4=tk.Label(f4,text="cable supported crunches\n\n3 sets- 10-12 reps .modrate weight\n Mainly targets upper abs and it gives burn to lower abs also",font="arial 11",bg="light gray",fg="black",justify="left")
    text4.pack(side=tk.LEFT,padx=10)


    f5=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f5.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data5=Image.open("fullabs.png")
    resized5=image_data5.resize((70,70))
    photo5=ImageTk.PhotoImage(resized5)
    img_label5=tk.Label(f5,image=photo5,bg="light grey")
    img_label5.image=photo5
    img_label5.pack(side=tk.LEFT,padx=10)

    text5=tk.Label(f5,text="Plank\n\n1 set till failure\n target full abs try to give your maximum and do it at the end of your abs workout its double your abs workout",font="arial 11",bg="light gray",fg="black",justify="left")
    text5.pack(side=tk.LEFT,padx=10)


    f6=tk.Frame(main_frame,bg="light gray",height=90,pady=5)
    f6.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data6=Image.open("lowerabs.png")
    resized6=image_data6.resize((70,70))
    photo6=ImageTk.PhotoImage(resized6)
    img_label6=tk.Label(f6,image=photo6,bg="light grey")
    img_label6.image=photo6
    img_label6.pack(side=tk.LEFT,padx=10)

    text6=tk.Label(f6,text="hanging legs raises\n\n3 sets- 10-12 reps Body weight\n Mainly targets lower abs by handing on a pull-up bar raises your legs it burns yours abdominal muscles",font="arial 11",bg="light gray",fg="black",justify="left")
    text6.pack(side=tk.LEFT,padx=10)

def arms_window():
    for widgets in root.winfo_children():
        widgets.destroy()
    root.title("Arms muscle")
    root.maxsize(900, 600)
    f=tk.Frame(root,width=400,bg="white")
    f.pack(fill=tk.BOTH,side=tk.TOP)
    back_btn=tk.Button(f,text="<-- back to Select Muscles",font="arial 10 bold",bg="dark blue",fg="white",command=muscle_gain_window,pady=8)
    back_btn.pack(side=tk.LEFT,padx=10)
    tk.Label(f,bg="white",text="                                           ").pack(side=tk.LEFT,padx=20)
    tk.Label(f,text="Best Arms Exercises",font="arial 15",bg="white",fg="black").pack(side=tk.LEFT,padx=20)

    #changes from here
    main_frame=tk.Frame(root,width=700,height=500,bg="white")
    main_frame.pack(fill=tk.BOTH,expand=True)

    f1=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f1.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data1=Image.open("bicep.png")
    resized1=image_data1.resize((70,70))
    photo1=ImageTk.PhotoImage(resized1)
    img_label1=tk.Label(f1,image=photo1,bg="light gray")
    img_label1.image=photo1
    img_label1.pack(side=tk.LEFT,padx=10)

    text=tk.Label(f1,text="rod curls\n\n3 sets- 10-15 reps .heavy weight\n targets complete biceps but its mainly covers short head of bicep but good for whole bicep pump ",font="arial 11",bg="light gray",fg="black",justify="left")
    text.pack(side=tk.LEFT,padx=10)

    f2=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f2.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data2=Image.open("longhead.png")
    resized2=image_data2.resize((70,70))
    photo2=ImageTk.PhotoImage(resized2)
    img_label2=tk.Label(f2,image=photo2,bg="light gray")
    img_label2.image=photo2
    img_label2.pack(side=tk.LEFT,padx=10)

    text2=tk.Label(f2,text="incline dumbell curl\n\n3 sets- 10-12 reps Heavy weight\n Mainly targets long head of bicep that is mainly visible in looks and better for biceps development",font="arial 11",bg="light gray",fg="black",justify="left")
    text2.pack(side=tk.LEFT,padx=10)

    f3=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f3.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data3=Image.open("shorthead.png")
    resized3=image_data3.resize((70,70))
    photo3=ImageTk.PhotoImage(resized3)
    img_label3=tk.Label(f3,image=photo3,bg="light gray")
    img_label3.image=photo3
    img_label3.pack(side=tk.LEFT,padx=10)

    text3=tk.Label(f3,text="standing dumbell curl\n\n3 sets- 10-12 reps Heavy weight\n Mainly targets short head of bicep you can also uses ez bar for curls if dubells are not comfortable",font="arial 11",bg="light gray",fg="black",justify="left")
    text3.pack(side=tk.LEFT,padx=10)

    f4=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f4.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data4=Image.open("tricep.png")
    resized4=image_data4.resize((70,70))
    photo4=ImageTk.PhotoImage(resized4)
    img_label4=tk.Label(f4,image=photo4,bg="light grey")
    img_label4.image=photo4
    img_label4.pack(side=tk.LEFT,padx=10)

    text4=tk.Label(f4,text="tricep push down\n\n3 sets- 10-12 reps Moderate weight\n Mainly targets short head of tricep best for cuts and definition to complete tricep muscle ",font="arial 11",bg="light gray",fg="black",justify="left")
    text4.pack(side=tk.LEFT,padx=10)


    f5=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f5.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data5=Image.open("tricep2.png")
    resized5=image_data5.resize((70,70))
    photo5=ImageTk.PhotoImage(resized5)
    img_label5=tk.Label(f5,image=photo5,bg="light grey")
    img_label5.image=photo5
    img_label5.pack(side=tk.LEFT,padx=10)

    text5=tk.Label(f5,text="tricep pull over\n\n3 sets- 10-12 reps Moderate weight\n Mainly targets long head of tricep but also median head of tricep that muscle is mainly visible",font="arial 11",bg="light gray",fg="black",justify="left")
    text5.pack(side=tk.LEFT,padx=10)


    f6=tk.Frame(main_frame,bg="light gray",height=90,pady=5)
    f6.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data6=Image.open("medianhead.png")
    resized6=image_data6.resize((70,70))
    photo6=ImageTk.PhotoImage(resized6)
    img_label6=tk.Label(f6,image=photo6,bg="light grey")
    img_label6.image=photo6
    img_label6.pack(side=tk.LEFT,padx=10)

    text6=tk.Label(f6,text="one hand tricep extension\n\n3 sets- 15-20 reps Moderate weight\n Mainly targets median head of tricep it helps to gives a better pump and defination to the muscle",font="arial 11",bg="light gray",fg="black",justify="left")
    text6.pack(side=tk.LEFT,padx=10)

def shoulder_window():
    for widgets in root.winfo_children():
        widgets.destroy()
    root.title("Shoulder muscle")
    root.maxsize(900, 600)
    f=tk.Frame(root,width=400,bg="white")
    f.pack(fill=tk.BOTH,side=tk.TOP)
    back_btn=tk.Button(f,text="<-- back to Select Muscles",font="arial 10 bold",bg="dark blue",fg="white",command=muscle_gain_window,pady=8)
    back_btn.pack(side=tk.LEFT,padx=10)
    tk.Label(f,bg="white",text="                                           ").pack(side=tk.LEFT,padx=20)
    tk.Label(f,text="Best Shoulder Exercises",font="arial 15",bg="white",fg="black").pack(side=tk.LEFT,padx=20)

    #changes from here
    main_frame=tk.Frame(root,width=700,height=500,bg="white")
    main_frame.pack(fill=tk.BOTH,expand=True)

    f1=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f1.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data1=Image.open("frontdelt.png")
    resized1=image_data1.resize((70,70))
    photo1=ImageTk.PhotoImage(resized1)
    img_label1=tk.Label(f1,image=photo1,bg="light gray")
    img_label1.image=photo1
    img_label1.pack(side=tk.LEFT,padx=10)

    text=tk.Label(f1,text="Dumbell press\n\n3 sets- 10-15 reps .heavy weight\n mainly focus on front deltoids in this bench at 60% then this exercise will be more effective then normally",font="arial 11",bg="light gray",fg="black",justify="left")
    text.pack(side=tk.LEFT,padx=10)

    f2=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f2.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data2=Image.open("raredeelts.png")
    resized2=image_data2.resize((70,70))
    photo2=ImageTk.PhotoImage(resized2)
    img_label2=tk.Label(f2,image=photo2,bg="light gray")
    img_label2.image=photo2
    img_label2.pack(side=tk.LEFT,padx=10)

    text2=tk.Label(f2,text="face pull over\n\n3 sets- 15-20 reps Moderate weight\n Mainly targets rare deltoids but also helps in developingthe traps and rhomboids muscles",font="arial 11",bg="light gray",fg="black",justify="left")
    text2.pack(side=tk.LEFT,padx=10)

    f3=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f3.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data3=Image.open("shoulder.png")
    resized3=image_data3.resize((70,70))
    photo3=ImageTk.PhotoImage(resized3)
    img_label3=tk.Label(f3,image=photo3,bg="light gray")
    img_label3.image=photo3
    img_label3.pack(side=tk.LEFT,padx=10)

    text3=tk.Label(f3,text="machine shoulder press\n\n3 sets- 10-12 reps Heavy weight\n Mainly targets upper deltoids of shoulder but also helps in developing the middle deltoids",font="arial 11",bg="light gray",fg="black",justify="left")
    text3.pack(side=tk.LEFT,padx=10)

    f4=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f4.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data4=Image.open("sidedelts.png")
    resized4=image_data4.resize((70,70))
    photo4=ImageTk.PhotoImage(resized4)
    img_label4=tk.Label(f4,image=photo4,bg="light grey")
    img_label4.image=photo4
    img_label4.pack(side=tk.LEFT,padx=10)

    text4=tk.Label(f4,text="dumbell raises\n\n3 sets- 10-12 reps Moderate weight\n targets side deltoids of shoulders ,you can also uses cable machine that gives more stabalization to this exercise ",font="arial 11",bg="light gray",fg="black",justify="left")
    text4.pack(side=tk.LEFT,padx=10)


    f5=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f5.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data5=Image.open("shoulder.png")
    resized5=image_data5.resize((70,70))
    photo5=ImageTk.PhotoImage(resized5)
    img_label5=tk.Label(f5,image=photo5,bg="light grey")
    img_label5.image=photo5
    img_label5.pack(side=tk.LEFT,padx=10)

    text5=tk.Label(f5,text="Arnold Press\n\n3 sets- 10-12 reps Moderate weight\n Mainly targets complete shoulders but it is a combiination of three exercises that is best for complete shoulders",font="arial 11",bg="light gray",fg="black",justify="left")
    text5.pack(side=tk.LEFT,padx=10)


    f6=tk.Frame(main_frame,bg="light gray",height=90,pady=5)
    f6.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data6=Image.open("frontdelt.png")
    resized6=image_data6.resize((70,70))
    photo6=ImageTk.PhotoImage(resized6)
    img_label6=tk.Label(f6,image=photo6,bg="light grey")
    img_label6.image=photo6
    img_label6.pack(side=tk.LEFT,padx=10)

    text6=tk.Label(f6,text="Front Deltoid Raises\n\n3 sets- 10-12 reps Moderate weight\n Mainly targets front deltoids but it helps to strengthen the entire shoulder and give it a round shape",font="arial 11",bg="light gray",fg="black",justify="left")
    text6.pack(side=tk.LEFT,padx=10)

def legs_window():
    for widgets in root.winfo_children():
        widgets.destroy()
    root.title("Legs muscle")
    root.maxsize(900, 600)
    f=tk.Frame(root,width=400,bg="white")
    f.pack(fill=tk.BOTH,side=tk.TOP)
    back_btn=tk.Button(f,text="<-- back to Select Muscles",font="arial 10 bold",bg="dark blue",fg="white",command=muscle_gain_window,pady=8)
    back_btn.pack(side=tk.LEFT,padx=10)
    tk.Label(f,bg="white",text="                                           ").pack(side=tk.LEFT,padx=20)
    tk.Label(f,text="Best Legs Exercises",font="arial 15",bg="white",fg="black").pack(side=tk.LEFT,padx=20)

    #changes from here
    main_frame=tk.Frame(root,width=700,height=500,bg="white")
    main_frame.pack(fill=tk.BOTH,expand=True)

    f1=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f1.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data1=Image.open("leg1.png")
    resized1=image_data1.resize((70,70))
    photo1=ImageTk.PhotoImage(resized1)
    img_label1=tk.Label(f1,image=photo1,bg="light gray")
    img_label1.image=photo1
    img_label1.pack(side=tk.LEFT,padx=10)

    text=tk.Label(f1,text="leg press\n\n3 sets- 10-15 reps .heavy weight\n targets complete leg muscles but not to completely streight your legs while doing this exercise ",font="arial 11",bg="light gray",fg="black",justify="left")
    text.pack(side=tk.LEFT,padx=10)

    f2=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f2.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data2=Image.open("legs2.png")
    resized2=image_data2.resize((70,70))
    photo2=ImageTk.PhotoImage(resized2)
    img_label2=tk.Label(f2,image=photo2,bg="light gray")
    img_label2.image=photo2
    img_label2.pack(side=tk.LEFT,padx=10)

    text2=tk.Label(f2,text="Leg Curls\n\n3 sets- 10-12 reps Heavy weight\n very affective exercise for gluits muscle of legs little bit tricky but very affective for legs",font="arial 11",bg="light gray",fg="black",justify="left")
    text2.pack(side=tk.LEFT,padx=10)

    f3=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f3.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data3=Image.open("leg3.png")
    resized3=image_data3.resize((70,70))
    photo3=ImageTk.PhotoImage(resized3)
    img_label3=tk.Label(f3,image=photo3,bg="light gray")
    img_label3.image=photo3
    img_label3.pack(side=tk.LEFT,padx=10)

    text3=tk.Label(f3,text="Leg Extensions\n\n3 sets- 10-12 reps Moderate weight\n completely dominating the legs muscle best exercise ever",font="arial 11",bg="light gray",fg="black",justify="left")
    text3.pack(side=tk.LEFT,padx=10)

    f4=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f4.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data4=Image.open("leg1.png")
    resized4=image_data4.resize((70,70))
    photo4=ImageTk.PhotoImage(resized4)
    img_label4=tk.Label(f4,image=photo4,bg="light grey")
    img_label4.image=photo4
    img_label4.pack(side=tk.LEFT,padx=10)

    text4=tk.Label(f4,text="Leg Raises\n\n3 sets- 10-15 reps .modrate-weight\n targets front legs muscles best exercise of legs ever also train abdominal muscle also",font="arial 11",bg="light gray",fg="black",justify="left")
    text4.pack(side=tk.LEFT,padx=10)


    f5=tk.Frame(main_frame,bg="light gray",height=80,pady=5)
    f5.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data5=Image.open("legs2.png")
    resized5=image_data5.resize((70,70))
    photo5=ImageTk.PhotoImage(resized5)
    img_label5=tk.Label(f5,image=photo5,bg="light grey")
    img_label5.image=photo5
    img_label5.pack(side=tk.LEFT,padx=10)

    text5=tk.Label(f5,text="barbell extensions\n\n3 sets- 10-12 reps Heavy weight\n targets gluites muscle of legs also for cabs and slightly trains lower back also",font="arial 11",bg="light gray",fg="black",justify="left")
    text5.pack(side=tk.LEFT,padx=10)


    f6=tk.Frame(main_frame,bg="light gray",height=90,pady=5)
    f6.pack(fill=tk.BOTH,pady=5,padx=5)
    image_data6=Image.open("leg3.png")
    resized6=image_data6.resize((70,70))
    photo6=ImageTk.PhotoImage(resized6)
    img_label6=tk.Label(f6,image=photo6,bg="light grey")
    img_label6.image=photo6
    img_label6.pack(side=tk.LEFT,padx=10)

    text6=tk.Label(f6,text="sumo squats\n\n3 sets- 10-12 reps bodyweight\n targets internal muscles of legs, full dominating exercise for legs",font="arial 11",bg="light gray",fg="black",justify="left")
    text6.pack(side=tk.LEFT,padx=10)


sign_up_window()

root.mainloop()   
