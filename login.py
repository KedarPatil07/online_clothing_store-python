from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
root=Tk()
root.title("AK cloth store")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)


def signup():
    root.destroy()
    import signup


def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen, text='Hello Everyone!', bg='#fff', font=('Calibre(Body)', 50, 'bold')).pack(expand=True)

        screen.mainloop()

    try:
        conn = mysql.connector.connect(host="localhost", user="root", passwd="", port='3306', database='user_info')
        my_corser = conn.cursor()
        select = "select user_name, password from  signup where user_name='" + username + "' and password = '" + password + "' "
        print(type(select))
        my_corser.execute(select)
        passanduser = list(my_corser.fetchone())
        if username == passanduser[0] and password == str(passanduser[1]):
            print("Login successfully.")
            print("username", passanduser[0])
            print("password", passanduser[1])
            messagebox.showinfo(title="Login", message="Login Successfully")
        # conn.commit()
        print("connected")
        root.destroy()
        import homesample



    except:
        print("failed connection")


img = (Image.open('Beige Modern Fashion Collection (Banner (Landscape)).png'))
resizeimg=img.resize((950,500), Image.ANTIALIAS)
newimg=ImageTk.PhotoImage(resizeimg)
Label(root, image=newimg, bg='#c2b5a6').place(x=0, y=0)


frame = Frame(root, width=350, height=350, bg="#c2b5a6")
frame.place(x=560,y=70)

heading = Label(frame, text='𝗦𝗶𝗴𝗻 𝗶𝗻', fg='#000000', bg='#c2b5a6', font=('Microsoft YaHei Light', 30))
heading.place(x=125, y=5)


def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg="#c2b5a6", font=('Microsoft YaHei Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name=='':
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg="#c2b5a6", font=('Microsoft YaHei Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


Button(frame, width=39, pady=7, text='Sign in', bg='#000000', fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='#c2b5a6', font=('Microsoft YaHei Light', 9))
label.place(x=80, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='#c2b5a6', cursor='hand2', fg='#004aad',font=('Microsoft YaHei Light', 11),command=signup)
sign_up.place(x=220, y=265)



root.mainloop()