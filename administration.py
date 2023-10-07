from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
root=Tk()
root.title('Administrator')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)




def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password=='1234':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")


        root.destroy()
        import riportframe

        screen.mainloop()

    elif username!='admin' and password!='1234':
        messagebox.showerror("Invalid", "invalid username and password")

    elif password!="1234":
        messagebox.showerror("Invalid", "invalid password")

    elif username!='admin':
        messagebox.showerror("Invalid", "invalid username")

img = (Image.open('Green Gradient Digital Marketing Agency Facebook Ad.png'))
resizeimg=img.resize((950,500), Image.ANTIALIAS)
newimg=ImageTk.PhotoImage(resizeimg)
Label(root, image=newimg, bg='#e3ecee').place(x=0, y=0)


frame = Frame(root, width=350, height=350, bg="#e3ecee")
frame.place(x=500,y=70)

heading = Label(frame, text='Administration Login', fg='#57a1f8', bg='#e3ecee', font=('Microsoft YaHei Light', 23, 'bold'))
heading.place(x=10, y=5)


def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg="#e3ecee", font=('Microsoft YaHei Light', 11))
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

code = Entry(frame, width=25, fg='black', border=0, bg="#e3ecee", font=('Microsoft YaHei Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)



root.mainloop()