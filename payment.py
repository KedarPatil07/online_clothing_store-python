from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as mysql
import ast

window = Tk()
window.title("Buy Now")
window.geometry("1100x500+300+200")
window.configure(bg="#fff")
window.resizable(False, False)

img = Image.open("Gray Red Black White Dark Red Photo Shopping Black Friday Sale Banner (4).png")
resizeimg = img.resize((1100,500))
newimg = ImageTk.PhotoImage(resizeimg)
Label(window, image=newimg, border=0,bg="white").place(x=0, y=0)

def pay1():
    bname=house_inpt.get()
    brname=landmrk_inpt.get()
    ifcode=street_lane_inpt.get()
    acc=village_city_inpt.get()
    mobile=village_city_inpt.get()
    try:
        connection = mysql.connect(host='localhost', user='root', password='', port='3306', database='buynow')
        c = connection.cursor()
        query="INSERT INTO payment(bankname,branchname,ifsccode,accountno,mobileno) VALUES ('"+str(bname)+\
              "','"+str(brname)+"','"+str(ifcode)+"','"+str(acc)+"','"+str(mobile)+"')"
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
canvas.create_text(550, 50, text="𝗣𝗔𝗬𝗠𝗘𝗡𝗧", font=('Microsoft YaHei Light', 30))


canvas.create_text(400, 100,text="𝗕𝗮𝗻𝗸 𝗡𝗮𝗺𝗲 :",  font=('Microsoft YaHei Light', 12))



house_inpt = Entry(window, width=35, fg="black", border=1, bg="white", font=("microsoft Yahei UI Light",11))
house_inpt.place(x=485, y=90)

canvas.create_text(405, 140, text="𝗕𝗿𝗮𝗻𝗰𝗵 𝗡𝗮𝗺𝗲 :", font=('Microsoft YaHei Light', 12))

landmrk_inpt = Entry(window, width=35, fg="black", border=1, bg="white", font=("microsoft Yahei UI Light",11))
landmrk_inpt.place(x=485, y=130)


canvas.create_text(400, 180, text="𝗜𝗙𝗦𝗖 𝗖𝗼𝗱𝗲 :", font=('Microsoft YaHei Light', 12))

street_lane_inpt = Entry(window, width=35, fg="black", border=1, bg="white", font=("microsoft Yahei UI Light",11))
street_lane_inpt.place(x=485, y=170)


canvas.create_text(400, 220, text="𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗡𝘂𝗺𝗯𝗲𝗿 :", font=('Microsoft YaHei Light', 12))



house_inpt = Entry(window, width=35, fg="black", border=1, bg="white", font=("microsoft Yahei UI Light",11))
house_inpt.place(x=485, y=210)


canvas.create_text(400, 260, text="𝗠𝗼𝗯𝗶𝗹𝗲 𝗡𝘂𝗺𝗯𝗲𝗿 :", font=('Microsoft YaHei Light', 12))


village_city_inpt = Entry(window, width=35, fg="black", border=1, bg="white", font=("microsoft Yahei UI Light",11))
village_city_inpt.place(x=485, y=250)



options = StringVar(window)

Button(window, width=40,height= 1, text="Conform", bg="black", fg="white", border=1, command=pay1).place(x=410, y=320)
Button(window, width=40,height= 1, text="𝗣𝗔𝗬", bg="black", fg="white", border=1, command=home).place(x=410, y=350)




window.mainloop()