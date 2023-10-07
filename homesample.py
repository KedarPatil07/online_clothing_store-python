import tkinter as tk
import tkinter
from tkinter.ttk import Label
import cv

root = tkinter.Tk()
from PIL import Image, ImageTk
root.state('zoomed')
root.title("AK cloth store")
root.resizable(False,False)


def contact():
    root.destroy()
    import contactus

def about():
    root.destroy()
    import aboutus

def home():
    root.destroy()
    import homesample

def sign():
    root.destroy()
    import signup

def login():
    root.destroy()
    import login

def sellersign():
    root.destroy()
    import seller_sample

def sellerlogin():
    root.destroy()
    import sellerLogIn


def men():
    root.destroy()
    import mens

def women():
    root.destroy()
    import women

def kid():
    root.destroy()
    import kids



def suggestion():
    root.destroy()
    import suggestion

def orderreturn():
    root.destroy()
    import orderreturn

def admin():
    root.destroy()
    import administration



def toggle_menu():

    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='☰')
        toggle_btn.config(command=toggle_menu)




    toggle_menu_fm=tk.Frame(root,bg='#fff')
    window_height = 700
    toggle_menu_fm.place(x=0, y=50, height=window_height, width=200)
    toggle_btn.config(text='X')
    toggle_btn.config(command=collapse_toggle_menu)

    home_btn = tk.Button(toggle_menu_fm, text='   HOME              ', font=('bold', 16), bd=2, bg='#000000',
                         fg='white', activeforeground='#000000', activebackground='white', command=home)
    home_btn.place(x=0, y=20)


    contact_btn = tk.Button(toggle_menu_fm, text='   CONTACT US       ', font=('bold', 16), bd=2, bg='#000000', fg='white',
                            activeforeground='#000000', activebackground='white', command=contact)
    contact_btn.place(x=0, y=80)

    about_btn = tk.Button(toggle_menu_fm, text='   ABOUT US              ', font=('bold', 16), bd=2, bg='#000000',
                          fg='white',
                          activeforeground='#000000', activebackground='white', command=about)
    about_btn.place(x=0, y=140)

    about_btn = tk.Button(toggle_menu_fm, text='   Order Return                ', font=('bold', 16), bd=2, bg='#000000', fg='white',
                         activeforeground='#000000',activebackground='white',command=orderreturn)
    about_btn.place(x=0, y=200)

    about_btn = tk.Button(toggle_menu_fm, text='   Suggestion             ', font=('bold', 16), bd=2, bg='#000000', fg='white',
                         activeforeground='#000000',activebackground='white',command=suggestion)
    about_btn.place(x=0, y=260)

    contact_btn = tk.Button(toggle_menu_fm, text='    ADMINISTRATION             ', font=('bold', 12), bd=2, bg='#000000', fg='white',
                         activeforeground='#000000', activebackground='white',command=admin)
    contact_btn.place(x=0, y=320)

    window_height=root.winfo_height()
    toggle_menu_fm.place(x=0,y=50,height=window_height,width=170)
    toggle_btn.config(text='✖')
    toggle_btn.config(command=collapse_toggle_menu)

head_frame = tk.Frame(root, bg='#fff',highlightbackground='black',highlightthickness=1)
toggle_btn = tk.Button(head_frame,text="☰ ", bg="#fff",fg='black',font=('bold',20),bd=0,activeforeground='#fff',activebackground='black',command=toggle_menu)
toggle_btn.pack(side=tk.LEFT)

title_lb = tk.Label(head_frame,text='AK cloth store 👜', bg="#fff",fg='black',font=('bold',20))
title_lb.pack(side=tk.LEFT)
head_frame.pack(side=tk.TOP,fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)

frame1=tk.Frame(head_frame, bg="#fff")
frame1.pack(side=tk.RIGHT)
frame1.pack_propagate(False)
frame1.config(width=10)

sign_up_btn = tk.Button(head_frame, text='Sign Up', font=('bold', 12), bd=1, bg='#fff', fg='black',
                        activeforeground='#fff', activebackground='black', command=sign)
sign_up_btn.pack(side=tk.RIGHT)


frame1=tk.Frame(head_frame, bg="#fff")
frame1.pack(side=tk.RIGHT)
frame1.pack_propagate(False)
frame1.config(width=10)


Sign_In_btn = tk.Button(head_frame, text='Sign In', font=('bold', 12), bd=1, bg='#fff', fg='black',
                        activeforeground='#fff', activebackground='black', command=login)
Sign_In_btn.pack(side=tk.RIGHT)

frame1=tk.Frame(head_frame, bg="#fff")
frame1.pack(side=tk.RIGHT)
frame1.pack_propagate(False)
frame1.config(width=10)

sign_up_btn = tk.Button(head_frame, text=' Seller Sign Up', font=('bold', 12), bd=1, bg='#fff', fg='black',
                        activeforeground='#fff', activebackground='black', command=sellersign)
sign_up_btn.pack(side=tk.RIGHT)


frame1=tk.Frame(head_frame, bg="#fff")
frame1.pack(side=tk.RIGHT)
frame1.pack_propagate(False)
frame1.config(width=10)


Sign_In_btn = tk.Button(head_frame, text='Seller Sign In', font=('bold', 12), bd=1, bg='#fff', fg='black',
                        activeforeground='#fff', activebackground='black', command=sellerlogin)
Sign_In_btn.pack(side=tk.RIGHT)


Mens_btn = tk.Button(head_frame, text='Mens', font=('bold', 13), bd=0, bg='#fff', fg='black',
                        activeforeground='#fff', activebackground='black', command=men)
Mens_btn.place(x=700, y=13)


Women_btn = tk.Button(head_frame, text='Womens', font=('bold', 13), bd=0, bg='#fff', fg='black',
                        activeforeground='#fff', activebackground='black', command=women)
Women_btn.place(x=760, y=13)

Kids_btn = tk.Button(head_frame, text='Kids', font=('bold', 13), bd=0, bg='#fff', fg='black',
                        activeforeground='#fff', activebackground='black', command=kid)
Kids_btn.place(x=850, y=13)






item_frame=tk.Frame(root, bg="#000000")
item_frame.pack(side=tk.TOP, fill=tk.X)
item_frame.pack_propagate(False)
item_frame.config(height=800)




frame1=tk.Frame(item_frame, bg="#fff")
frame1.place(x=180, y=10)
frame1.pack_propagate(False)
frame1.config(width=310, height=350)

img = Image.open("Louvre.png.png")
resizeimg = img.resize((310,350))
newimg = ImageTk.PhotoImage(resizeimg)
Label(frame1, image=newimg, border=0).place(x=0, y=0)

heading = tk.Label(item_frame, text="                     𝗞𝗨𝗥𝗧𝗔                    ",bg="#fff", font=("Microsoft Yahei UI Light", 15))
heading.place(x=180, y=320)






item=tk.Frame(item_frame, bg="#fff")
item.place(x=520, y=10)
item.pack_propagate(False)
item.config(width=310, height=350)

img1 = Image.open("Fashion-_-Ravenstyles.png")
resizeimg = img1.resize((310,350))
newimg1 = ImageTk.PhotoImage(resizeimg)
Label(item, image=newimg1, border=0).place(x=0, y=0)

heading = tk.Label(item_frame, text="                     𝗦𝗛𝗜𝗥𝗧                     ",bg="#fff", font=("Microsoft Yahei UI Light", 15))
heading.place(x=520, y=320)


frame3=tk.Frame(item_frame, bg="#fff")
frame3.place(x=860, y=10)
frame3.pack_propagate(False)
frame3.config(width=310, height=350)

img2 = Image.open("New-Summer-High-Quality-Men-Polo-Shirts-High-Street-Print-Casual-Short-Sleeve-Mens-Shirts-Turn-Down-.png")
resizeimg = img2.resize((310,350))
newimg2 = ImageTk.PhotoImage(resizeimg)
Label(frame3, image=newimg2, border=0).place(x=0, y=0)

heading = tk.Label(item_frame, text="                     𝗧-𝗦𝗛𝗜𝗥𝗧                   ",bg="#fff", font=("Microsoft Yahei UI Light", 15))
heading.place(x=860, y=320)

frame4=tk.Frame(item_frame, bg="#fff")
frame4.place(x=1200, y=10)
frame4.pack_propagate(False)
frame4.config(width=310, height=350)

img3 = Image.open("Men-Light-Wash-Slant-Pocket-Jeans.png")
resizeimg = img3.resize((310,350))
newimg3 = ImageTk.PhotoImage(resizeimg)
Label(frame4, image=newimg3, border=0).place(x=0, y=0)

heading = tk.Label(item_frame, text="                      𝗝𝗘𝗔𝗡𝗦                    ",bg="#fff", font=("Microsoft Yahei UI Light", 15))
heading.place(x=1200, y=320)








frame5=tk.Frame(item_frame, bg="#fff")
frame5.place(x=180, y=380)
frame5.pack_propagate(False)
frame5.config(width=310, height=350)

img4= Image.open("Rashmika-Mandanna.png")
resizeimg = img4.resize((310,350))
newimg4 = ImageTk.PhotoImage(resizeimg)
Label(frame5, image=newimg4, border=0).place(x=0, y=0)

heading = tk.Label(item_frame, text="                     𝗞𝗨𝗥𝗧𝗜                     ",bg="#fff", font=("Microsoft Yahei UI Light", 15))
heading.place(x=180, y=690)


frame4=tk.Frame(item_frame, bg="#fff")
frame4.place(x=1200, y=380)
frame4.pack_propagate(False)
frame4.config(width=310, height=350)

img5 = Image.open("download.png")
resizeimg = img5.resize((310,350))
newimg5 = ImageTk.PhotoImage(resizeimg)
Label(frame4, image=newimg5, border=0).place(x=0, y=0)

frame3=tk.Frame(item_frame, bg="#fff")
frame3.place(x=860, y=380)
frame3.pack_propagate(False)
frame3.config(width=310, height=350)

img6 = Image.open("Rashmika Mandanna Age, Wiki, Family, Education, Boyfriend.png")
resizeimg = img6.resize((310,350))
newimg6 = ImageTk.PhotoImage(resizeimg)
Label(frame3, image=newimg6, border=0).place(x=0, y=0)

heading = tk.Label(item_frame, text="                   𝗪𝗘𝗦𝗧𝗘𝗥𝗡                 ",bg="#fff", font=("Microsoft Yahei UI Light", 15))
heading.place(x=860, y=690)

item=tk.Frame(item_frame, bg="#fff")
item.place(x=520, y=380)
item.pack_propagate(False)
item.config(width=310, height=350)

img7 = Image.open("Rashmika Mandanna walks the ramp at ICW'22 in a red embellished lehenga!.png")
resizeimg = img7.resize((310,350))
newimg7 = ImageTk.PhotoImage(resizeimg)
Label(item, image=newimg7, border=0).place(x=0, y=0)

heading = tk.Label(item_frame, text="                   𝗦𝗔𝗥𝗘𝗘                       ",bg="#fff", font=("Microsoft Yahei UI Light", 15))
heading.place(x=1200, y=690)


heading = tk.Label(item_frame, text="                     𝗟𝗘𝗛𝗘𝗡𝗚𝗔                ",bg="#fff", font=("Microsoft Yahei UI Light", 15))
heading.place(x=520, y=690)





root.mainloop()
