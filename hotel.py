from tkinter import *
from PIL import Image, ImageTk
from customer import customer
from room import room
from details import details_room
from report import report

class hms:
    def __init__(self,root):
        self.root=root
        self.root.title("Azure Bliss")
        self.root.geometry("1550x800+0+0")


        img1=Image.open(r"C:\Users\HUSSAIN\OneDrive\Desktop\hotel management system\final hotel.png")
        img1=img1.resize((1280,670),Image.LANCZOS)
        self.photoimg1= ImageTk.PhotoImage(img1)
        label_img=Label(self.root,image=self.photoimg1,bd=0)
        label_img.place(x=0,y=0,width=1280,height=670)

        #=============main frame=================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        
        #=============MENU=======================
        label_menu=Label(main_frame,text="MENU",font=("Broadway",20),bg="#6088b1",fg="white",bd=4,relief=RIDGE)
        label_menu.place(x=0,y=0,width=230)


        #=============button frame================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        #============all buttons===============
        cust_btn=Button(btn_frame,width=22,text="Customer",command=self.cust_details,font=("Century Gothic",14,"bold"),bg="#bbcce2",fg="#545454",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,width=22,text="Room Booking",command=self.roombooking,font=("Century Gothic",14,"bold"),bg="#bbcce2",fg="#545454",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,width=22,text="Room Details",command=self.details_room,font=("Century Gothic",14,"bold"),bg="#bbcce2",fg="#545454",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,width=22,text="Report",command=self.report,font=("Century Gothic",14,"bold"),bg="#bbcce2",fg="#545454",bd=0,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,width=22,text="Log Out",command=self.logout,font=("Century Gothic",14,"bold"),bg="#bbcce2",fg="#545454",bd=0,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)

        #===============down image==========
        img2=Image.open(r"C:\Users\HUSSAIN\OneDrive\Desktop\hotel management system\download.jpg")
        img2=img2.resize((230,235),Image.LANCZOS)
        self.photoimg2= ImageTk.PhotoImage(img2)
        label_img2=Label(main_frame,image=self.photoimg2,bd=0)
        label_img2.place(x=0,y=228,width=230,height=235)

        #===============right side image===========
        img3=Image.open(r"C:\Users\HUSSAIN\OneDrive\Desktop\hotel management system\greece1.png")
        img3=img3.resize((1100,465),Image.LANCZOS)
        self.photoimg3= ImageTk.PhotoImage(img3)
        label_img3=Label(main_frame,image=self.photoimg3,bd=0)
        label_img3.place(x=230,y=0,width=1100,height=465)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=customer(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=room(self.new_window)    

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=details_room(self.new_window)

    def report(self):
        self.new_window=Toplevel(self.root)
        self.app=report(self.new_window)

    def logout(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=hms(root)
    root.mainloop()
    


