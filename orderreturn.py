from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as mysql
import ast

window = Tk()
window.title("Order Return")
window.geometry("1000x500+300+200")
window.configure(bg="#fff")
window.resizable(False, False)

img = Image.open("AK Cloth Store (1).png")
resizeimg = img.resize((1100,500))
newimg = ImageTk.PhotoImage(resizeimg)
Label(window, image=newimg, border=0,bg="white").place(x=0, y=0)

def conform():
    pcode=house_inpt.get()
    twhy=str(options.get())
    print(twhy)
    try:
        connection = mysql.connect(host='localhost', user='root', password='', port='3306', database='buynow')
        c = connection.cursor()
        query="INSERT INTO orderreturn(productcode,why) VALUES ('"+str(pcode)+"','"+twhy+"')"
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
canvas.create_text(550, 50, text="𝗢𝗿𝗱𝗲𝗿 𝗥𝗲𝘁𝘂𝗿𝗻", font=('Microsoft YaHei Light', 30))



canvas.create_text(450, 100,text="𝗣𝗿𝗼𝗱𝘂𝗰𝘁 𝗰𝗼𝗱𝗲 :",  font=('Microsoft YaHei Light', 12, 'bold'))


house_inpt = Entry(window, width=35, fg="black", border=1, bg="white", font=("microsoft Yahei UI Light",11))
house_inpt.place(x=540, y=90)



canvas.create_text(350, 140, text="𝗪𝗵𝘆 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝘁𝗵𝗶𝘀 𝗽𝗿𝗼𝗱𝘂𝗰𝘁 :", font=('Microsoft YaHei Light', 12, 'bold'))
options = StringVar(window)
options.set("Select one")
optmnu =OptionMenu(window,options,"Size of product is big","Size of product is small ","Defective product","Got different product")
optmnu.place(x=540, y=130)



Button(window, width=40,height= 1, text="DONE", bg="black", fg="white", border=1, command=conform).place(x=410, y=370)
Button(window, width=40,height= 1, text="𝗖𝗼𝗻𝗳𝗼𝗿𝗺", bg="black", fg="white", border=1, command=home).place(x=410, y=410)




window.mainloop()