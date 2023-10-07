from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import ast

window = Tk()
window.title("Sign Up")
window.geometry("1100x500+300+200")
window.configure(bg="#fff")
window.resizable(False, False)

def signup():
    uname = name.get()
    uemail = email.get()
    username = user.get()
    password = userpass.get()
    conform_pass = confpass.get()

    if password == conform_pass:
        try:
            file = open("datasheet.txt", "r+")
            d = file.read()
            r = ast.literal_eval(d)
            dict2 = {username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            #Connecting to the mysql------------------------------#
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="", port=3306, database='user_info')
                cursor = con.cursor()
                insert = "INSERT INTO signup(name, email, user_name, password) VALUES('"+str(uname)+"','"+str(uemail)+"','"+str(username)+"','"+str(password)+"')"
                cursor.execute(insert)
                con.commit()
                print("connected.")



            except:
                print("connection failed")

            file = open("datasheet.txt", "w")
            w = file.write(str(r))

            messagebox.showinfo("SignUp","Successfully sign up.")
        except:
            file = open("datasheet.txt","w")
            pp = str({"Username":"password"})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror("Invalid", "Both Password should match")


def sign():
    window.destroy()
    import login





img = Image.open("White and Brown Minimalist Fashion Banner Landscape (1).png")
resizeimg = img.resize((1100,500))
newimg = ImageTk.PhotoImage(resizeimg)
Label(window, image=newimg, border=0, bg="white").place(x=0, y=0)

frame = Frame(window, width=350, height=420, bg="#926a4b")
frame.place(x=700, y=30)

heading = Label(frame, text="𝗦𝗶𝗴𝗻 𝘂𝗽", fg="#000000",bg="#926a4b", font=("Microsoft Yahei UI Light", 30))
heading.place(x=100, y=5)

#---------Name-----------#

def on_enter_name(e):
    name.delete(0,"end")


def on_leave_name(e):
    if name.get() == "":
        name.insert(0, "Name")


name = Entry(frame, width=40, fg="black", border=0, bg="#926a4b", font=("microsoft Yahei UI Light",11))
name.place(x=30, y=70)
name.insert(0, "Name")
name.bind("<FocusIn>", on_enter_name)
name.bind("<FocusOut>", on_leave_name)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=95)


#---------Email-------------#

def on_enter_email(e):
    email.delete(0,"end")


def on_leave_email(e):
    if email.get() == "":
        email.insert(0, "Email")


email = Entry(frame, width=23, fg="black", border=0, bg="#926a4b", font=("microsoft Yahei UI Light",11))
email.place(x=30, y=120)
email.insert(0, "Email")
email.bind("<FocusIn>", on_enter_email)
email.bind("<FocusOut>", on_leave_email)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=145)


#---------Username-----------#

def on_enter_uname(e):
    user.delete(0,"end")


def on_leave_uname(e):
    if user.get() == "":
        user.insert(0, "Create Username")


user = Entry(frame, width=23, fg="black", border=0, bg="#926a4b", font=("microsoft Yahei UI Light",11))
user.place(x=30,y=170)
user.insert(0, "Create Username")
user.bind("<FocusIn>",on_enter_uname)
user.bind("<FocusOut>",on_leave_uname)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=195)


#----------Password-----------#


def on_enter_pass(e):
    userpass.delete(0, "end")


def on_leave_pass(e):
    if userpass.get() == "":
        userpass.insert(0, "Password")


userpass = Entry(frame, width=23, fg="black", border=0, bg="#926a4b", font=("microsoft Yahei UI Light",11))
userpass.place(x=30,y=220)
userpass.insert(0, "Password")
userpass.bind("<FocusIn>",on_enter_pass)
userpass.bind("<FocusOut>",on_leave_pass)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=245)


#----------Conform Password-----------#


def on_enter_cpass(e):
    confpass.delete(0,"end")


def on_leave_cpass(e):
    if confpass.get() == "":
        confpass.insert(0, "Conform Password")


confpass = Entry(frame, width=23, fg="black", border=0, bg="#926a4b", font=("microsoft Yahei UI Light", 11))
confpass.place(x=30, y=270)
confpass.insert(0, "Conform Password")
confpass.bind("<FocusIn>", on_enter_cpass)
confpass.bind("<FocusOut>", on_leave_cpass)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=295)

#

#--------Button--------#


Button(frame, width=39, pady=7, text="Sign Up", bg="#000000", fg="white", border=0, command=signup).place(x=35, y=330)
label = Label(frame, text = "I have an account?", fg="black", bg="#926a4b", font=("microsoft Yahei UI Ligh", 9))
label.place(x=90, y=385)

signin = Button(frame, width=6, text="Sign In", border=0, bg="#926a4b", cursor="hand2",fg="#57a1f8",font=10, command=sign)
signin.place(x=200, y=378)


window.mainloop()
