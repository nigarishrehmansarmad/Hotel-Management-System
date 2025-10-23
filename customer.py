from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class customer:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer")
        self.root.geometry("1295x550+0+0")

        #============variable=============================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name=StringVar()
        self.var_mobile_num=StringVar()
        self.var_gender=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_id_num=StringVar()
        self.var_address=StringVar()
        self.var_email=StringVar()


        #============background image========================
        img=Image.open(r"C:\Users\HUSSAIN\OneDrive\Desktop\hotel management system\bell.png")
        img=img.resize((1280,670),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        label_img=Label(self.root,image=self.photoimg,bd=0)
        label_img.place(x=0,y=0,width=1280,height=670)


        #============label frame=========================
        label_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Add Your Details",padx=2,font=("Alice",18),bg="white",fg="#615a51")
        label_frame.place(x=5,y=150,width=425,height=490)


        #=============labels & entries=====================
        # custRef
        label_cust_ref=Label(label_frame,text="Customer Reference: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(label_frame,width=22,textvariable=self.var_ref,font=("calibri",12),state="readonly")
        entry_ref.grid(row=0,column=1)

        # cust name
        label_cust_name=Label(label_frame,text="Name: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_cust_name.grid(row=1,column=0,sticky=W)

        entry_ref1=ttk.Entry(label_frame,textvariable=self.var_name,width=22,font=("calibri",12))
        entry_ref1.grid(row=1,column=1)

        #cust num
        label_cust_num=Label(label_frame,text="Mobile Number: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_cust_num.grid(row=3,column=0,sticky=W)

        entry_ref2=ttk.Entry(label_frame,textvariable=self.var_mobile_num,width=22,font=("calibri",12))
        entry_ref2.grid(row=3,column=1)

        # gender combobox
        label_gender=Label(label_frame,text="Gender: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=4,column=0,sticky=W)

        combo_gender=ttk.Combobox(label_frame,textvariable=self.var_gender,font=("Alice",12),state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1)

        # nationality combobox
        label_nation=Label(label_frame,text="Nationality: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_nation.grid(row=5,column=0,sticky=W)

        combo_nation=ttk.Combobox(label_frame,textvariable=self.var_nationality,font=("Alice",12),state="readonly")
        combo_nation["value"]=("Pakistani","Non-Pakistani","Dual Nationality")
        combo_nation.current(0)
        combo_nation.grid(row=5,column=1)

        # idproof type combo
        label_id=Label(label_frame,text="ID Proof Type: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_id.grid(row=6,column=0,sticky=W)

        combo_id=ttk.Combobox(label_frame,textvariable=self.var_idproof,font=("Alice",12),state="readonly")
        combo_id["value"]=("CNIC No.","Passport","Driving Licence")
        combo_id.current(0)
        combo_id.grid(row=6,column=1)

        # id number
        label_id_num=Label(label_frame,text="ID #: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_id_num.grid(row=7,column=0,sticky=W)

        label_id_num_txt=ttk.Entry(label_frame,textvariable=self.var_id_num,width=27,font=("calibri",12))
        label_id_num_txt.grid(row=7,column=1)

        # address
        label_address=Label(label_frame,text="Address: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_address.grid(row=8,column=0,sticky=W)

        entry_ref3=ttk.Entry(label_frame,textvariable=self.var_address,width=26,font=("calibri",12))
        entry_ref3.grid(row=8,column=1)

        # email
        label_email=Label(label_frame,text="Email: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_email.grid(row=9,column=0,sticky=W)

        entry_ref4=ttk.Entry(label_frame,textvariable=self.var_email,width=26,font=("calibri",12))
        entry_ref4.grid(row=9,column=1)

        # button frame
        btn_frame=Frame(label_frame,bd=2)
        btn_frame.place(x=0,y=400,width=412,height=40)

        # add button
        btn_add=Button(btn_frame,command=self.add_data,text="Add",font=("Alice",12,"bold"),bg="#6d412a",fg="white",width=9,cursor="hand2")
        btn_add.grid(row=0,column=0,padx=1)

        #update button
        btn_update=Button(btn_frame,text="Update",command=self.update,font=("Alice",12,"bold"),bg="#6d412a",fg="white",width=9,cursor="hand2")
        btn_update.grid(row=0,column=1,padx=1)

        #delete button
        btn_delete=Button(btn_frame,text="Delete",command=self.mDelete,font=("Alice",12,"bold"),bg="#6d412a",fg="white",width=9,cursor="hand2")
        btn_delete.grid(row=0,column=2,padx=1)

        # reset button
        btn_reset=Button(btn_frame,text="Reset",command=self.reset,font=("Alice",12,"bold"),bg="#6d412a",fg="white",width=9,cursor="hand2")
        btn_reset.grid(row=0,column=3,padx=1)

        #========= table frame ================
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",padx=2,font=("Alice",18),bg="white",fg="#615a51")
        table_frame.place(x=435,y=150,width=840,height=490)

        # searching label & combobox
        label_search_by=Label(table_frame,text="Search By: ",font=("Alice",12,"bold"))
        label_search_by.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search_by=ttk.Combobox(table_frame,textvariable=self.search_var,font=("Alice",12),state="readonly")
        combo_search_by["value"]=("Mobile No.","Passport","Driving License","CNIC","Ref")
        combo_search_by.current(0)
        combo_search_by.grid(row=0,column=1,padx=2) 

        self.txt_search=StringVar()
        label_search_by_txt=ttk.Entry(table_frame,textvariable=self.txt_search,width=24,font=("calibri",12))
        label_search_by_txt.grid(row=0,column=2,padx=2)

        # search btn
        btn_search=Button(table_frame,text="Search",command=self.search,font=("Alice",12,"bold"),bg="#6d412a",fg="white",width=9,cursor="hand2")
        btn_search.grid(row=0,column=3,padx=1)

        # show all button
        btn_show_all=Button(table_frame,text="Show All",command=self.fetch_data,font=("Alice",12,"bold"),bg="#6d412a",fg="white",width=9,cursor="hand2")
        btn_show_all.grid(row=0,column=4,padx=1)

        #====== Show Data Table===========
        details_table=LabelFrame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=840,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("Ref","Name","ID Proof","Nationality","Address","Gender","Mobile No.","ID No.","Email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Ref",text="Refer No.")
        self.Cust_Details_Table.heading("Name",text="Name")
        self.Cust_Details_Table.heading("ID Proof",text="ID Proof")
        self.Cust_Details_Table.heading("Nationality",text="Nationality")
        self.Cust_Details_Table.heading("Address",text="Address")
        self.Cust_Details_Table.heading("Gender",text="Gender")
        self.Cust_Details_Table.heading("Mobile No.",text="Mobile No.")
        self.Cust_Details_Table.heading("ID No.",text="ID No.")
        self.Cust_Details_Table.heading("Email",text="Email")

        self.Cust_Details_Table["show"]="headings"
        #self.Cust_Details_Table.pack(fill=BOTH,expand=1)

        self.Cust_Details_Table.column("Ref",width=90)
        self.Cust_Details_Table.column("Name",width=90)
        self.Cust_Details_Table.column("ID Proof",width=90)
        self.Cust_Details_Table.column("Nationality",width=90)
        self.Cust_Details_Table.column("Address",width=90)
        self.Cust_Details_Table.column("Gender",width=90)
        self.Cust_Details_Table.column("Mobile No.",width=90)
        self.Cust_Details_Table.column("ID No.",width=90)
        self.Cust_Details_Table.column("Email",width=90)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    
    def add_data(self):
        if self.var_mobile_num.get()=="" or self.var_id_num.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_ref.get(),
                                                                                self.var_name.get(),
                                                                                self.var_idproof.get(),
                                                                                self.var_nationality.get(),
                                                                                self.var_address.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_mobile_num.get(),
                                                                                self.var_id_num.get(),
                                                                                self.var_email.get()
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except  Exception   as es:
                messagebox.showwarning("Warning",f"Something went wrong.:{str(es)}",parent=self.root) 


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!= 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_idproof.set(row[2]),
        self.var_nationality.set(row[3]),
        self.var_address.set(row[4]),
        self.var_gender.set(row[5]),
        self.var_mobile_num.set(row[6]),
        self.var_id_num.set(row[7]),
        self.var_email.set(row[8])

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="AlishbaAnwar16%", database="hotel")
        my_cursor = conn.cursor()

        query = "SELECT * FROM customer WHERE `" + str(self.search_var.get()) + "` LIKE '%" + str(self.txt_search.get()) + "%'"

        my_cursor.execute(query)
        rows = my_cursor.fetchall()
        
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()

        conn.close()


    def update(self):
        if self.var_mobile_num.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="AlishbaAnwar16%", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE customer SET Name=%s, `ID Proof`=%s, Nationality=%s, Address=%s, Gender=%s, `Mobile No.`=%s, `ID No.`=%s, Email=%s WHERE Ref=%s", (
                                                                                                                                                        self.var_name.get(),
                                                                                                                                                        self.var_idproof.get(),
                                                                                                                                                        self.var_nationality.get(),
                                                                                                                                                        self.var_address.get(),
                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                        self.var_mobile_num.get(),
                                                                                                                                                        self.var_id_num.get(),
                                                                                                                                                        self.var_email.get(),
                                                                                                                                                        self.var_ref.get()
                                                                                                                                                    ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated", "Customer details have been updated successfully.", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Azure Bliss", "Do you want to delete this customer?", parent=self.root)
        if mDelete:
            conn = mysql.connector.connect(host="localhost", username="root", password="AlishbaAnwar16%", database="hotel")
            my_cursor = conn.cursor()
            query = "delete from customer where Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()

    

    def reset(self):
        #self.var_ref.set(""),
        self.var_name.set(""),
        #self.var_idproof.set(""),
        #self.var_nationality.set(""),
        self.var_address.set(""),
        #self.var_gender.set(""),
        self.var_mobile_num.set(""),
        self.var_id_num.set(""),
        self.var_email.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


if __name__ == "__main__":
    root=Tk()
    obj=customer(root)
    root.mainloop()