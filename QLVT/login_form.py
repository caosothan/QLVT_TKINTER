
#class dùng để tạo form đăng nhập dùng cả cho user và admin

from tkinter import*
from tkinter import messagebox
import sqlite3
import register_or_login 
from  process import process
import admin

class login:
    object_login = None
    root_login = None
    def __init__(self, object_login):
        self.object_login = object_login
        self.login_form()

    
    def start(self):
        self.root_login.mainloop()
        
    def login_form(self):
        self.root_login= Tk()
        self.root_login.title("ĐĂNG NHẬP")
        self.root_login.resizable(0,0)
        self.root_login.geometry("600x300")
        self.root_login.config(background= "#0B5A81")
        frame = Frame(self.root_login, background= "#0B5A81")
        lb_username = Label(frame, text= "Username", width = 20,background= "#0B5A81" , font= ("Times", 14))
        lb_password = Label(frame, text= "Password", width = 20, background= "#0B5A81" ,font= ("Times", 14))
        self.var_username_login  =StringVar()
        self.var_password_login = StringVar()
        self.en_username_login = Entry(frame, font= ("Times", 18), border= 2)
        self.en_password_login = Entry(frame, font= ("Times", 18), border= 2, show = "*")
        back_btn = Button(frame, text= "Trở lại", background= "brown", width= 30, height= 1, command= self.turnback_from_login )
        btn_login = Button(frame, text= "Đăng nhập", background= "brown", width= 30, height= 1, command= self.validate)
        lb_username.grid(column= 0, row= 0, sticky=W, padx= 10,  pady= 20)
        lb_password.grid(column= 0, row= 1, sticky= W, padx =10, pady= 20)
        self.en_username_login.grid(column= 1, row= 0, pady  =20)
        self.en_password_login.grid(column= 1, row= 1, pady= 20)
        btn_login.grid(column= 1, row= 2, pady= 20)
        back_btn.grid(column= 1, row= 3, pady= 20)
        frame.pack()
    
   
    def validate(self):
        rows = []
        name = self.en_username_login.get()
        pw = self.en_password_login.get() 
        if name =="":
            messagebox.showinfo("Thông báo", "Bạn cần nhập tên người dùng!")
            self.en_username_login.focus_set()
        elif pw == "": 
            messagebox.showinfo("Thông báo", "Bạn cần nhập mật khẩu!")
            self.en_password_login.focus_set()
        else:
            
            if self.object_login == "user":
                conn = sqlite3.connect("UserDatabase.db")
                cursor = conn.cursor()
                cursor.execute("select Username, Password, State from User")
                rows = cursor.fetchall()
                conn.commit()
                conn.close()
            elif self.object_login == "admin":
                conn = sqlite3.connect("AdminDatabase.db")
                cursor = conn.cursor()
                cursor.execute("select Username, Password, State from Admin")
                rows = cursor.fetchall()
                conn.commit()
                conn.close()
                
            state = None
            for row in rows:
                if row[0] == name and row[1] == pw:
                    if row[2] == "Hoạt động":
                        state = 1
                        break
                    elif row[2] == "Khóa":
                        state = 0
                        break
                else:
                    state = -1  

            if state == 1:
                messagebox.showinfo("Thông báo", "Bạn đã đăng nhập thành công!")
                if self.root_login != None:
                    self.root_login.destroy()
                if self.object_login == "user":
                    user = process()
                    user.root_process.title("QUẢN LÍ VẬT TƯ - tên người dùng: '{}' đang đăng nhập".format(name))
                    user.start()
                elif self.object_login == "admin":
                    ad = admin.UserData() #Admin đăng nhập để xử lí dữ liệu người dùng
                    ad.master.title("ADMIN - Admin: '{}' đang đăng nhập".format(name))
                    ad.start()
                
            elif state == 0:
                messagebox.showinfo("Thông báo", "Tài khoản này bị khóa!")

            elif state == -1:
                messagebox.showwarning("Thông báo", "Tên người dùng hoặc tên người dùng không đúng!") 

           
            

                

    def turnback_from_login(self):
        self.root_login.destroy()
        obj = register_or_login.reg_or_log(self.object_login, self.object_login)
        obj.start()





