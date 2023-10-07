from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as mysql
import ast

window = Tk()
window.title("AK cloth store")
window.geometry("1100x500+300+200")
window.configure(bg="#fff")
window.resizable(False, False)

img = Image.open("Blue Simple Fashion Jeans Banner.png")
resizeimg = img.resize((1100,500))
newimg = ImageTk.PhotoImage(resizeimg)
Label(window, image=newimg, border=0,bg="white").place(x=0, y=0)

def cod():
    hname=house_inpt.get()
    lmark=landmrk_inpt.get()
    street=street_lane_inpt.get()
    city=village_city_inpt.get()
    state=options.get()
    pincode=pincode_inpt.get()
    try:
        connection = mysql.connect(host='localhost', user='root', password='', port='3306', database='buynow')
        c = connection.cursor()
        query="INSERT INTO buy(House_No,Landmark,Street_Lane,City_Village,State,Pincode) VALUES ('"+str(hname)+\
              "','"+str(lmark)+"','"+str(street)+"','"+str(city)+"','"+str(state)+"','"+str(pincode)+"')"
        c.execute(query)
        connection.commit()
        print("connected")
    except:
        print("faild")

def thanks():
    window.destroy()
    import thank
def UPI():
    window.destroy()
    import UPI

def payment():
    window.destroy()
    import payment

canvas=Canvas(window, width=400, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image = newimg, anchor = "nw")
canvas.create_text(550, 50, text="𝗔𝗗𝗗𝗥𝗘𝗦𝗦", font=('Microsoft YaHei Light', 30))


canvas.create_text(400, 100, text="House No. :", font=('Microsoft YaHei Light', 12, 'bold'))


house_inpt = Entry(window, width=35, fg="black", border=1, bg="white", font=("microsoft Yahei UI Light",11))
house_inpt.place(x=470, y=85)

canvas.create_text(400, 145, text="Land Mark :", font=('Microsoft YaHei Light', 12, 'bold'))


landmrk_inpt = Entry(window, width=35, fg="black", border=1, bg="white", font=("microsoft Yahei UI Light",11))
landmrk_inpt.place(x=470, y=130)

canvas.create_text(400, 190, text="Street\Lane :", font=('Microsoft YaHei Light', 12, 'bold'))


street_lane_inpt = Entry(window, width=35, fg="black", border=1, bg="white", font=("microsoft Yahei UI Light",11))
street_lane_inpt.place(x=470, y=175)

canvas.create_text(400, 235, text="City\Village :", font=('Microsoft YaHei Light', 12, 'bold'))

village_city_inpt = Entry(window, width=35, fg="black", border=1, bg="white", font=("microsoft Yahei UI Light",11))
village_city_inpt.place(x=470, y=220)

canvas.create_text(375, 280, text="State :", font=('Microsoft YaHei Light', 12, 'bold'))

options = StringVar(window)
options.set("Select State")
optmnu =OptionMenu(window,options,"Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
                   "Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh",
                   "Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim",
                   "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal",
                   "Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep",
                   "National Capital Territory of Delhi","Puducherry")
optmnu.place(x=470, y=265)

canvas.create_text(385, 325, text="Pincode :", font=('Microsoft YaHei Light', 12, 'bold'))


pincode_inpt = Entry(window, width=35, fg="black", border=1, bg="white", font=("microsoft Yahei UI Light",11))
pincode_inpt.place(x=470, y=310)

canvas.create_text(350, 390, text="Select Payment Method :", font=('Microsoft YaHei Light', 12, 'bold'))


Button(window, width=13,height= 1, text="Save address", bg="darkorange", fg="white", border=1,command=cod).place(x=585, y=340)
Button(window, width=13,height= 1, text="Cash on delivery", bg="darkorange", fg="white", border=1,command=thanks).place(x=470, y=380)
Button(window, width=10,height= 1, text="Net Banking", bg="darkorange", fg="white", border=1, command=payment).place(x=585, y=380)
Button(window, width=10,height= 1, text="UPI", bg="darkorange", fg="white", border=1, command=UPI).place(x=680, y=380)

print(optmnu)

window.mainloop()