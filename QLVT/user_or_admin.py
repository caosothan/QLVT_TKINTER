

# Class dùng để xác định trạng thái người dùng user hay admin


from tkinter import *
import register_or_login

class user_admin:
    state = ["user", "admin"]
    
    def __init__(self):
        self.validate_from_login()


    def start(self): # hàm bắt đầu chạy giao diện
        self.root_user_admin.mainloop()

    def validate_from_login(self):
        self.root_user_admin = Tk()
        self.root_user_admin.geometry("600x300")
        self.root_user_admin.title("QUẢN LÍ VẬT TƯ")
        self.root_user_admin.resizable(0,0)
        self.root_user_admin.config(background= "#336699")
        self.var_state = StringVar()
        self.var_state.set("  ")
        lb = Label(self.root_user_admin, text = "BẠN LÀ NGƯỜI DÙNG HAY QUẢN TRỊ VIÊN?", font= ("Times", 20), background= "#336699", foreground= "#00FF00")
        cbbox_user = Radiobutton(self.root_user_admin, text  ="Người dùng", variable= self.var_state, value = "user", font = ("times", 16), foreground= "red", background= "#336699")
        cbbox_server = Radiobutton(self.root_user_admin, text= "Quản trị viên", variable= self.var_state, value= "admin", font = ("times", 16), foreground= "red", background= "#336699")
        btn_next = Button(self.root_user_admin, text ="Tiếp theo", font = ("Times", 14), background = "#EEEEEE" ,command= self.button_next)
        lb.pack(pady= 20)
        cbbox_user.pack(pady = 20)
        cbbox_server.pack(pady =20)
        btn_next.pack(pady= 20)
    
    def button_next(self):
        if self.var_state.get() == self.state[0]:
            self.root_user_admin.destroy()
            obj = register_or_login.reg_or_log(self.state[0], self.state[0])
            obj.start()
           
        elif self.var_state.get() == self.state[1]:

            self.root_user_admin.destroy()
            obj = register_or_login.reg_or_log(self.state[1], self.state[1])
            obj.start()
            



