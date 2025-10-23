from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import Calendar
import mysql.connector
from hotel import hms


def main():
     win=Tk()
     app=login(win)
     win.mainloop()

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        img1=Image.open(r"C:\Users\HUSSAIN\OneDrive\Desktop\hotel management system\Login.png")
        img1=img1.resize((1280,670),Image.LANCZOS)
        self.photoimg1= ImageTk.PhotoImage(img1)
        label_img=Label(self.root,image=self.photoimg1,bd=0)
        label_img.place(x=0,y=0,width=1280,height=670)

        frame = Frame(self.root,bg="#384c89")
        frame.place(x=490,y=170,width=340,height=400)

        #img2=Image.open(r"C:\Users\HUSSAIN\OneDrive\Desktop\hotel management system\hotel images\LoginIconAppl.png")
        #img2=img2.resize((100,100),Image.LANCZOS)
        #self.photoimg2=ImageTk.PhotoImage(img2)
        #label_img2=Label(frame,image=self.photoimg2,bg="#384c89",borderwidth=0)
        #label_img2.place(x=600,y=80,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("Century Gothic",19),fg="white",bg="#384c89")
        get_str.place(x=95,y=30)

        #====================  LABELS =======================
        # USERNAME LABEL
        username_lbl=Label(frame,text="Username: ",font=("Bell MT",15),fg="white",bg="#384c89")
        username_lbl.place(x=2,y=100)

        self.txtuser=ttk.Entry(frame,font=("Bell MT",15),foreground="black",background="white")
        self.txtuser.place(x=100,y=100)

        # PASSWORD LABEL
        password_lbl=Label(frame,text="Password: ",font=("Bell MT",15),fg="white",bg="#384c89")
        password_lbl.place(x=2,y=150)

        self.txtpass=ttk.Entry(frame,font=("Bell MT",15),foreground="black",background="white")
        self.txtpass.place(x=100,y=150)

        # LOGIN BUTTON
        login_btn=Button(frame,text="Login",command=self.login,font=("Century Gothic",18,"bold"),fg="white",bg="red",activebackground="red",activeforeground="white")
        login_btn.place(x=100,y=200,width=150,height=50)

        # REGISTER BUTTON
        reg_btn=Button(frame,text="Register",font=("Century Gothic",15,"bold"),command=self.register_window,fg="white",bg="#384c89",activebackground="#384c89",activeforeground="white",border=0)
        reg_btn.place(x=5,y=300,width=150,height=50)
 
        # FORGOT PASSWORD BUTTON
        pass_btn=Button(frame,text="Forgot Password",command=self.forgot_password,font=("Century Gothic",13,"bold"),fg="white",bg="#384c89",activebackground="#384c89",activeforeground="white",border=0)
        pass_btn.place(x=185,y=300,width=150,height=50)

    def register_window(self):
         self.new_window=Toplevel(self.root)
         self.app=register(self.new_window)
         

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txtuser.get()=="nigarish" and self.txtpass.get()=="1234":
            messagebox.showinfo("Success","Welcome to Azure Bliss!")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE Email=%s and Password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                     ))
            row=my_cursor.fetchone()
            if row == None:
                 messagebox.showerror("Error","Invalid Username & Password")
            else:
                 open_main=messagebox.askyesno("Yes/No","Access only admin")
                 if open_main>0:
                      self.new_window=Toplevel(self.root)
                      self.app=hms(self.new_window)

                 else:
                      if not open_main:
                           return
            conn.commit()
            conn.close()

    def reset_password(self):
         if self.combo_secq.get()=="Select":
              messagebox.showerror("Error","Select security question.",parent=self.root2)
         elif self.txt_sec_ans.get()=="":
               messagebox.showerror("Error","Please enter security answer",parent=self.root2)
         elif self.txt_newpass.get()=="":
              messagebox.showerror("Error","Enter new password.",parent=self.root2)
         else:
              conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
              my_cursor=conn.cursor()
              query=("SELECT * FROM register WHERE Email=%s and SecQ=%s and SecAns=%s")
              value=(self.txtuser.get(),self.combo_secq.get(),self.txt_sec_ans.get())
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              if row == None:
                   messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
              else:
                   query=("UPDATE register SET Password=%s and CPassword=%s WHERE Email=%s")
                   value=(self.txt_newpass.get(),self.txt_newpass.get(),self.txtuser.get())
                   my_cursor.execute(query,value)

                   conn.commit()
                   conn.close()
                   messagebox.showinfo("Info","Your Password has been reset, Please login with new password.",parent=self.root2)
                   self.root2.destroy()
                  

    def forgot_password(self):
          if self.txtuser.get()=="":
              messagebox.showerror("Error","Please enter the Email Address to reset password.")
          else:
              conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
              my_cursor=conn.cursor()
              query=("SELECT * FROM register WHERE Email=%s")
              value=(self.txtuser.get(),)
              my_cursor.execute(query,value)
              row=my_cursor.fetchone()
              #print(row)

              if row == None:
                   messagebox.showerror("Error","Please enter the valid username.")
              else:
                   conn.close()
                   self.root2=Toplevel()
                   self.root2.title("Forgot Password")
                   self.root2.geometry("340x450+610+170")

                   l=Label(self.root2,text="Forgot password",font=("times new roman",20,"bold"),fg="black",bg="white")
                   l.place(x=0,y=10,relwidth=1)
                   
                   #SECURITY QUESTION
                   secq_label=Label(self.root2,text="Security Question: ",font=("Century Gothic",13),fg="#545454",bg="white")
                   secq_label.place(x=50,y=80)
                   self.combo_secq=ttk.Combobox(self.root2,font=("Calibri",15),state="readonly")
                   self.combo_secq["value"]=("Select","Your Birth Place","Your Mother's Maiden name","Your pet name","Childhood's best friend name")
                   self.combo_secq.current(0)
                   self.combo_secq.place(x=50,y=110,width=250)

                    # Security Answer
                   sec_ans_label=Label(self.root2,text="Security Answer: ",font=("Century Gothic",13),fg="#545454",bg="white")
                   sec_ans_label.place(x=50,y=150)
                   self.txt_sec_ans=ttk.Entry(self.root2,font=("Calibri",15),foreground="black",background="white")
                   self.txt_sec_ans.place(x=50,y=180,width=250)

                   new_pass=Label(self.root2,text="New Password: ",font=("Century Gothic",13),fg="#545454",bg="white")
                   new_pass.place(x=50,y=220)
                   self.txt_newpass=ttk.Entry(self.root2,font=("Calibri",15),foreground="black",background="white")
                   self.txt_newpass.place(x=50,y=250,width=250)

                   btn=Button(self.root2,text="Reset",fg="white",command=self.reset_password,bg="#384c89",font=("Century Gothic",15,"bold"))
                   btn.place(x=100,y=290)







