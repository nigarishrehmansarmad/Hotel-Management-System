from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from time import strftime
from datetime import datetime
from tkinter import messagebox
import random

class  details_room:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Details")
        self.root.geometry("1550x800+0+0")

        #==================== VARIABLES ===================
        self.var_floor=StringVar()

        self.var_room_num=StringVar()
        x=random.randint(100,999)
        self.var_room_num.set(str(x))

        self.var_room_type=StringVar()



        #============background image========================
        img=Image.open(r"C:\Users\HUSSAIN\OneDrive\Desktop\hotel management system\ROOM DETAILS.png")
        img=img.resize((1280,670),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        label_img=Label(self.root,image=self.photoimg,bd=0)
        label_img.place(x=0,y=0,width=1280,height=670)

        #============label frame=========================
        label_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Adding Room Details",padx=2,font=("Open Sauce",20),bg="#a2b8c2",fg="white")
        label_frame.place(x=0,y=140,width=540,height=510)

        #=============labels & entries=====================
        # Floor
        label_floor=Label(label_frame,text="Floor: ",font=("Alice",12,"bold"))
        label_floor.grid(row=0,column=0)

        combo_floor=ttk.Combobox(label_frame,textvariable=self.var_floor,font=("Alice",12),state="readonly")
        combo_floor["value"]=("1","2","3","4")
        combo_floor.current(0)
        combo_floor.grid(row=0,column=1,padx=2)

        # Room No.
        label_room_num=Label(label_frame,text="Room No.: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_room_num.grid(row=1,column=0)

        entry_ref1=ttk.Entry(label_frame,width=22,font=("calibri",12),textvariable=self.var_room_num)
        entry_ref1.grid(row=1,column=1)

        # Room Type
        label_room_type=Label(label_frame,text="Room Type: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_room_type.grid(row=2,column=0,sticky=W)

        combo_room_type=ttk.Combobox(label_frame,textvariable=self.var_room_type,font=("Alice",12),state="readonly")
        combo_room_type["value"]=("Single","Double","Luxury")
        combo_room_type.current(0)
        combo_room_type.grid(row=2,column=1)

        # button frame
        btn_frame=Frame(label_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=50,y=425,width=412,height=40)

        # add button
        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("Alice",12,"bold"),bg="#56707b",fg="white",width=9,cursor="hand2")
        btn_add.grid(row=0,column=0,padx=1)

        #update button
        btn_update=Button(btn_frame,text="Update",command=self.update,font=("Alice",12,"bold"),bg="#56707b",fg="white",width=9,cursor="hand2")
        btn_update.grid(row=0,column=1,padx=1)

        #delete button
        btn_delete=Button(btn_frame,text="Delete",command=self.mDelete,font=("Alice",12,"bold"),bg="#56707b",fg="white",width=9,cursor="hand2")
        btn_delete.grid(row=0,column=2,padx=1)

        # reset button
        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("Alice",12,"bold"),bg="#56707b",fg="white",width=9,cursor="hand2")
        btn_reset.grid(row=0,column=3,padx=1)

        #========= table frame ================
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Search Details",padx=2,font=("Alice",18),bg="#a2b8c2",fg="white")
        table_frame.place(x=550,y=148,width=730,height=400)


        #====== Show Data Table===========
        details_table=LabelFrame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=720,height=300)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("Floor","Room No.","Room Type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Floor",text="Floor")
        self.room_table.heading("Room No.",text="Room No.")
        self.room_table.heading("Room Type",text="Room Type")
        

        self.room_table["show"]="headings"

        self.room_table.column("Floor")
        self.room_table.column("Room No.")
        self.room_table.column("Room Type")
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #================= ADD FUNCTION ===========================
    def add_data(self):
        if self.var_room_num.get()=="" or self.var_room_type.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                            self.var_floor.get(),
                                                                            self.var_room_num.get(),
                                                                            self.var_room_type.get()
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Details Added!",parent=self.root)
            except  Exception   as es:
                messagebox.showwarning("Warning",f"Something went wrong.:{str(es)}",parent=self.root)

    #====================== Fetch Data Function=========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #======================= GET CURSOR FUNCTION ==========================
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0])
        self.var_room_num.set(row[1])
        self.var_room_type.set(row[2])

    def update(self):
        if self.var_room_type.get() == "":
            messagebox.showerror("Error", "Please enter room type", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="AlishbaAnwar16%", database="hotel")
            my_cursor = conn.cursor()
            
            my_cursor.execute("UPDATE details SET Floor=%s, `Room No.`=%s, `Room Type`=%s WHERE `Room No.`=%s", (
                                                                                            self.var_floor.get(),
                                                                                            self.var_room_num.get(),
                                                                                            self.var_room_type.get(),
                                                                                            self.var_room_num.get()
                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated", "Room details have been updated successfully.", parent=self.root)


    def mDelete(self):
        mDelete = messagebox.askyesno("Azure Bliss", "Do you want to delete this room?", parent=self.root)
        if mDelete:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="AlishbaAnwar16%", database="hotel")
                my_cursor = conn.cursor()
                query = "DELETE FROM details WHERE `Room No.`=%s"
                value = (self.var_room_num.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room deleted successfully.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting room: {str(e)}", parent=self.root)
        else:
            return
        
    def reset_data(self):

        self.var_floor.set(""),
        self.var_room_num.set("")
        x=random.randint(100,999)
        self.var_room_num.set(str(x)),
        self.var_room_type.set("")


if __name__ == "__main__":
    root=Tk()
    obj= details_room(root)
    root.mainloop()