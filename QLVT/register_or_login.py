

# Class tạo cửa sổ xác nhận đăng nhập hay đăng kí
from tkinter import *
import user_or_admin
from register_form import register
from login_form import login

class reg_or_log:
    object_login = None # biến dùng để xác định đối tượng đăng nhập hay đăng kí là user hay admin
    object_register = None
    def __init__(self, object_login, object_register):
        self.object_login = object_login
        self.object_register = object_register
        self.root_reg_or_log = Tk()
        if self.object_login == "user" and self.object_register == "user":
            self.root_reg_or_log.title("ĐĂNG KÍ/ĐĂNG NHẬP-{}".format("User"))
        elif self.object_login == "admin" and self.object_register == "admin":
            self.root_reg_or_log.title("ĐĂNG KÍ/ĐĂNG NHẬP-{}".format("Admin"))
 
             
        self.root_reg_or_log.geometry("600x300")
        self.root_reg_or_log.config(background = "#336699")
        self.root_reg_or_log.resizable(0,0)
        self.btn_reg = Button(self.root_reg_or_log, text= "Đăng ký", font= ("bold", "16"), height= 2, width= 10, background = "red")
        self.btn_reg.config(command= self.validate_reg)
        self.btn_log = Button(self.root_reg_or_log, text= "Đăng nhập", font= ("bold", "16"), height= 2, width= 10, background = "red")
        self.btn_log.config(command= self.validate_log)
        self.btn_back = Button(self.root_reg_or_log, text= "Trở lại", font= ("bold", "16"), height= 2, width= 10)
        self.btn_back.config(command= self.back)
        self.btn_reg.pack(pady= 20)
        self.btn_log.pack(pady= 20)
        self.btn_back.pack(pady= 20)
 

    def start(self):  # hàm khởi chạy giao diện
        self.root_reg_or_log.mainloop()

    def validate_reg(self):  #tạo form xác nhận đăng kí 
            self.root_reg_or_log.destroy()
            reg = register(self.object_register)
            reg.start()
            
            
    def validate_log(self):  #tạo form xác nhận đăng nhập 
            self.root_reg_or_log.destroy()
            log = login(self.object_login)
            log.start()
            
    def back(self):   # hàm quaytrở lại các giao diện tương ứng
        self.root_reg_or_log.destroy()
        obj  = user_or_admin.user_admin()
        obj.start()


         



        
