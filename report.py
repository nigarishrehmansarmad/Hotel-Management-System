from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from tkcalendar import Calendar

class report:
    def __init__(self,root):
        self.root=root
        self.root.title("Report")
        self.root.geometry("1550x800+0+0")

        #============variable=============================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name=StringVar()
        self.var_mobile_num=StringVar()
        self.var_gender=StringVar()
        self.var_idproof=StringVar()
        self.var_id_num=StringVar()
        self.var_email=StringVar()
        self.var_sal=StringVar()
        self.var_rank=StringVar()
        self.var_attendance=StringVar()
        self.var_date=StringVar()

        #============background image========================
        img=Image.open(r"C:\Users\HUSSAIN\OneDrive\Desktop\hotel management system\employee details.png")
        img=img.resize((1280,670),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        label_img=Label(self.root,image=self.photoimg,bd=0)
        label_img.place(x=0,y=0,width=1280,height=670)

        #============label frame=========================
        label_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Add Employee Details",padx=2,font=("Alice",18),bg="white",fg="#355f55")
        label_frame.place(x=5,y=150,width=425,height=500)

        #=============labels & entries=====================
        # Employee Ref
        label_cust_ref=Label(label_frame,text="Employee Reference: ",font=("Alice",12,"bold"),padx=2,pady=6,bg="white",fg="#355f55")
        label_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(label_frame,width=22,textvariable=self.var_ref,font=("calibri",12),state="readonly")
        entry_ref.grid(row=0,column=1)

        # Employee name
        label_cust_name=Label(label_frame,text="Name: ",font=("Alice",12,"bold"),padx=2,pady=6,bg="white",fg="#355f55")
        label_cust_name.grid(row=1,column=0,sticky=W)

        entry_ref1=ttk.Entry(label_frame,textvariable=self.var_name,width=22,font=("calibri",12))
        entry_ref1.grid(row=1,column=1)

        #Employee num
        label_cust_num=Label(label_frame,text="Mobile Number: ",font=("Alice",12,"bold"),padx=2,pady=6,bg="white",fg="#355f55")
        label_cust_num.grid(row=3,column=0,sticky=W)

        entry_ref2=ttk.Entry(label_frame,textvariable=self.var_mobile_num,width=22,font=("calibri",12))
        entry_ref2.grid(row=3,column=1)

        # gender combobox
        label_gender=Label(label_frame,text="Gender: ",font=("Alice",12,"bold"),padx=2,pady=6,bg="white",fg="#355f55")
        label_gender.grid(row=4,column=0,sticky=W)

        combo_gender=ttk.Combobox(label_frame,font=("Alice",12),state="readonly",textvariable=self.var_gender)
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1)

        # idproof type combo
        label_id=Label(label_frame,text="ID Proof Type: ",font=("Alice",12,"bold"),padx=2,pady=6,bg="white",fg="#355f55")
        label_id.grid(row=6,column=0,sticky=W)

        combo_id=ttk.Combobox(label_frame,font=("Alice",12),state="readonly",textvariable=self.var_idproof)
        combo_id["value"]=("CNIC No.","Passport","Driving Licence")
        combo_id.current(0)
        combo_id.grid(row=6,column=1)

        # id number
        label_id_num=Label(label_frame,text="ID #: ",font=("Alice",12,"bold"),padx=2,pady=6,bg="white",fg="#355f55")
        label_id_num.grid(row=7,column=0,sticky=W)

        label_id_num_txt=ttk.Entry(label_frame,width=27,font=("calibri",12),textvariable=self.var_id_num)
        label_id_num_txt.grid(row=7,column=1)

        # email
        label_email=Label(label_frame,text="Email: ",font=("Alice",12,"bold"),padx=2,pady=6,bg="white",fg="#355f55")
        label_email.grid(row=8,column=0,sticky=W)

        entry_ref4=ttk.Entry(label_frame,width=26,font=("calibri",12),textvariable=self.var_email)
        entry_ref4.grid(row=8,column=1)

        # salary
        label_sal=Label(label_frame,text="Salary: ",font=("Alice",12,"bold"),padx=2,pady=6,bg="white",fg="#355f55")
        label_sal.grid(row=9,column=0,sticky=W)

        entry_ref5=ttk.Entry(label_frame,width=26,font=("calibri",12),textvariable=self.var_sal)
        entry_ref5.grid(row=9,column=1)

        # rank
        label_rank=Label(label_frame,text="Rank: ",font=("Alice",12,"bold"),padx=2,pady=6,bg="white",fg="#355f55")
        label_rank.grid(row=10,column=0,sticky=W)

        entry_ref6=ttk.Entry(label_frame,width=26,font=("calibri",12),textvariable=self.var_rank)
        entry_ref6.grid(row=10,column=1)

        # attendance combobox
        label_attendance=Label(label_frame,text="Attendance: ",font=("Alice",12,"bold"),padx=2,pady=6,bg="white",fg="#355f55")
        label_attendance.grid(row=11,column=0,sticky=W)

        combo_gender=ttk.Combobox(label_frame,font=("Alice",12),state="readonly",textvariable=self.var_attendance)
        combo_gender["value"]=("Present","Absent")
        combo_gender.current(0)
        combo_gender.grid(row=11,column=1)

        #date
        date=Label(label_frame,text="Date: ",font=("Alice",12,"bold"),padx=2,pady=6,bg="white",fg="#355f55")
        date.grid(row=12,column=0,sticky=W)

        txt_date=ttk.Entry(label_frame,width=18,font=("calibri",12),textvariable=self.var_date)
        txt_date.grid(row=12,column=1,sticky=W)

        date_button = Button(label_frame, text="Select",command=self.select_date,font=("Alice", 10),fg="white",bg="#355f55", width=5, cursor="hand2")
        date_button.grid(row=13,column=1)

        # button frame
        btn_frame=Frame(label_frame,bd=2)
        btn_frame.place(x=0,y=430,width=412,height=40)

        # add button
        btn_add=Button(btn_frame,text="Add",font=("Alice",12,"bold"),command=self.add_data,fg="white",bg="#355f55",width=9,cursor="hand2")
        btn_add.grid(row=0,column=0,padx=1)

        #update button
        btn_update=Button(btn_frame,text="Update",font=("Alice",12,"bold"),command=self.update,fg="white",bg="#355f55",width=9,cursor="hand2")
        btn_update.grid(row=0,column=1,padx=1)

        #delete button
        btn_delete=Button(btn_frame,text="Delete",font=("Alice",12,"bold"),command=self.mDelete,fg="white",bg="#355f55",width=9,cursor="hand2")
        btn_delete.grid(row=0,column=2,padx=1)

        # reset button
        btn_reset=Button(btn_frame,text="Reset",font=("Alice",12,"bold"),command=self.reset,fg="white",bg="#355f55",width=9,cursor="hand2")
        btn_reset.grid(row=0,column=3,padx=1)

        #========= table frame ================
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",padx=2,font=("Alice",18),bg="white",fg="#355f55")
        table_frame.place(x=435,y=150,width=840,height=490)

        # searching label & combobox
        label_search_by=Label(table_frame,text="Search By: ",font=("Alice",12,"bold"))
        label_search_by.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search_by=ttk.Combobox(table_frame,textvariable=self.search_var,font=("Alice",12),state="readonly")
        combo_search_by["value"]=("Passport","Driving License","CNIC","Ref")
        combo_search_by.current(0)
        combo_search_by.grid(row=0,column=1,padx=2) 

        self.txt_search=StringVar()
        label_search_by_txt=ttk.Entry(table_frame,textvariable=self.txt_search,width=24,font=("calibri",12))
        label_search_by_txt.grid(row=0,column=2,padx=2)

        # search btn
        btn_search=Button(table_frame,text="Search",font=("Alice",12,"bold"),command=self.search,fg="white",bg="#355f55",width=9,cursor="hand2")
        btn_search.grid(row=0,column=3,padx=1)

        # show all button
        btn_show_all=Button(table_frame,text="Show All",font=("Alice",12,"bold"),command=self.fetch_data,fg="white",bg="#355f55",width=9,cursor="hand2")
        btn_show_all.grid(row=0,column=4,padx=1)

        #====== Show Data Table===========
        details_table=LabelFrame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=840,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Employee_Details_Table=ttk.Treeview(details_table,columns=("Ref","Name","Mobile No","Gender","ID Proof","ID No","Email","Salary","Rank","Attendance","Date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Employee_Details_Table.xview)
        scroll_y.config(command=self.Employee_Details_Table.yview)

        self.Employee_Details_Table.heading("Ref",text="Refer No.")
        self.Employee_Details_Table.heading("Name",text="Name")
        self.Employee_Details_Table.heading("Mobile No", text="Mobile No.")
        self.Employee_Details_Table.heading("Gender",text="Gender")
        self.Employee_Details_Table.heading("ID Proof",text="ID Proof")
        self.Employee_Details_Table.heading("ID No",text="ID No.")
        self.Employee_Details_Table.heading("Email",text="Email")
        self.Employee_Details_Table.heading("Salary",text="Salary")
        self.Employee_Details_Table.heading("Rank",text="Rank")
        self.Employee_Details_Table.heading("Attendance",text="Attendance")
        self.Employee_Details_Table.heading("Date",text="Date")

        self.Employee_Details_Table["show"]="headings"
        #self.Employee_Details_Table.pack(fill=BOTH,expand=1)

        self.Employee_Details_Table.column("Ref",width=90)
        self.Employee_Details_Table.column("Name",width=90)
        self.Employee_Details_Table.column("Mobile No",width=90)
        self.Employee_Details_Table.column("Gender",width=90)
        self.Employee_Details_Table.column("ID Proof",width=90)
        self.Employee_Details_Table.column("ID No",width=90)
        self.Employee_Details_Table.column("Email",width=90)
        self.Employee_Details_Table.column("Salary",width=90)
        self.Employee_Details_Table.column("Rank",width=90)    
        self.Employee_Details_Table.column("Attendance",width=90)
        self.Employee_Details_Table.column("Date",width=90)

        self.Employee_Details_Table.pack(fill=BOTH,expand=1)
        self.Employee_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    
    def add_data(self):
        if self.var_mobile_num.get()=="" or self.var_id_num.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into report values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_ref.get(),
                                                                                                self.var_name.get(),
                                                                                                self.var_mobile_num.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_idproof.get(),
                                                                                                self.var_id_num.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_sal.get(),
                                                                                                self.var_rank.get(),
                                                                                                self.var_attendance.get(),
                                                                                                self.var_date.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee has been added",parent=self.root)
            except  Exception   as es:
                messagebox.showwarning("Warning",f"Something went wrong.:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from report")
        rows=my_cursor.fetchall()
        if len(rows)!= 0:
            self.Employee_Details_Table.delete(*self.Employee_Details_Table.get_children())
            for i in rows:
                self.Employee_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Employee_Details_Table.focus()
        content=self.Employee_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_name.set(row[1])
        self.var_mobile_num.set(row[2])
        self.var_gender.set(row[3])
        self.var_idproof.set(row[4])
        self.var_id_num.set(row[5])
        self.var_email.set(row[6])
        self.var_sal.set(row[7])
        self.var_rank.set(row[8])
        self.var_attendance.set(row[9])
        self.var_date.set(row[10])

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="AlishbaAnwar16%", database="hotel")
        my_cursor = conn.cursor()

        query = "SELECT * FROM report WHERE `" + str(self.search_var.get()) + "` LIKE '%" + str(self.txt_search.get()) + "%'"

        my_cursor.execute(query)
        rows = my_cursor.fetchall()
        
        if len(rows) != 0:
            self.Employee_Details_Table.delete(*self.Employee_Details_Table.get_children())
            for i in rows:
                self.Employee_Details_Table.insert("", END, values=i)
            conn.commit()

        conn.close()

    #===================== UPDATE FUNCTION ===============================
    def update(self):
        if self.var_date.get() == "":
            messagebox.showerror("Error", "Please enter today's date", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="AlishbaAnwar16%", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE report SET Name=%s, No=%s, Gender=%s, `ID Proof`=%s, `ID No`=%s, Email=%s, Salary=%s, `Rank`=%s, Attendance=%s, Date=%s WHERE `Ref`=%s", (
                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                self.var_mobile_num.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_idproof.get(),
                                                                                                                                                                                                self.var_id_num.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_sal.get(),
                                                                                                                                                                                                self.var_rank.get(),
                                                                                                                                                                                                self.var_attendance.get(),
                                                                                                                                                                                                self.var_date.get(),
                                                                                                                                                                                                self.var_ref.get()         
                                                                                                                                                                                            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated", "Employee details have been updated successfully.", parent=self.root)



    def mDelete(self):
        mDelete = messagebox.askyesno("Azure Bliss", "Do you want to delete this employee?", parent=self.root)
        if mDelete:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="AlishbaAnwar16%", database="hotel")
                my_cursor = conn.cursor()
                query = "DELETE FROM report WHERE `Ref`=%s"
                value = (self.var_ref.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Employee deleted successfully.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting employee: {str(e)}", parent=self.root)
        else:
            return
    
    def reset(self):
        self.var_ref.set("")
        self.var_name.set("")
        self.var_mobile_num.set("")
        self.var_gender.set("")
        self.var_idproof.set("")
        self.var_id_num.set("")
        self.var_email.set("")
        self.var_sal.set("")
        self.var_rank.set("")
        self.var_attendance.set("")
        self.var_date.set("")

    def select_date(self):
        def on_date_select():
            self.var_date.set(cal.get_date())
            top.destroy()

        top = Toplevel()
        cal = Calendar(top, selectmode="day", date_pattern="dd/MM/yyyy")
        cal.pack(padx=10, pady=10)
        Button(top, text="OK", command=on_date_select).pack()


if __name__ == "__main__":
    root=Tk()
    obj=report(root)
    root.mainloop()

