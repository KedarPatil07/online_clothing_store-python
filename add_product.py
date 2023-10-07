import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog


window = Tk()
window.title("Add product")
window.geometry("950x500+300+200")
window.configure(bg="#fff")
window.resizable(False, False)




img = Image.open("SEll YOUR OWN PRODUcT (1).png")
resizeimg = img.resize((925,500))
newimg = ImageTk.PhotoImage(resizeimg)
Label(window, image=newimg, border=0,bg="white").place(x=0, y=0)



def add():
    pname = name.get()
    proprice = price.get()
    quanti = qty.get()
    opt = options.get()
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="", port=3306, database="buynow")
        cursor = con.cursor()
        insert = "INSERT INTO addproduct(pro_name, category, price, quantity)  values('"+str(pname)+\
                 "','"+str(opt)+"','"+str(proprice)+"','"+str(quanti)+"')"
        cursor.execute(insert)
        con.commit()
        print("connected")
        window.destroy()
        import homesample
    except:
        print("failed")


frame = Frame(window, width=430, height=420, bg="#fff")
frame.place(x=550, y=30)

heading = Label(frame, text="Add Product Information", fg="#000000",bg="#fff", font=("Microsoft Yahei UI Light", 23, "bold"))
heading.place(x=10, y=25)


def on_enter_name(e):
    name.delete(0,"end")


def on_leave_name(e):
    if name.get() == "":
        name.insert(0, "Name of Product")


name = Entry(frame, width=23, fg="#000000", border=0, bg="#fff", font=("microsoft Yahei UI Light",11))
name.place(x=30, y=100)
name.insert(0, "Name of Product")
name.bind("<FocusIn>", on_enter_name)
name.bind("<FocusOut>", on_leave_name)

Frame(frame, width=295, height=2, bg="#000000").place(x=25, y=130)

cat = Entry(frame, width=23, fg="#000000", border=0, bg="#fff", font=("microsoft Yahei UI Light",11))
cat.place(x=30, y=170)
cat.insert(0, "Select Category")

options = StringVar(window)
options.set("Select Category")
optmnu =OptionMenu(frame,options,"Men","Women","Kids")
optmnu.place(x=190, y=165)

Frame(frame, width=295, height=2, bg="#000000").place(x=25, y=200)




def on_enter_price(e):
    price.delete(0,"end")


def on_leave_price(e):
    if price.get() == "":
        price.insert(0, "Price of Product per item")


price = Entry(frame, width=23, fg="#000000", border=0, bg="#fff", font=("microsoft Yahei UI Light",11))
price.place(x=30, y=240)
price.insert(0, "Price of Product per item")
price.bind("<FocusIn>", on_enter_price)
price.bind("<FocusOut>", on_leave_price)

Frame(frame, width=295, height=2, bg="#000000").place(x=25, y=265)


def on_enter_qty(e):
    qty.delete(0,"end")


def on_leave_qty(e):
    if qty.get() == "":
        qty.insert(0, "Quantity")


qty = Entry(frame, width=23, fg="#000000", border=0, bg="#fff", font=("microsoft Yahei UI Light",11))
qty.place(x=30, y=310)
qty.insert(0, "Quantity")
qty.bind("<FocusIn>", on_enter_qty)
qty.bind("<FocusOut>", on_leave_qty)

Frame(frame, width=295, height=2, bg="#000000").place(x=25, y=335)

Button(frame, width=39, pady=7, text="Add", bg="#000000", fg="#fff", border=0, command=add).place(x=35, y=370)

window.mainloop()