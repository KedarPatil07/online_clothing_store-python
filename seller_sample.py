from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as mysql
import ast

window = Tk()
window.title("Sign up as a Seller")
window.geometry("1000x500+300+200")
window.configure(bg="#fff")
window.resizable(False, False)


def signup():
    uname = name.get()
    gmail = email.get()
    username = user.get()
    password = userpass.get()
    conform_pass = confpass.get()
    add = adderss.get()
    contact = cont.get()



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
                con = mysql.connect(host="localhost", port="3306",user="root", password="", database="user_info")
                cursor = con.cursor()
                cursor.execute("INSERT INTO sellerinfo(name,email,user_name,pass,address,contact) values('"+str(uname)+"','"+str(gmail)+"','"+str(username)+"','"+str(password)+"','"+str(add)+"','"+str(contact)+"')")
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
    import sellerLogIn


img = Image.open("BE the BEST SELLER (1).png")
resizeimg = img.resize((1000,500))
newimg = ImageTk.PhotoImage(resizeimg)
Label(window, image=newimg, border=0,bg="white").place(x=0, y=0)

canvas=Canvas(window, width=400, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image = newimg, anchor = "nw")
canvas.create_text(760, 40, text="𝗟𝗼𝗴 𝗶𝗻 𝗮𝘀 𝗮 𝗦𝗲𝗹𝗹𝗲𝗿", font=('Microsoft YaHei Light', 30))



#---------Name-----------#

def on_enter_name(e):
    name.delete(0,"end")


def on_leave_name(e):
    if name.get() == "":
        name.insert(0, "Name")


name = Entry(window, width=35, fg="black", border=0, bg="#ece8e3", font=("microsoft Yahei UI Light",11))
name.place(x=610, y=70)
name.insert(0, "Name")
name.bind("<FocusIn>", on_enter_name)
name.bind("<FocusOut>", on_leave_name)

Frame(window, width=295, height=2, bg="black").place(x=610, y=95)


#---------Email-------------#

def on_enter_email(e):
    email.delete(0,"end")


def on_leave_email(e):
    if email.get() == "":
        email.insert(0, "Email")


email = Entry(window, width=35, fg="black", border=0, bg="#ece8e3", font=("microsoft Yahei UI Light",11))
email.place(x=610, y=120)
email.insert(0, "Email")
email.bind("<FocusIn>", on_enter_email)
email.bind("<FocusOut>", on_leave_email)

Frame(window, width=295, height=2, bg="black").place(x=610, y=145)


#---------Username-----------#

def on_enter_uname(e):
    user.delete(0,"end")


def on_leave_uname(e):
    if user.get() == "":
        user.insert(0, "Create Username")


user = Entry(window, width=35, fg="black", border=0, bg="#ece8e3", font=("microsoft Yahei UI Light",11))
user.place(x=610,y=170)
user.insert(0, "Create Username")
user.bind("<FocusIn>",on_enter_uname)
user.bind("<FocusOut>",on_leave_uname)

Frame(window, width=295, height=2, bg="black").place(x=610, y=195)


#----------Password-----------#


def on_enter_pass(e):
    userpass.delete(0, "end")


def on_leave_pass(e):
    if userpass.get() == "":
        userpass.insert(0, "Password")


userpass = Entry(window, width=35, fg="black", border=0, bg="#ece8e3", font=("microsoft Yahei UI Light",11))
userpass.place(x=610,y=220)
userpass.insert(0, "Password")
userpass.bind("<FocusIn>",on_enter_pass)
userpass.bind("<FocusOut>",on_leave_pass)

Frame(window, width=295, height=2, bg="black").place(x=610, y=245)


#----------Conform Password-----------#


def on_enter_cpass(e):
    confpass.delete(0,"end")


def on_leave_cpass(e):
    if confpass.get() == "":
        confpass.insert(0, "Create Username")

confpass = Entry(window, width=35, fg="black", border=0, bg="#ece8e3", font=("microsoft Yahei UI Light", 11))
confpass.place(x=610, y=270)
confpass.insert(0, "Conform Password")
confpass.bind("<FocusIn>", on_enter_cpass)
confpass.bind("<FocusOut>", on_leave_cpass)

Frame(window, width=295, height=2, bg="black").place(x=610, y=295)

#--------Address------#


def on_enter_add(e):
    adderss.delete(0, "end")


def on_leave_add(e):
    if adderss.get() == "":
        adderss.insert(0, "Address")


adderss = Entry(window, width=35, fg="black", border=0, bg="#ece8e3", font=("microsoft Yahei UI Light", 11))
adderss.place(x=610, y=320)
adderss.insert(0, "Address")
adderss.bind("<FocusIn>", on_enter_add)
adderss.bind("<FocusOut>", on_leave_add)

Frame(window, width=295, height=2, bg="black").place(x=610, y=345)

#-------contact------#


def on_enter_cont(e):
    cont.delete(0, "end")


def on_leave_cont(e):
    if cont.get() == "":
        cont.insert(0, "Contact")


cont = Entry(window, width=35, fg="black", border=0, bg="#ece8e3", font=("microsoft Yahei UI Light", 11))
cont.place(x=610, y=370)
cont.insert(0, "Contact")
cont.bind("<FocusIn>", on_enter_cont)
cont.bind("<FocusOut>", on_leave_cont)

Frame(window, width=295, height=2, bg="black").place(x=610, y=395)

#--------Button--------#


Button(window, width=39, pady=7, text="Sign Up", bg="#8B7861", fg="#ece8e3", border=0, command=signup).place(x=618, y=410)
label = Label(window, text = "I have an account?", fg="black", bg="#ece8e3", font=("microsoft Yahei UI Ligh", 9))
label.place(x=680, y=450)

signin = Button(window, width=6, text="Sing In", border=0, bg="#ece8e3", cursor="hand2",fg="#57a1f8", command=sign)
signin.place(x=790, y=450)


window.mainloop()