class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # =========== VARIABLES ==========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_mob_num=StringVar()
        self.var_email=StringVar()
        self.var_secq=StringVar()
        self.var_sec_ans=StringVar()
        self.var_nation=StringVar()
        #self.var_dob=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_cnic=StringVar()
        self.var_passport=StringVar()

        img1=Image.open(r"C:\Users\HUSSAIN\OneDrive\Desktop\hotel management system\register.png")
        img1=img1.resize((1280,670),Image.LANCZOS)
        self.photoimg1= ImageTk.PhotoImage(img1)
        label_img=Label(self.root,image=self.photoimg1,bd=0)
        label_img.place(x=0,y=0,width=1280,height=670)

        img2=Image.open(r"C:\Users\HUSSAIN\OneDrive\Desktop\hotel management system\register_pg.png")
        img2=img2.resize((400,520),Image.LANCZOS)
        self.photoimg2= ImageTk.PhotoImage(img2)
        label_img2=Label(self.root,image=self.photoimg2,bd=0)
        label_img2.place(x=50,y=100,width=400,height=520)


        #========== MAIN FRAME =============
        frame=Frame(self.root,bg="white")
        frame.place(x=450,y=100,width=790,height=520)

        reg_label=Label(frame,text="Register Here",font=("Copperplate Gothic Light",25),fg="#545454",bg="white")
        reg_label.place(x=250,y=10)

        #========== label and entry ==============

        # FIRST NAME -- ROW1
        fname_label=Label(frame,text="First Name: ",font=("Century Gothic",15),fg="#545454",bg="white")
        fname_label.place(x=5,y=100)

        self.txt_fname=ttk.Entry(frame,font=("Calibri",15),textvariable=self.var_fname,foreground="black",background="white")
        self.txt_fname.place(x=120,y=100)

        # LAST NAME -- ROW1
        lname_label=Label(frame,text="Last Name: ",font=("Century Gothic",15),fg="#545454",bg="white")
        lname_label.place(x=350,y=100)

        self.txt_lname=ttk.Entry(frame,font=("Calibri",15),textvariable=self.var_lname,foreground="black",background="white")
        self.txt_lname.place(x=470,y=100)

        # Phone Num -- ROW2
        ph_label=Label(frame,text="Mobile No.: ",font=("Century Gothic",15),fg="#545454",bg="white")
        ph_label.place(x=5,y=150)

        self.txt_ph=ttk.Entry(frame,font=("Calibri",15),textvariable=self.var_mob_num,foreground="black",background="white")
        self.txt_ph.place(x=120,y=150)
        # Email -- ROW2
        email_label=Label(frame,text="Email: ",font=("Century Gothic",15),fg="#545454",bg="white")
        email_label.place(x=400,y=150)

        self.txt_email=ttk.Entry(frame,font=("Calibri",15),textvariable=self.var_email,foreground="black",background="white")
        self.txt_email.place(x=470,y=150)

        # CNIC -- ROW3
        cnic_label=Label(frame,text="CNIC: ",font=("Century Gothic",15),fg="#545454",bg="white")
        cnic_label.place(x=50,y=200)
        self.txt_cnic=ttk.Entry(frame,font=("Calibri",15),textvariable=self.var_cnic,foreground="black",background="white")
        self.txt_cnic.place(x=120,y=200)

        # Passport -- ROW3
        passport_label=Label(frame,text="Passport No.: ",font=("Century Gothic",15),fg="#545454",bg="white")
        passport_label.place(x=340,y=200)
        self.txt_passport=ttk.Entry(frame,font=("Calibri",15),textvariable=self.var_passport,foreground="black",background="white")
        self.txt_passport.place(x=470,y=200)

        # Nationality -- ROW4
        nation_label=Label(frame,text="Nationality: ",font=("Century Gothic",15),fg="#545454",bg="white")
        nation_label.place(x=0,y=250)
        self.combo_nation=ttk.Combobox(frame,font=("Calibri",15),state="readonly",textvariable=self.var_nation)
        self.combo_nation["value"]=("Pakistani","Non-Pakistani","Dual Nationality")
        self.combo_nation.current(0)
        self.combo_nation.place(x=120,y=250)

        # Security Question -- ROW 4
        secq_label=Label(frame,text="Security Question: ",font=("Century Gothic",13),fg="#545454",bg="white")
        secq_label.place(x=350,y=250)
        self.combo_secq=ttk.Combobox(frame,font=("Calibri",15),state="readonly",textvariable=self.var_secq)
        self.combo_secq["value"]=("Select","Your Birth Place","Your Mother's Maiden name","Your pet name","Childhood's best friend name")
        self.combo_secq.current(0)
        self.combo_secq.place(x=510,y=250)

        # Security Answer -- ROW 5
        sec_ans_label=Label(frame,text="Security Answer: ",font=("Century Gothic",13),fg="#545454",bg="white")
        sec_ans_label.place(x=0,y=300)
        self.txt_sec_ans=ttk.Entry(frame,textvariable=self.var_sec_ans,font=("Calibri",15),foreground="black",background="white")
        self.txt_sec_ans.place(x=140,y=300)

        #================= DOB -- ROW 5 =================
        dob_label=Label(frame,text="D.O.B: ",font=("Century Gothic",15),fg="#545454",bg="white")
        dob_label.place(x=400,y=300)
        self.txt_dob = StringVar()
        self.txt_dob_entry = ttk.Entry(frame, textvariable=self.txt_dob, font=("Calibri", 15), foreground="black", background="white")
        self.txt_dob_entry.place(x=470, y=300)

        # Calendar widget for selecting date
        self.calendar = Calendar(frame, selectmode="day", date_pattern="dd/MM/yyyy",background="#f4e2da", foreground="#545454")
        self.calendar.place(x=510, y=330)

        # Bind a function to retrieve the selected date
        self.calendar.bind("<<CalendarSelected>>", self.get_selected_dob)

        # ========= PASSWORD -- ROW 6 =============
        pass_label=Label(frame,text="Password: ",font=("Century Gothic",15),fg="#545454",bg="white")
        pass_label.place(x=0,y=350)
        self.txt_pass=ttk.Entry(frame,font=("Calibri",15),foreground="black",background="white",textvariable=self.var_pass)
        self.txt_pass.place(x=140,y=350)

        # ======== CONFIRM PASSWORD -- ROW 7 ==========
        confirm_pass_label=Label(frame,text="Confirm Password: ",font=("Century Gothic",13),fg="#545454",bg="white")
        confirm_pass_label.place(x=0,y=400)
        self.txt_confirm_pass=ttk.Entry(frame,font=("Calibri",15),foreground="black",background="white",textvariable=self.var_confpass)
        self.txt_confirm_pass.place(x=160,y=400)

        # CHECK BUTTON
        self.var_check=IntVar()
        self.check_btn=Checkbutton(frame,variable=self.var_check,text="I agree to terms and condition.",font=("Century Gothic",13,"bold"),fg="#545454",bg="white",onvalue=1,offvalue=0)
        self.check_btn.place(x=5,y=450)

        # ============ BUTTONS =============
        self.btn_reg=Button(frame,text="Register Now",command=self.register_data,font=("Century Gothic",13,"bold"),fg="#545454",bg="#f4e2da",cursor="hand2")
        self.btn_reg.place(x=330,y=480)

        self.btn_login=Button(frame,text="Login Now",font=("Century Gothic",13,"bold"),fg="#545454",bg="#f4e2da",cursor="hand2")
        self.btn_login.place(x=100,y=480)

    # =============== FUNCTION DECLARATION =================

    def get_selected_dob(self, event=None):
        # Retrieve the selected date from the Calendar widget and update the entry field
        txt_dob = self.calendar.get_date()
        self.txt_dob.set(txt_dob)


    def register_data(self):
            if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_secq.get()=="Select" or self.txt_dob.get()=="":
                 messagebox.showerror("Error","All fields are required.")
            elif self.var_pass.get()!=self.var_confpass.get():
                 messagebox.showerror("Error","The password you entered do not match.")
            elif self.var_check.get()==0:
                 messagebox.showerror("Error","Make sure you tick the box.")
            elif self.var_cnic.get()=="" and self.var_passport.get()=="":
                 messagebox.showerror("Error","Either enter both CNIC Number and Passport Number or any one of them.")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="AlishbaAnwar16%",database="hotel")
                my_cursor=conn.cursor()
                query=("SELECT * FROM register WHERE Email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row != None:
                     messagebox.showerror("Error","User already exist, please try another email.")
                else:
                     my_cursor.execute("INSERT INTO register values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_fname.get(),
                                                                                                            self.var_lname.get(),
                                                                                                            self.var_mob_num.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_cnic.get(),
                                                                                                            self.var_passport.get(),
                                                                                                            self.var_nation.get(),
                                                                                                            self.var_secq.get(),
                                                                                                            self.var_sec_ans.get(),
                                                                                                            self.txt_dob.get(),
                                                                                                            self.var_pass.get(),
                                                                                                            self.var_confpass.get()
                                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered successfully!!")


if __name__ == "__main__":
    main()


       #messagebox.showinfo("Success","Welcome to Azure Bliss!")
        #else: