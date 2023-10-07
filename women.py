import tkinter as tk
from tkinter import *
import tkinter
from tkinter.ttk import Label
import cv



root = Tk()
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

def kurta():
    root.destroy()
    import kurta

def sign():
    root.destroy()
    import signup

def login():
    root.destroy()
    import login


def buynow():
    root.destroy()
    import Buy_now

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

    toggle_menu_fm = tk.Frame(root, bg='#fff')
    window_height = 700
    toggle_menu_fm.place(x=0, y=50, height=window_height, width=200)
    toggle_btn.config(text='X')
    toggle_btn.config(command=collapse_toggle_menu)

    home_btn = tk.Button(toggle_menu_fm, text='   HOME              ', font=('bold', 16), bd=2, bg='#000000',
                         fg='white', activeforeground='#000000', activebackground='white',command=home)
    home_btn.place(x=0, y=20)

    contact_btn = tk.Button(toggle_menu_fm, text='   CONTACT US       ', font=('bold', 16), bd=2, bg='#000000', fg='white',
                            activeforeground='#000000', activebackground='white',command=contact)
    contact_btn.place(x=0, y=80)

    about_btn = tk.Button(toggle_menu_fm, text='   ABOUT US              ', font=('bold', 16), bd=2, bg='#000000',
                          fg='white',
                          activeforeground='#000000', activebackground='white',command=about)
    about_btn.place(x=0, y=140)

    about_btn = tk.Button(toggle_menu_fm, text='   Order Return                ', font=('bold', 16), bd=2, bg='#000000',
                          fg='white',
                          activeforeground='#000000', activebackground='white', command=orderreturn)
    about_btn.place(x=0, y=200)

    about_btn = tk.Button(toggle_menu_fm, text='   Suggestion             ', font=('bold', 16), bd=2, bg='#000000',
                          fg='white',
                          activeforeground='#000000', activebackground='white', command=suggestion)
    about_btn.place(x=0, y=260)

    contact_btn = tk.Button(toggle_menu_fm, text='    ADMINISTRATION             ', font=('bold', 12), bd=2,
                            bg='#000000', fg='white',
                            activeforeground='#000000', activebackground='white', command=admin)
    contact_btn.place(x=0, y=320)

    window_height=root.winfo_height()
    toggle_menu_fm.place(x=0,y=50,height=window_height,width=170)
    toggle_btn.config(text='✖')
    toggle_btn.config(command=collapse_toggle_menu)

head_frame = tk.Frame(root, bg='#fff',highlightbackground='black',highlightthickness=1)
toggle_btn = tk.Button(head_frame,text="☰ ", bg="#fff",fg='black',font=('bold',20),bd=0,activeforeground='#fff',activebackground='white',command=toggle_menu)
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

Mens_btn = tk.Button(head_frame, text='Mens', font=('bold', 13), bd=0, bg='#fff', fg='black',
                        activeforeground='#fff', activebackground='black',command=men)
Mens_btn.place(x=750, y=13)


Women_btn = tk.Button(head_frame, text='Womens', font=('bold', 13), bd=0, bg='#fff', fg='black',
                        activeforeground='#fff', activebackground='black', command=women)
Women_btn.place(x=810, y=13)

Kids_btn = tk.Button(head_frame, text='Kids', font=('bold', 13), bd=0, bg='#fff', fg='black',
                        activeforeground='#fff', activebackground='black', command=kid)
Kids_btn.place(x=890, y=13)






item_frame=tk.Frame(root, bg="#000000")
item_frame.pack(side=tk.TOP, fill=tk.X)
item_frame.pack_propagate(False)
item_frame.config(height=800)



frame1=tk.Frame(item_frame, bg="#fff")
frame1.place(x=180, y=10)
frame1.pack_propagate(False)
frame1.config(width=310, height=700)

img = Image.open("Deep-Green-Mirror-Work-Kurta-Set.png")
resizeimg = img.resize((310,700))
newimg = ImageTk.PhotoImage(resizeimg)
Label(frame1, image=newimg, border=0).place(x=0, y=0)



