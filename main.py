from tkinter import *
from tkinter import messagebox
import pyqrcode
import png
from resizeimage import resizeimage
import qrcode

from PIL import ImageTk,Image

class Qrcodegenarate:
    def __init__(self,root):
        self.root = root
        self.root.title("My QR code genarator")
        img = PhotoImage(file="qr.png")
        self.root.iconphoto(False,img)
        self.root.geometry("900x500+200+50")
        self.root.config(bg="#bacdd9")
        self.root.resizable(0,0)

        self.std_name = StringVar()
        self.std_id = StringVar()
        self.std_dept = StringVar()
        self.std_sem = StringVar()

        heading = Label(self.root,text="   QR Code generator",font=("times new roman",40),bg="#165780",fg="White",anchor=W).place(x=0,y=0,relwidth=1)

        #Student window
        std_f = Frame(self.root,bd=2,relief=RIDGE,bg="White")
        std_f.place(x=50,y=100,width=500,height=380)



        std_heading = Label(std_f, text="Student details", font=("times new roman", 20), bg="#185f8c", fg="White").place(x=0, y=0, relwidth=1)

        std_label_1 = Label(std_f, text="Student Name", font=("times new roman", 15,"bold"), bg="#ffffff",
                            fg="black").place(x=45, y=60)
        std_label_2 = Label(std_f, text="Student ID", font=("times new roman", 15, "bold"), bg="#ffffff",
                            fg="black").place(x=45, y=110)
        std_label_3 = Label(std_f, text="Student Depertment", font=("times new roman", 15, "bold"), bg="#ffffff",
                            fg="black").place(x=45, y=160)
        std_label_4 = Label(std_f, text="Student Semester", font=("times new roman", 15, "bold"), bg="#ffffff",
                            fg="black").place(x=45, y=210)

        std_text_1 = Entry(std_f, font=("times new roman", 15), bg="#bacdd9",
                            fg="black",textvariable=self.std_name).place(x=227, y=60)
        std_text_2 = Entry(std_f, font=("times new roman", 15), bg="#bacdd9",
                            fg="black",textvariable=self.std_id).place(x=227, y=110)
        std_text_3 = Entry(std_f, font=("times new roman", 15), bg="#bacdd9",
                            fg="black",textvariable=self.std_dept).place(x=227, y=160)
        std_text_4 = Entry(std_f,font=("times new roman", 15), bg="#bacdd9",
                            fg="black",textvariable=self.std_sem).place(x=227, y=210)


        btn_1 = Button(std_f,text="Generate QR",font = ("times ner roman",18,"bold"),bg="#165780",fg="white",command=self.generate).place(x=50,y=265,width=160,height=30)
        btn_2 = Button(std_f, text="Clear All", font=("times ner roman", 18, "bold"), bg="#165780", fg="white",command=self.clear).place(
            x=270, y=265, width=160, height=30)\

        self.msg = ""
        self.msg_label = Label(std_f, text=self.msg, font=("times new roman", 20), bg="white", fg="green")
        self.msg_label.place(x=0, y=320, relwidth=1)

        # QR window
        QR_f = Frame(self.root, bd=2, relief=RIDGE, bg="White")
        QR_f.place(x=600, y=100, width=250, height=380)

        std_heading = Label(QR_f, text="Student QR code", font=("times new roman", 20), bg="#185f8c",
                            fg="White").place(x=0, y=0, relwidth=1)


        self.qr_label = Label(QR_f,text="No QR\nAvailable",font="arial 15",bg="#bacdd9",bd=1,relief=RIDGE)
        self.qr_label.place(x=35,y=100,width=180,height=180)


    def clear(self):
        self.std_name.set('')
        self.std_id.set('')
        self.std_dept.set('')
        self.std_sem.set('')
        self.msg = ""
        self.msg_label.config(text=self.msg)
    def generate(self):
        if self.std_dept.get() == "" or self.std_name.get() =="" or self.std_id.get() == "" or self.std_sem.get() == "":
            self.msg = "Required All Value"
            self.msg_label.config(text=self.msg,fg="red")
            messagebox.showerror("My QR code generator","Try again")

        else:
            data = (f"Student Name:{self.std_name.get()}\nStudent ID:{self.std_id.get()}\nStudent Dept:{self.std_dept.get()}\nStudent Semester:{self.std_sem.get()}")
            qr_code = qrcode.make(data)
            #print(qr_code)
            qr_code = resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("std_QR/std_"+str(self.std_name.get())+'.png',scale=10)
            self.imag = ImageTk.PhotoImage(qr_code)
            self.qr_label.config(image=self.imag)
            self.msg = "QR generated successfully.!"
            self.msg_label.config(text=self.msg, fg="green")

root = Tk()
run = Qrcodegenarate(root)
root.mainloop()