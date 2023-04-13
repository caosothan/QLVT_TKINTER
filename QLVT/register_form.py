

# class này dung để đăng kí cho user và admin
# Thông tin user lưu trong UserDatabas và thông tin admin lưu trong AdminDatabase
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import register_or_login 

class register:
    object_register = None
    def __init__(self, object_register):
        self.object_register = object_register
        self.register_form()


    def start(self):  #Hàm khởi tạo giao diện
        self.root_reg.mainloop()

    def register_form(self):
        self.root_reg = Tk()
        self.root_reg.title("ĐĂNG KÍ")
        self.root_reg.config(background= '#0B5A81')
        self.root_reg.geometry('800x700')
        # self.master.resizable(0,0)
        f =('Times', 16)
        f1 =('Times', 14)
        f2 =('Times', 10)
        self.frame = Frame(self.root_reg, bd= 2, background= "#DDDDDD",  padx= 10, pady= 10)

        # tạo label
        self.lb_name = Label(self.frame, text = "Họ và tên", background= "#DDDDDD",font=f1)
        self.lb_email = Label(self.frame, text= "Email", background= "#DDDDDD", font= f1)
        self.lb_phone = Label(self.frame, text= "Điện thoại", background= "#DDDDDD", font= f1)
        self.lb_GT  = Label(self.frame, text= "Giới tính", background= "#DDDDDD", font= f1)
        self.lb_nation = Label(self.frame, text= "Quốc gia", background= "#DDDDDD", font= f1)
        self.username = Label(self.frame, text= "Tên đăng nhập", background=  "#DDDDDD", font= f1)
        self.password = Label(self.frame, text= "Mật khẩu", background=  "#DDDDDD", font= f1)
        self.confirmPass = Label(self.frame, text= "Xác nhận mật khẩu", background=  "#DDDDDD", font= f1)

        # tạo entry
        self.en_name = Entry(self.frame, width= 20, font= f, border= 2, background= "#FFFF66")
        self.en_email = Entry(self.frame, width= 20, font= f, border= 2, background= "#FFFF66")
        self.en_phone = Entry(self.frame, width= 20, font= f, border= 2, background= "#FFFF66")
        self.en_nation = Entry(self.frame, width= 20, font= f, border= 2, background= "#FFFF66")
        self.en_username = Entry(self.frame, width= 20, font= f, border= 2, background= "#FFFF66")
        self.en_pass = Entry(self.frame, width= 20, font= f, border= 2,background= "#FFFF66", show = "*")
        self.confirm_PW = Entry(self.frame, width= 20, font= f, border= 2, background= "#FFFF66", show = "*")

        # xử lí chọn giới tính
        self.var = StringVar()
        self.var.set("other")
        self.gebder_frame = LabelFrame(self.frame, background= "#FFFF66", padx= 10, pady= 20, border= 2)
        self.male_rb = Radiobutton(self.gebder_frame, text= "Nam", variable= self.var, value= "male", background="#FFFF66", font= f)
        self.female_rb = Radiobutton(self.gebder_frame, text= "Nữ", variable= self.var, value= "female",background="#FFFF66", font= f)
        self.other_rb = Radiobutton(self.gebder_frame, text= "Khác", variable= self.var, value= "other",background="#FFFF66", font= f)

        # xử lí chọn quốc gia qua combobox
        self.var1 = StringVar()
        self.var1.set("Chọn quốc gia")
        self.cobb = ttk.Combobox(self.frame, width= 19, font= f1)
        self.cobb.config(values= ["", "Việt Nam", "Singapore", "US", "UK", "Indonesia"], textvariable= self.var1, background= "#FFFF66")
        # tạo button đăng đăng kí
        self.register_btn = Button(self.root_reg, text= "Đăng kí", width= 62, height= 2)
        self.register_btn.config(command= self.validate, background= "#CCFF66")
        self.back_btn = Button(self.root_reg, text = "Trở lại", width= 62, height= 2)
        self.back_btn.config(command= self.turnback_from_reg, background= "#CCFF66")
        # layout cho label
        self.lb_name.grid(column= 0, row= 0, sticky= W, padx= 10, pady= 10)
        self.lb_email.grid(column= 0, row= 1, sticky= W, padx= 10, pady= 10)
        self.lb_phone.grid(column= 0, row= 2, sticky= W, padx= 10, pady= 10)
        self.lb_GT.grid(column= 0, row= 3, sticky= W, padx= 10, pady= 10)
        self.lb_nation.grid(column= 0, row= 4, sticky= W, padx =10, pady= 10)
        self.username.grid(column= 0, row= 5, sticky= W, padx= 10, pady= 10)
        self.password.grid(column= 0, row= 6, sticky= W, padx= 10, pady= 10)
        self.confirmPass.grid(column= 0, row= 7, sticky= W, padx= 10, pady= 10)
        self.frame.pack()
        self.register_btn.pack( after= self.frame, padx= 10, pady= 10) 
        self.back_btn.pack( after= self.register_btn, padx= 10, pady= 10) 
        # layout cho entry
        self.en_name.grid(column= 1, row= 0, padx= 10, pady= 10)
        self.en_email.grid(column= 1, row= 1, padx= 10, pady= 10)
        self.en_phone.grid (column= 1, row= 2, padx= 10,  pady= 10)
        self.en_username.grid(column= 1, row= 5, padx= 10, pady= 10)
        self.en_pass.grid(column= 1, row= 6, padx= 10, pady= 10 )
        self.confirm_PW.grid(column= 1, row= 7, padx= 10, pady= 10)

        self.male_rb.grid(column= 0, row= 0)
        self.female_rb.grid(column= 1, row= 0)
        self.other_rb.grid(column= 2, row= 0)
        self.gebder_frame.grid(column= 1, row= 3, padx= 10, pady= 10)
        self.cobb.grid(column= 1, row= 4, padx= 10,  pady= 10)


    def validate(self):
        if self.en_name.get() == "":
            messagebox.showwarning("Thông báo","Hãy nhập tên của bạn!")
            self.en_name.focus_set()

        elif self.en_email.get() == "":
            messagebox.showwarning("Thông báo","Hãy nhập email của bạn!")
            self.en_email.focus_set()

        elif self.en_phone.get() == "":
            messagebox.showwarning("Thông báo","Hãy nhập số điện thoại của bạn!")
            self.en_phone.focus_set()

        elif self.cobb.get() in ["", "Chọn quốc gia"]: 
            messagebox.showwarning("Thông báo","Hãy chọn quốc gia của bạn!")
            self.var1.set("Chọn quốc gia")
            self.cobb.focus_set()

        elif self.en_username.get() == "":
            messagebox.showwarning("Thông báo", "Hãy nhập tên đăng nhập của ban!")    
            self.en_username.focus_set()

        elif self.en_pass.get() == "":
            messagebox.showwarning("Thông báo", "Hãy nhập mật khẩu ủa bạn!")
            self.en_username.focus_set()

        elif self.confirm_PW.get() == "":
            messagebox.showwarning("Thông báo", "Hãy nhập lại mật khẩu của bạn để xác nhận!")        
            self.confirm_PW.focus_set()
        elif self.confirm_PW.get() != self.en_pass.get():
            messagebox.showwarning("Thông báo", "Mật khẩu xác nhận không đúng!")
            self.confirm_PW.delete(0, len(self.confirm_PW.get())) 
            self.confirm_PW.focus_set()
        else:   
            if self.duplicate_username() == False:
                if self.object_register == "user":
                    conn = sqlite3.connect("UserDatabase.db")
                    cursor = conn.cursor()
                    # count = cursor.execute("select count(ID) from User")
                    # row = count.fetchall()
                    cursor.execute("INSERT INTO User(Name, Email, Phone, GT, Nation, Username, Password, State) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
                            .format(self.en_name.get(), self.en_email.get(), self.en_phone.get(), self.var.get(), self.cobb.get()
                                    ,self.en_username.get(), self.en_pass.get(), "Hoạt động"))
                    conn.commit()
                    conn.close() 
                elif self.object_register == "admin":
                    conn = sqlite3.connect("AdminDatabase.db")
                    cursor = conn.cursor()
                    count = cursor.execute("select count(ID) from Admin")
                    row = count.fetchall()
                    cursor.execute("INSERT INTO Admin(ID, Name, Email, Phone, GT, Nation, Username, Password, State) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
                            .format(int(row[0][0])+1, self.en_name.get(), self.en_email.get(), self.en_phone.get(), self.var.get(), self.cobb.get()
                                    ,self.en_username.get(), self.en_pass.get(), "Hoạt động"))
                    conn.commit()
                    conn.close()

                messagebox.showinfo("Thông báo", "Bạn tạo tài khoản thành công!") 
            
         

    def duplicate_username(self): # hàm này để xử lí dữ liệu đăng kí trùng lặp
        if self.object_register == "user":
            conn = sqlite3.connect("UserDatabase.db")
            cursor = conn.cursor()
            cursor.execute("select Email, Phone, Username, Password from User")
            rows = cursor.fetchall()
            status = None
            for row in rows:
                if row[0] == self.en_email.get():
                    messagebox.showinfo("Thông báo", "Email tồn tại!")
                    self.en_email.focus_set()
                    status = True # True có nghĩa là có dữ liệu trùng lặp
                    break
                elif row[1] == self.en_phone.get():
                    messagebox.showinfo("Thông báo", "Số điện thoại tồn tại!")
                    self.en_phone.focus_set()
                    status = True 
                    break
                elif row[2] == self.en_username.get():
                    messagebox.showinfo("Thông báo", "Tên người dùng đã tồn tại!")
                    self.en_username.focus_set()
                    status = True
                    break
                elif row[3] == self.en_pass.get():
                    messagebox.showinfo("Thông báo", "Tên mật khẩu đã tồn tại!")
                    self.en_pass.focus_set()
                    status = True
                    break
                else:
                    status = False
            conn.commit()
            conn.close()
            return status

        elif self.object_register == "admin":
            conn = sqlite3.connect("AdminDatabase.db")
            cursor = conn.cursor()
            cursor.execute("select Email, Phone, Username, Password from Admin")
            rows = cursor.fetchall()
            status = None
            for row in rows:
                if row[0] == self.en_email.get():
                    messagebox.showinfo("Thông báo", "Email tồn tại!")
                    self.en_email.focus_set()
                    status = True # True có nghĩa là có dữ liệu trùng lặp
                    break
                elif row[1] == self.en_phone.get():
                    messagebox.showinfo("Thông báo", "Số điện thoại tồn tại!")
                    self.en_phone.focus_set()
                    status = True 
                    break
                elif row[2] == self.en_username.get():
                    messagebox.showinfo("Thông báo", "Tên người dùng đã tồn tại!")
                    self.en_username.focus_set()
                    status = True
                    break
                elif row[3] == self.en_pass.get():
                    messagebox.showinfo("Thông báo", "Tên mật khẩu đã tồn tại!")
                    self.en_pass.focus_set()
                    status = True
                    break
                else:
                    status = False
            conn.commit()
            conn.close()
            return status       

                






    def turnback_from_reg(self):
        self.root_reg.destroy()
        obj = register_or_login.reg_or_log(self.object_register, self.object_register)
        obj.start()
        