heading = tk.Label(item_frame, text="Fit Type: Regular Fit                                              ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=180, y=545)

heading = tk.Label(item_frame, text="Occasion : Casual                                                  ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=180, y=565)

heading = tk.Label(item_frame, text="Fit : Regular Fit                                                     ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=180, y=585)

heading = tk.Label(item_frame, text="Material : 60% Cotton and 40% Polyester               ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=180, y=605)

heading = tk.Label(item_frame, text="Care Instructions: Machine Wash                           ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=180, y=625)

heading = tk.Label(item_frame, text="Pattern : Solid                                                       ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=180, y=645)

heading = tk.Label(item_frame, text="Rs. 999                Product no. 005",bg="#fff", font=("Microsoft Yahei UI Light", 15))
heading.place(x=180, y=668)


btn = tk.Button(root, width=43, height= 2, text="𝗕𝗨𝗬", bg="darkorange", fg="white", border=1, command=buynow).place(x=180, y=750)




item=tk.Frame(item_frame, bg="#fff")
item.place(x=520, y=10)
item.pack_propagate(False)
item.config(width=310, height=700)

img1 = Image.open("Red-Pink-and-Gold-Bridal-Lehenga-Set-Anisha-Shetty-East-Boutique.png")
resizeimg = img1.resize((310,700))
newimg1 = ImageTk.PhotoImage(resizeimg)
Label(item, image=newimg1, border=0).place(x=0, y=0)

heading = tk.Label(item_frame, text="Lehenga Fabric:Slub Silk ; Blouse Fabric:Slub Silk     ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=520, y=605)

heading = tk.Label(item_frame, text="Care Instructions: Dry Clean Only                           ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=520, y=625)

heading = tk.Label(item_frame, text="Fit Type: Regular                                                    ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=520, y=645)

heading = tk.Label(item_frame, text="Rs. 7999              Product no. 006",bg="#fff", font=("Microsoft Yahei UI Light", 15))
heading.place(x=520, y=668)

btn = tk.Button(root, width=43, height= 2, text="𝗕𝗨𝗬", bg="darkorange", fg="white", border=1,  command=buynow).place(x=520, y=750)


frame3=tk.Frame(item_frame, bg="#fff")
frame3.place(x=860, y=10)
frame3.pack_propagate(False)
frame3.config(width=310, height=700)

img2 = Image.open("77dba1e3-4446-435a-b6dd-7bfe4fbede82.png")
resizeimg = img2.resize((310,700))
newimg2 = ImageTk.PhotoImage(resizeimg)
Label(frame3, image=newimg2, border=0).place(x=0, y=0)

heading = tk.Label(item_frame, text="western dress                                                        ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=860, y=605)

heading = tk.Label(item_frame, text="Care Instructions: Machin wash                              ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=860, y=625)

heading = tk.Label(item_frame, text="Fit Type: Regular                                                   ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=860, y=645)

heading = tk.Label(item_frame, text="Rs. 999                Product no. 007",bg="#fff", font=("Microsoft Yahei UI Light", 15))
heading.place(x=860, y=668)

btn = tk.Button(root, width=43, height= 2, text="𝗕𝗨𝗬", bg="darkorange", fg="white", border=1,  command=buynow).place(x=860, y=750)


frame4=tk.Frame(item_frame, bg="#fff")
frame4.place(x=1200, y=10)
frame4.pack_propagate(False)
frame4.config(width=310, height=700)

img3 = Image.open("Sarees-Saree-Online-_-Indian-Sarees-Online-Shopping-with-Best-Price-at-joshindia.png")
resizeimg = img3.resize((310,700))
newimg3 = ImageTk.PhotoImage(resizeimg)
Label(frame4, image=newimg3, border=0).place(x=0, y=0)
#
heading = tk.Label(item_frame, text="Saree Fabric: Silk and cotton                                  ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=1200, y=605)

heading = tk.Label(item_frame, text="Care Instructions: Dry Clean Only                           ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=1200, y=625)

heading = tk.Label(item_frame, text="Hand work                                                            ",bg="#fff", font=("Microsoft Yahei UI Light", 10))
heading.place(x=1200, y=645)
heading = tk.Label(item_frame, text="Rs.1999               Product no. 008",bg="#fff", font=("Microsoft Yahei UI Light", 15))
heading.place(x=1200, y=668)

btn = tk.Button(root, width=43, height= 2, text="𝗕𝗨𝗬", bg="darkorange", fg="white", border=1,  command=buynow).place(x=1200, y=750)





root.mainloop()
