from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from time import strftime
from datetime import datetime
from tkinter import messagebox
from tkcalendar import Calendar

class room:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Booking")
        self.root.geometry("1295x550+0+0")

        #============== variables ===============
        self.var_id_proof=StringVar()
        self.var_id_num=StringVar()
        self.var_check_in=StringVar()
        self.var_check_out=StringVar()
        self.var_room_type=StringVar()
        self.var_available_room=StringVar()
        self.var_meal=StringVar()
        self.var_num_days=StringVar()
        self.var_paid_tax=StringVar()
        self.var_subtotal=StringVar()
        self.var_total_cost=StringVar()

        #============background image========================
        img=Image.open(r"C:\Users\HUSSAIN\OneDrive\Desktop\hotel management system\Room Booking.png")
        img=img.resize((1280,670),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        label_img=Label(self.root,image=self.photoimg,bd=0)
        label_img.place(x=0,y=0,width=1280,height=670)

        #============label frame=========================
        label_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",padx=2,font=("Alice",18),bg="white",fg="#615a51")
        label_frame.place(x=450,y=145,width=425,height=510)

        #=============labels & entries=====================
        # ID Proof
        label_id=Label(label_frame,text="ID Proof Type: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_id.grid(row=0,column=0,sticky=W)

        combo_id=ttk.Combobox(label_frame,textvariable=self.var_id_proof,font=("Alice",12),state="readonly")
        combo_id["value"]=("CNIC No.","Passport","Driving Licence","Ref No.")
        combo_id.current(0)
        combo_id.grid(row=0,column=1)

        # customer id num
        label_id_num=Label(label_frame,text="Customer ID No.: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_id_num.grid(row=1,column=0,sticky=W)

        entry_id_num=ttk.Entry(label_frame,textvariable=self.var_id_num,width=22,font=("calibri",12))
        entry_id_num.grid(row=1,column=1,sticky=W)


        #==================== BUTTON =============================
        # fetch data button
        btn_fetch=Button(label_frame,text="Fetch",command=self.fetch,font=("Alice",12,"bold"),bg="#6d412a",fg="white",width=8,cursor="hand2")
        btn_fetch.place(x=328,y=35)

        #================== ENTRIES ==============================
        #check in date
        check_in_date=Label(label_frame,text="Check-In Date: ",font=("Alice",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=2,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(label_frame,textvariable=self.var_check_in,width=22,font=("calibri",12))
        txtcheck_in_date.grid(row=2,column=1)

        check_in_button = Button(label_frame, text="Select", command=self.select_check_in_date, font=("Alice", 10), bg="#6d412a", fg="white", width=5, cursor="hand2")
        check_in_button.grid(row=2, column=2, padx=5)

        #check_out date
        check_out_date=Label(label_frame,text="Check-Out Date: ",font=("Alice",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=3,column=0,sticky=W)

        txtcheck_out_date=ttk.Entry(label_frame,textvariable=self.var_check_out,width=22,font=("calibri",12))
        txtcheck_out_date.grid(row=3,column=1)

        check_out_button = Button(label_frame, text="Select", command=self.select_check_out_date, font=("Alice", 10), bg="#6d412a", fg="white", width=5, cursor="hand2")
        check_out_button.grid(row=3, column=2, padx=5)

        #Room Type Combobox
        label_room_type=Label(label_frame,text="Room Type: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_room_type.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT `Room Type` FROM details")
        ide=my_cursor.fetchall()

        combo_room_type=ttk.Combobox(label_frame,textvariable=self.var_room_type,font=("Alice",12),state="readonly")
        combo_room_type["value"]=ide
        combo_room_type.current(0)
        combo_room_type.grid(row=4,column=1)

        # Available room
        label_available_room=Label(label_frame,text="Available Room: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_available_room.grid(row=5,column=0,sticky=W)

        #txt_available_room=ttk.Entry(label_frame,textvariable=self.var_available_room,width=22,font=("calibri",12))
        #txt_available_room.grid(row=5,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT `Room No.` FROM details")
        rows=my_cursor.fetchall()
        room_numbers=[row[0] for row in rows]
        conn.close()

        combo_room_no=ttk.Combobox(label_frame,textvariable=self.var_available_room,font=("Alice",12),state="readonly")
        combo_room_no["value"]=room_numbers
        combo_room_no.grid(row=5,column=1)

        #Meal
        label_meal=Label(label_frame,text="Meal: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_meal.grid(row=6,column=0,sticky=W)

        txt_meal=ttk.Entry(label_frame,textvariable=self.var_meal,width=22,font=("calibri",12))
        txt_meal.grid(row=6,column=1)

        #No. of days
        label_days_num=Label(label_frame,text="No. of Days: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_days_num.grid(row=7,column=0,sticky=W)

        txt_days_num=ttk.Entry(label_frame,textvariable=self.var_num_days,width=22,font=("calibri",12))
        txt_days_num.grid(row=7,column=1)

        # Paid Tax
        label_paid_tax=Label(label_frame,text="Paid Tax: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_paid_tax.grid(row=8,column=0,sticky=W)

        paid_tax=ttk.Entry(label_frame,textvariable=self.var_paid_tax,width=22,font=("calibri",12))
        paid_tax.grid(row=8,column=1)

        #Sub Total
        label_subtotal=Label(label_frame,text="Sub Total: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_subtotal.grid(row=9,column=0,sticky=W)

        subtotal=ttk.Entry(label_frame,width=22,textvariable=self.var_subtotal,font=("calibri",12))
        subtotal.grid(row=9,column=1)

        # Total Cost
        label_total_cost=Label(label_frame,text="Total Cost: ",font=("Alice",12,"bold"),padx=2,pady=6)
        label_total_cost.grid(row=11,column=0,sticky=W)

        total_cost=ttk.Entry(label_frame,width=22,textvariable=self.var_total_cost,font=("calibri",12))
        total_cost.grid(row=11,column=1,sticky=W)

        #===================== BUTTONS ========================

        # billing button
        btn_bill=Button(label_frame,text="Bill",command=self.total,font=("Alice",12,"bold"),bg="#6d412a",fg="white",width=7,cursor="hand2")
        btn_bill.place(x=330,y=385)

        # button frame
        btn_frame=Frame(label_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=440,width=412,height=40)

        # add button
        btn_add=Button(btn_frame,text="Add",command=self.add_data,font=("Alice",12,"bold"),bg="#6d412a",fg="white",width=9,cursor="hand2")
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
        table_frame=LabelFrame(self.root)
        #table_frame.place(x=435,y=150,width=620,height=90)


        #====== Show Data Table===========
        details_table=LabelFrame(table_frame,bd=2,relief=RIDGE)
        
        self.room_table=ttk.Treeview(details_table,columns=("ID Proof","ID No.","Check In","Check Out","Room Type","Available Rooms","Meal","No. Of Days","No. Of Rooms","Paid Tax","Sub Total","Total Cost"))
        

        self.room_table.heading("ID Proof",text="ID Proof")
        self.room_table.heading("ID No.",text="ID No.")
        self.room_table.heading("Check In",text="Check-In Date")
        self.room_table.heading("Check Out",text="Check-Out Date")
        self.room_table.heading("Room Type",text="Room Type")
        self.room_table.heading("Available Rooms",text="Available Rooms")
        self.room_table.heading("Meal",text="Meal")
        self.room_table.heading("No. Of Days",text="No.of Days")
        #self.room_table.heading("No. Of Rooms",text="No. of Rooms")
        self.room_table.heading("Paid Tax",text="Paid Tax")
        self.room_table.heading("Sub Total",text="Sub Total")
        self.room_table.heading("Total Cost",text="Total Cost")

        #self.Cust_Details_Table["show"]="headings"
        self.room_table.column("ID Proof")
        self.room_table.column("ID No.",)
        self.room_table.column("Check In")
        self.room_table.column("Check Out",)
        self.room_table.column("Room Type")
        self.room_table.column("Available Rooms")
        self.room_table.column("Meal")
        self.room_table.column("No. Of Days")
        #self.room_table.column("No. Of Rooms")
        self.room_table.column("Paid Tax")
        self.room_table.column("Sub Total")
        self.room_table.column("Total Cost")
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

    #================= ADD FUNCTION ===========================
    def add_data(self):
        if self.var_check_in.get()=="" or self.var_id_num.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_id_proof.get(),
                                                                                                self.var_id_num.get(),
                                                                                                self.var_check_in.get(),
                                                                                                self.var_check_out.get(),
                                                                                                self.var_room_type.get(),
                                                                                                self.var_meal.get(),
                                                                                                self.var_num_days.get(),
                                                                                                self.var_available_room.get(),
                                                                                                self.var_paid_tax.get(),
                                                                                                self.var_subtotal.get(),
                                                                                                self.var_total_cost.get()
                                                                                    ))
                conn.commit()
                #self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked!",parent=self.root)
            except  Exception   as es:
                messagebox.showwarning("Warning",f"Something went wrong.:{str(es)}",parent=self.root)


    #======================= GET CURSOR FUNCTION ==========================
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_id_proof.set(row[0])
        self.var_id_num.set(row[1])
        self.var_check_in.set(row[2])
        self.var_check_out.set(row[3])
        self.var_room_type.set(row[4])
        self.var_available_room.set(row[5])
        self.var_meal.set(row[6])
        self.var_num_days.set(row[7])
        

    #===================== UPDATE FUNCTION ===============================
    def update(self):
        if self.var_check_out.get() == "":
            messagebox.showerror("Error", "Please enter check-out date", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="AlishbaAnwar16%", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE room SET 'ID Proof'=%s, Check In =%s, Check Out=%s, Room Type=%s, `Meal`=%s, `No. Of Days`=%s, 'Available Room'=%s, 'Paid Tax'=%s, 'Sub Total'=%s, 'Total Cost'=%s WHERE `ID No.`=%s", (
                                                                                                                                                                                                                            self.var_id_proof.get(),
                                                                                                                                                                                                                            self.var_id_num.get(),
                                                                                                                                                                                                                            self.var_check_in.get(),
                                                                                                                                                                                                                            self.var_check_out.get(),
                                                                                                                                                                                                                            self.var_room_type.get(),
                                                                                                                                                                                                                            self.var_meal.get(),
                                                                                                                                                                                                                            self.var_num_days.get(),
                                                                                                                                                                                                                            self.var_available_room.get(),
                                                                                                                                                                                                                            self.var_paid_tax.get(),
                                                                                                                                                                                                                            self.var_subtotal.get(),
                                                                                                                                                                                                                            self.var_total_cost.get()
                                                                                                                                                                                                                        ))

            conn.commit()
            #self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated", "Room Booking details have been updated successfully.", parent=self.root)
    

    #=========================== DELETE FUNCTION ========================
    def mDelete(self):
        mDelete = messagebox.askyesno("Azure Bliss", "Do you want to delete this room?", parent=self.root)
        if mDelete:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="AlishbaAnwar16%", database="hotel")
                my_cursor = conn.cursor()
                query = "DELETE FROM room WHERE `ID No.`=%s"
                value = (self.var_id_num.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Room left successfully.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error leaving room: {str(e)}", parent=self.root)
        else:
            return
  
    #=============================== RESET FUNCTION ================================
    def reset(self):
        self.var_id_proof.set("")
        self.var_id_num.set("")
        self.var_check_in.set("")
        self.var_check_out.set("")
        self.var_room_type.set("")
        self.var_meal.set("")
        self.var_num_days.set("")
        self.var_available_room.set("")
        self.var_paid_tax.set("")
        self.var_subtotal.set("")
        self.var_total_cost.set("")

        
    #====================== All Data Fetch =========================
    def fetch(self):
        if self.var_id_num.get()=="":
            messagebox.showerror("Error","Please enter your CNIC/Passport/Ref No./Driving Licence.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
            my_cursor=conn.cursor()
            query2 = "SELECT Name FROM customer WHERE `ID No.` = %s"

            value=(self.var_id_num.get(),)
            my_cursor.execute(query2,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This ID no. is NOT found.",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,padx=2)
                showDataFrame.place(x=900,y=250,width=300,height=180)

                label_name=Label(showDataFrame,text="Name: ",font=("arial",12,"bold"))
                label_name.place(x=0,y=0)

                label=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                label.place(x=90,y=0)

                #=============== Gender =========================
                conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
                my_cursor=conn.cursor()
                query2 = "SELECT Gender FROM customer WHERE `ID No.` = %s"

                value=(self.var_id_num.get(),)
                my_cursor.execute(query2,value)
                row=my_cursor.fetchone()

                label_gender=Label(showDataFrame,text="Gender: ",font=("arial",12,"bold"))
                label_gender.place(x=0,y=30)

                label=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                label.place(x=90,y=30)

                #=============== Email =============================
                conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
                my_cursor=conn.cursor()
                query2 = "SELECT Email FROM customer WHERE `ID No.` = %s"

                value=(self.var_id_num.get(),)
                my_cursor.execute(query2,value)
                row=my_cursor.fetchone()

                label_email=Label(showDataFrame,text="Email: ",font=("arial",12,"bold"))
                label_email.place(x=0,y=60)

                label=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                label.place(x=90,y=60)

                #================== Nationality ====================
                conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
                my_cursor=conn.cursor()
                query2 = "SELECT Nationality FROM customer WHERE `ID No.` = %s"

                value=(self.var_id_num.get(),)
                my_cursor.execute(query2,value)
                row=my_cursor.fetchone()

                label_email=Label(showDataFrame,text="Nationality: ",font=("arial",12,"bold"))
                label_email.place(x=0,y=90)

                label=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                label.place(x=90,y=90)

                #================ Address ======================
                conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
                my_cursor=conn.cursor()
                query2 = "SELECT Address FROM customer WHERE `ID No.` = %s"

                value=(self.var_id_num.get(),)
                my_cursor.execute(query2,value)
                row=my_cursor.fetchone()

                label_address=Label(showDataFrame,text="Address: ",font=("arial",12,"bold"))
                label_address.place(x=0,y=120)

                label=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                label.place(x=90,y=120)


    def total(self):
        inDate=self.var_check_in.get()
        outDate=self.var_check_out.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_num_days.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="Breakfast" and self.var_room_type.get()=="Luxury"):
           q1=float(3000)
           q2=float(1000) 
           q3=float(self.var_num_days.get())
           q4=float(q1+q2)
           q5=float(q4+q3)
           tax="Rs. "+str("%.2f"%((q5)*0.1))
           subtol="Rs. "+str("%.2f"%((q5)))
           tol="Rs. "+str("%.2f"%(q5+((q5)*0.1)))
           self.var_paid_tax.set(tax)
           self.var_subtotal.set(subtol)
           self.var_total_cost.set(tol)

        elif(self.var_meal.get()=="Lunch" and self.var_room_type.get()=="Single"):
           q1=float(500)
           q2=float(200) 
           q3=float(self.var_num_days.get())
           q4=float(q1+q2)
           q5=float(q4+q3)
           tax="Rs. "+str("%.2f"%((q5)*0.1))
           subtol="Rs. "+str("%.2f"%((q5)))
           tol="Rs. "+str("%.2f"%(q5+((q5)*0.1)))
           self.var_paid_tax.set(tax)
           self.var_subtotal.set(subtol)
           self.var_total_cost.set(tol)

        elif(self.var_meal.get()=="Lunch" and self.var_room_type.get()=="Double"):
           q1=float(1000)
           q2=float(400) 
           q3=float(self.var_num_days.get())
           q4=float(q1+q2)
           q5=float(q4+q3)
           tax="Rs. "+str("%.2f"%((q5)*0.1))
           subtol="Rs. "+str("%.2f"%((q5)))
           tol="Rs. "+str("%.2f"%(q5+((q5)*0.1)))
           self.var_paid_tax.set(tax)
           self.var_subtotal.set(subtol)
           self.var_total_cost.set(tol)

        elif(self.var_meal.get()=="Lunch" and self.var_room_type.get()=="Luxury"):
           q1=float(1500)
           q2=float(1000) 
           q3=float(self.var_num_days.get())
           q4=float(q1+q2)
           q5=float(q4+q3)
           tax="Rs. "+str("%.2f"%((q5)*0.1))
           subtol="Rs. "+str("%.2f"%((q5)))
           tol="Rs. "+str("%.2f"%(q5+((q5)*0.1)))
           self.var_paid_tax.set(tax)
           self.var_subtotal.set(subtol)
           self.var_total_cost.set(tol)

        elif(self.var_meal.get()=="Breakfast" and self.var_room_type.get()=="Double"):
           q1=float(2500)
           q2=float(400) 
           q3=float(self.var_num_days.get())
           q4=float(q1+q2)
           q5=float(q4+q3)
           tax="Rs. "+str("%.2f"%((q5)*0.1))
           subtol="Rs. "+str("%.2f"%((q5)))
           tol="Rs. "+str("%.2f"%(q5+((q5)*0.1)))
           self.var_paid_tax.set(tax)
           self.var_subtotal.set(subtol)
           self.var_total_cost.set(tol)

        elif(self.var_meal.get()=="Dinner" and self.var_room_type.get()=="Luxury"):
           q1=float(2500)
           q2=float(1000) 
           q3=float(self.var_num_days.get())
           q4=float(q1+q2)
           q5=float(q4+q3)
           tax="Rs. "+str("%.2f"%((q5)*0.1))
           subtol="Rs. "+str("%.2f"%((q5)))
           tol="Rs. "+str("%.2f"%(q5+((q5)*0.1)))
           self.var_paid_tax.set(tax)
           self.var_subtotal.set(subtol)
           self.var_total_cost.set(tol)

        elif(self.var_meal.get()=="Dinner" and self.var_room_type.get()=="Single"):
           q1=float(2500)
           q2=float(200) 
           q3=float(self.var_num_days.get())
           q4=float(q1+q2)
           q5=float(q4+q3)
           tax="Rs. "+str("%.2f"%((q5)*0.1))
           subtol="Rs. "+str("%.2f"%((q5)))
           tol="Rs. "+str("%.2f"%(q5+((q5)*0.1)))
           self.var_paid_tax.set(tax)
           self.var_subtotal.set(subtol)
           self.var_total_cost.set(tol)

        elif(self.var_meal.get()=="Dinner" and self.var_room_type.get()=="Double"):
           q1=float(2500)
           q2=float(400) 
           q3=float(self.var_num_days.get())
           q4=float(q1+q2)
           q5=float(q4+q3)
           tax="Rs. "+str("%.2f"%((q5)*0.1))
           subtol="Rs. "+str("%.2f"%((q5)))
           tol="Rs. "+str("%.2f"%(q5+((q5)*0.1)))
           self.var_paid_tax.set(tax)
           self.var_subtotal.set(subtol)
           self.var_total_cost.set(tol)

        elif(self.var_meal.get()=="Breakfast" and self.var_room_type.get()=="Single"):
           q1=float(2500)
           q2=float(200) 
           q3=float(self.var_num_days.get())
           q4=float(q1+q2)
           q5=float(q4+q3)
           tax="Rs. "+str("%.2f"%((q5)*0.1))
           subtol="Rs. "+str("%.2f"%((q5)))
           tol="Rs. "+str("%.2f"%(q5+((q5)*0.1)))
           self.var_paid_tax.set(tax)
           self.var_subtotal.set(subtol)
           self.var_total_cost.set(tol)

    def select_check_in_date(self):
        def on_date_select():
            self.var_check_in.set(cal.get_date())
            top.destroy()

        top = Toplevel()
        cal = Calendar(top, selectmode="day", date_pattern="dd/MM/yyyy")
        cal.pack(padx=10, pady=10)
        Button(top, text="OK", command=on_date_select).pack()

    def select_check_out_date(self):
        def on_date_select():
            self.var_check_out.set(cal.get_date())
            top.destroy()

        top = Toplevel()
        cal = Calendar(top, selectmode="day", date_pattern="dd/MM/yyyy")
        cal.pack(padx=10, pady=10)
        Button(top, text="OK", command=on_date_select).pack()



if __name__ == "__main__":
    root=Tk()
    obj=room(root)
    root.mainloop()