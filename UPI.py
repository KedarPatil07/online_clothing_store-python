from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as mysql
import ast

window = Tk()
window.title("UPI")
window.geometry("1100x500+300+200")
window.configure(bg="#fff")
window.resizable(False, False)

img = Image.open("UPI.png")
resizeimg = img.resize((1100,500))
newimg = ImageTk.PhotoImage(resizeimg)
Label(window, image=newimg, border=0,bg="white").place(x=0, y=0)

def upi():
    upid=house.get()
    otpno=house_inpt.get()

    try:
        connection = mysql.connect(host='localhost', user='root', password='', port='3306', database='buynow')
        c = connection.cursor()
        query="INSERT INTO upi(upiid,otp) VALUES ('"+str(upid)+"','"+str(otpno)+"')"
        c.execute(query)
        connection.commit()
        print("connected")
    except:
        print("faild")

def home():
    window.destroy()
    import homesample

canvas=Canvas(window, width=400, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image = newimg, anchor = "nw")
canvas.create_text(550, 50, text="𝗨𝗣𝗜", font=('Microsoft YaHei Light', 30))


canvas.create_text(400, 120, text="𝗨𝗣𝗜 𝗜𝗱 :", font=('Microsoft YaHei Light', 12, 'bold'))



house = Entry(window, width=35, fg="black", border=1, bg="white", font=("microsoft Yahei UI Light",11))
house.place(x=440, y=110)

canvas.create_text(390, 170, text="𝗢𝗧𝗣 :", font=('Microsoft YaHei Light', 12, 'bold'))

house_inpt = Entry(window, width=35, fg="black", border=1, bg="white", font=("microsoft Yahei UI Light",11))
house_inpt.place(x=440, y=160)




options = StringVar(window)
Button(window, width=20,text="Conform", bg="black", fg="white", border=0, command=upi).place(x=475, y=210)
Button(window, width=20,text="𝗣𝗔𝗬", bg="black", fg="white", border=0, command=home).place(x=475, y=240)




window.mainloop()