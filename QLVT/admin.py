

# class dùng để cho admin sử lí tài khoản người dùng
from  tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import tkinter.ttk
import pandas as pd
import sqlite3

class UserData:
    
    record = None # biến dùng để chứa bản ghi
    def __init__(self):
        self.initUI()

    def start(self): # Hmà bắt đầu chạy giao diện
        self.master.mainloop()

    def initUI(self): # tạo giáo diện
        self.master = Tk()
        self.master.title("ADMIN")
        self.master.geometry("800x500")
        self.master.config(background =  "green")
        self.frame1 = Frame(self.master, highlightthickness = 2, highlightbackground = 'red', highlightcolor =  'red' )
        self.treeview = tkinter.ttk.Treeview(self.frame1, columns = ["#1", "#2", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9"], show = "headings")
        self.treeview.heading("#1", text = "ID", anchor = CENTER)
        self.treeview.heading("#2", text = "Tên", anchor = CENTER)
        self.treeview.heading("#3", text = "Email", anchor = CENTER)
        self.treeview.heading("#4", text = "Số điện thoại", anchor = CENTER)
        self.treeview.heading("#5", text = "Giới tính", anchor = CENTER)
        self.treeview.heading("#6", text = "Quốc gia", anchor = CENTER)
        self.treeview.heading("#7", text = "Tên đăng nhập", anchor = CENTER)
        self.treeview.heading("#8", text = "Mật khẩu", anchor = CENTER)
        self.treeview.heading("#9", text = "Trạng thái", anchor = CENTER)
        self.treeview.bind('<<TreeviewSelect>>',  self.item_select)
        self.scr_x = Scrollbar(self.frame1 , orient= HORIZONTAL, width= 18)
        self.scr_y = Scrollbar(self.frame1 , orient= VERTICAL, width= 18)
        self.treeview.config(xscrollcommand= self.scr_x.set, yscrollcommand= self.scr_y.set)
        self.scr_x.config(command = self.treeview.xview)
        self.scr_y.config(command= self.treeview.yview)
        self.scr_x.pack(side= BOTTOM, fill= X)
        self.scr_y.pack(side= RIGHT, fill= Y)
        self.treeview.pack( )
        self.frame1.pack(padx = 10, pady = 10)

        self.frame2 = Frame(self.master, background = "green",highlightthickness = 2, highlightbackground = 'red', highlightcolor =  'red' )
        bt_getData = Button(self.frame2, text = "Lấy dữ liệu", font = ("times", 12), width = 8, command = self.getData)
        bt_remove_result_treeview = Button(self.frame2, text = "Xóa kết quả", font = ("times", 12), width = 8, command = self.clear_treeview)
        bt_unselected_item = Button(self.frame2, text= "Xóa chọn", font= ("times", 12), width= 8, command = self.item_unselected)
        bt_getData.grid(row = 0, column = 0, padx = 10, pady = 10)
        bt_remove_result_treeview.grid(row = 0, column = 1, padx = 10, pady = 10)
        bt_unselected_item.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.frame2.place(x = 10, y = 270)

        self.frame3 = Frame(self.master, background= 'green', highlightthickness= 2, highlightbackground= 'red', highlightcolor= 'red')
        lb_title_find = Label(self.master, text= "Tìm kiếm bản ghi", font= ('Times', '18'), background= "green", foreground= "blue" )
        lb_find = Label(self.frame3, text= "Tìm kiếm theo", font= ("Times", 12), background= "green")
        lb_keyword = Label(self.frame3, text= "Từ khóa", font= ("Times", 12), background= 'green')
        self.cbb_find = tkinter.ttk.Combobox(self.frame3, font= ("bold", 14), width = 14)
        self.en_find = Entry(self.frame3, font= ("bold", 14), width = 16)
        self.cbb_find.set('Chọn')
        self.cbb_find.config (values= ['ID', 'Name', 'Email', 'Phone', 'GT', 'Nation', 'Username', 'Password', 'State'])
        bt_find = Button(self.frame3, text= "Tìm kiếm", font= ("Times", 12), width= 8, height= 1, command = self.search)
        lb_title_find.place(x = 880, y = 270)
        lb_find.grid(row = 0, column = 0, padx= 10, pady= 5)
        self.cbb_find.grid(row= 0, column= 1, padx= 10, pady= 5)
        lb_keyword.grid(row= 1, column= 0, padx= 10, pady= 5)
        self.en_find.grid(row= 1, column= 1, padx= 10, pady= 5)
        bt_find.grid(row = 1 , column = 3, padx= 15, pady= 5)
        self.frame3.place(x = 880, y = 300 )
       

        self.frame4 = Frame(self.master, highlightthickness= 2, highlightbackground= 'red', highlightcolor= 'red')
        # label
        self.lb_ID = Label(self.frame4, text= "ID", font= ("Times", 12))
        self.lb_name = Label(self.frame4, text= "Tên", font= ("Times", 12))
        self.lb_email = Label(self.frame4, text= "Email", font= ("Times", 12))
        self.lb_phone = Label(self.frame4, text= "Số điện thoại", font= ("Times", 12))
        self.lb_GT = Label(self.frame4, text= "Giới tính", font= ("Times", 12))
        self.lb_nation = Label(self.frame4, text= "Quốc gia", font= ("Times", 12))
        self.lb_username = Label(self.frame4, text= "Tên đăng nhập", font= ("Times", 12))
        self.lb_password = Label(self.frame4, text= "Mật khẩu", font= ("Times", 12))
        self.lb_state = Label(self.frame4, text= "Trạng thái", font= ("Times", 12))
        
        self.lb_ID.grid(row= 0, column= 0, padx= 10, pady= 10, sticky= W)
        self.lb_name.grid(row = 1, column= 0, padx= 10, pady= 10, sticky= W)
        self.lb_email.grid(row = 2, column= 0, padx= 10, pady= 10, sticky= W)
        self.lb_phone.grid(row = 3, column= 0, padx= 10, pady= 10, sticky= W)
        self.lb_GT.grid(row = 4, column= 0, padx= 10, pady= 10, sticky= W)
        self.lb_nation.grid(row = 0, column= 2, padx= 10, pady= 10, sticky= W)
        self.lb_username.grid(row = 1, column= 2, padx= 10, pady= 10, sticky= W)
        self.lb_password.grid(row= 2, column= 2, padx= 10, pady= 10, sticky= W)
        self.lb_state.grid(row= 3, column= 2, padx= 10, pady= 10, sticky= W)

        self.var_en_ID = StringVar()
        self.en_ID = Entry(self.frame4 , textvariable= self.var_en_ID,font= ("bold", 14))
        self.var_en_name = StringVar()
        self.en_name = Entry(self.frame4 , textvariable= self.var_en_name,font= ("bold", 14))
        self.var_en_email= StringVar()
        self.en_email = Entry(self.frame4 , textvariable= self.var_en_email,font= ("bold", 14))
        self.var_en_phone= StringVar()
        self.en_phone = Entry(self.frame4, textvariable= self.var_en_phone,font= ("bold", 14))
        self.var_en_GT= StringVar()
        self.en_GT = tkinter.ttk.Combobox(self.frame4, textvariable= self.var_en_GT,font= ('bold', 14))
        self.var_en_nation= StringVar()
        self.en_nation = tkinter.ttk.Combobox(self.frame4, textvariable= self.var_en_nation,font= ("bold", 14))
        self.var_en_username = StringVar()
        self.en_username = Entry(self.frame4, textvariable= self.var_en_username,font= ("bold", 14))
        self.var_en_password = StringVar()
        self.en_password = Entry(self.frame4, textvariable= self.var_en_password,font= ("bold", 14))
        self.var_en_state = StringVar()
        self.en_state = Entry(self.frame4, textvariable= self.var_en_state,font= ("bold", 14))
        self.en_ID.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.en_name.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.en_email.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.en_phone.grid(row = 3, column = 1, padx = 10, pady = 10)
        self.en_GT.grid(row = 4, column = 1,padx = 10, pady = 10)
        self.en_nation.grid(row = 0, column = 3,padx = 10, pady = 10)
        self.en_username.grid(row = 1, column = 3, padx = 10, pady = 10)
        self.en_password.grid(row = 2, column = 3, padx = 10, pady = 10)
        self.en_state.grid(row = 3, column = 3, padx = 10, pady = 10)
        self.frame4.place(x = 10, y = 350)

        self.fram5 = Frame(self.master, background = "green", highlightthickness= 2, highlightbackground= 'red', highlightcolor= 'red')
        lb_title_process = Label(self.master, text = "Xử lý", font= ('Times', 18), background= "green", foreground= "blue")
        self.cbb_process_account = tkinter.ttk.Combobox(self.fram5, font= ("bold", 14), width = 14)
        self.cbb_process_account.set("Chọn")
        self.cbb_process_account.config(values = ["Xóa tài khoản", "Khóa tài khoản", "Hủy khóa tài khoản"])
        self.bt_apply = Button(self.fram5, text = "Áp dụng", font = ("Times", 12), width = 8, height= 1, command = self.process_account)
        self.cbb_process_account.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.bt_apply.grid(row = 0, column = 1, padx = 10, pady = 10)
        lb_title_process.place(x = 10, y = 600)
        self.fram5.place(x = 10, y = 630)
        


        self.frame6 = Frame(self.master, background = "green",highlightthickness= 2, highlightbackground= 'red', highlightcolor= 'red')
        lb_title_import = Label(self.master, text = "Xuất file", font= ('Times', '18'), background= "green", foreground= "blue")
        self.lb_choose_file_type = Label(self.frame6, text = "Chọn loại file", font = ("Times", 12), background = "green")
        self.lb_directory_file = Label(self.frame6, text = "Đường dẫn", font = ("Times", 12), background = "green")
        self.lb_name_file = Label(self.frame6, text = "Tên file", font = ("Times", 12), background = "green")
        self.en_choose_file_type = tkinter.ttk.Combobox(self.frame6, font= ("bold", 14), width= 14)
        self.en_choose_file_type.set("Chọn")
        self.en_choose_file_type.config(values= ['xls', 'xlsx','csv'])
        self.var_en_directory = StringVar()
        self.en_directory = Entry(self.frame6, textvariable = self.var_en_directory ,font= ("bold", 14), width = 16)
        self.var_en_name_file = StringVar()
        self.en_name_file = Entry(self.frame6, textvariable = self.var_en_name_file ,font= ("bold", 14), width = 16)
        self.bt_browse_dir = Button(self.frame6, text = "Browse", width = 8, height = 1, font = ("Times", 12), command = self.get_path)
        self.bt_import = Button(self.frame6, text = "Xuất dữ liệu", width = 8, height = 1, font = ("Times", 12), command = self.save_to_file)
        self.lb_choose_file_type.grid(row = 0, column = 0, padx= 10, pady= 10, sticky= W)
        self.lb_directory_file.grid(row = 1, column= 0 , padx= 10, pady = 10, sticky= W)
        self.lb_name_file.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)
        self.en_choose_file_type.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.en_directory.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.en_name_file.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.bt_browse_dir.grid(row = 1, column = 3, padx = 10)
        self.bt_import.grid(row = 3, column = 1 , pady = 10)
        lb_title_import.place( x = 880, y = 415)
        self.frame6.place(x = 880, y = 450 )


    
    def getData(self): # lấy taonf bộ dữ liệu từ database
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        conn = sqlite3.connect("Userdatabase.db")
        cursor = conn.cursor()
        cursor.execute("select * from User")
        self.rows = cursor.fetchall()
        conn.commit()
        conn.close()

        number_item = 0  
        for row in self.rows:
            self.treeview.insert('', number_item, values = row)
            number_item += 1

    
    def item_select(self, event): # hàm dùng để chọn danh sách trên treeview
        selected_item = self.treeview.selection()
        self.l =[] # list dùng để lưu bản ghi đã chọn
        if selected_item != ():
            for i in range(0, len(selected_item)):
                item = self.treeview.item(selected_item[i])
                self.record = list(item.values())
                self.l.append(self.record[2]) # Đưa các phần tử đã chọn vào list
                self.var_en_ID.set(self.record[2][0])
                self.var_en_name.set(self.record[2][1])
                self.var_en_email.set(self.record[2][2])
                self.var_en_phone.set(self.record[2][3])
                self.var_en_GT.set(self.record[2][4])
                self.var_en_nation.set(self.record[2][5]) 
                self.var_en_username.set(self.record[2][6])
                self.var_en_password.set(self.record[2][7])
                self.var_en_state.set(self.record[2][8])

    
    def item_unselected(self): # xóa chọn 
        self.treeview.selection_remove(self.treeview.focus())
        self.record = None
        self.var_en_ID.set("")
        self.var_en_name.set("")
        self.var_en_email.set("")
        self.var_en_phone.set("")
        self.var_en_GT.set("")
        self.var_en_nation.set("")
        self.var_en_username.set("")
        self.var_en_password.set("")
        self.var_en_state.set("")

    def clear_treeview(self): # xóa kết quả hiển thị trên treeview
       for item in self.treeview.get_children():
           self.treeview.delete(item)
  
    def search(self): # tìm kiếm bản ghi theo truwòng nào đó
        criteria = self.cbb_find.get()
        keyword = self.en_find.get()
        if criteria not in ["ID", "Name", "Email", "Phone", "GT", "Username", "Password", "State"]:
            messagebox.showwarning("Thống báo", "Bạn cần chọn chỉ tiêu tìm kiếm!")
        else:
            conn = sqlite3.connect("Userdatabase.db")
            cursor = conn.cursor()

            if criteria == "ID":
                if not keyword.isdecimal():
                    messagebox.showinfo("Thông báo", "Nhập ID không đúng định dạng!")
                else:
                    cursor.execute("select * from User where [{}] = {}".format(criteria, int(keyword)))
                    rows = cursor.fetchall()

            if criteria != "ID":
                cursor.execute("select * from User where [{}] = '{}'".format(criteria, keyword))
                rows = cursor.fetchall()

            if rows == []:
                messagebox.showinfo("Thông báo", "Không có dữ diệu khớp với từ khóa!")
            else:
                for item in self.treeview.get_children():
                    self.treeview.delete(item)
                for row in rows:
                    self.treeview.insert('', END, values= row)

    def get_path(self): # Lấy đường dẫn để lưu file
        file = askdirectory(title= "Choose destination")
        self.var_en_directory.set(file)

    def save_to_file(self): #Để lưu file export
        if self.en_choose_file_type.get() == "" or self.en_choose_file_type.get() == "Chọn":
            messagebox.showinfo("Thông báo", "Vui lòng chọn loại file!")
            self.en_choose_file_type.focus_set()
        elif self.en_directory.get() == "":
            messagebox.showinfo("Thông báo", "Vui lòng chọn hoặc chèn đường dẫn!")
            self.en_directory.focus_set()
        elif self.en_name_file.get() =="":
            messagebox.showinfo("Thông báo", "Vui lòng nhập tên file!")
            self.en_choose_file_type.focus_set()
        else:
            pass
            # selected_item = self.treeview.selection()
            # if selected_item ==():
            #     messagebox.showinfo("Thông báo", "Vui lòng click một chọn bản ghi trong bảng kết quả hoặc nhấn phím Ctr + click để chọn nhiều bản ghi!")
            # elif selected_item != ():
            #     if self.en_choose_file_type.get() == "xls" or self.en_choose_file_type == "xlsx":
            #         for i in range(0, len(selected_item)):
            #             dataframe_excel = pd.DataFrame([self.record[2][i], self.record[2][i], self.record[2][i], self.record[2][i],self.record[2][i], self.record[2][i],self.record[2][i], self.record[2][i], self.record[2][i], self.record[2][i]], ["ID", "Name", "Email", "Phone", "GT", "Username", "Password", "State"])
            #             with pd.ExcelFile("{}/{}.{}".format(self.en_directory.get(), self.en_name_file.get(),self.en_choose_file_type.get())) as writer:
            #                 dataframe_excel.to_excel(writer, sheet_name = "Sheet1")

            #     if self.en_choose_file_type.get() == "csv":
            #         for i in range(0, len(selected_item)):
            #             dataframe_csv = pd.DataFrame([self.record[2][i], self.record[2][i], self.record[2][i], self.record[2][i],self.record[2][i], self.record[2][i],self.record[2][i], self.record[2][i], self.record[2][i], self.record[2][i]], ["ID", "Name", "Email", "Phone", "GT", "Username", "Password", "State"])
            #             with pd.ExcelFile("{}/{}.{}".format(self.en_directory.get(), self.en_name_file.get(),self.en_choose_file_type.get())) as writer:
            #                 dataframe_excel.to_csv(writer, sheet_name = "Sheet1")


    def process_account(self): # các hành động xử lí tài khoản người dùng: như khóa, hủy khóa, xóa tk user
        conn = sqlite3.connect("UserDatabase.db")
        cursor = conn.cursor()
        if self.cbb_process_account.get() == "Xóa tài khoản":
            if self.record == None:
                messagebox.showwarning("Thông báo", "Hãy chọn bản ghi trong bảng trên!")
            else:
                c = cursor.execute("delete from User where ID = {} and Name = '{}' and Email = '{}' and Phone = '{}' and GT = '{}' and Nation = '{}' and Username = '{}' and Password = '{}' and State = '{}'".format(self.record[2][0], self.record[2][1], self.record[2][2], self.record[2][3],self.record[2][4], self.record[2][5], self.record[2][6], self.record[2][7], self.record[2][8]))
                conn.commit()
                conn.close
                if c != None:
                    messagebox.showinfo("Thông báo", "Bạn đã xóa dữ liệu thành công!")
        
        elif self.cbb_process_account.get() == "Khóa tài khoản":
            if self.record == None:
                messagebox.showwarning("Thông báo", "Hãy chọn bản ghi trong bảng trên!")
            else:
                c = cursor.execute("Update User set State = 'Khóa' where ID = {} and Name = '{}' and Email = '{}' and Phone = '{}' and GT = '{}' and Nation = '{}' and Username = '{}' and Password = '{}' and State = '{}'".format(self.record[2][0], self.record[2][1], self.record[2][2], self.record[2][3],self.record[2][4], self.record[2][5], self.record[2][6], self.record[2][7], self.record[2][8]))
                conn.commit()
                conn.close
                for item in self.treeview.get_children():
                    self.treeview.delete(item)
                self.var_en_state.set("Khóa")
                self.record[2][8] = "Khóa"
                for item in self.treeview.get_children():
                    self.treeview.delete(item)
                self.treeview.insert('', END, values = [self.record[2][0], self.record[2][1], self.record[2][2], self.record[2][3], self.record[2][4], self.record[2][5], self.record[2][6], self.record[2][7], self.record[2][8]])
                messagebox.showinfo("Thông báo", "Bạn vừa mới khóa tài khoản người dùng!")

        elif self.cbb_process_account.get() =="Hủy khóa tài khoản":
            if self.record == None:
                messagebox.showwarning("Thông báo", "Hãy chọn bản ghi trong bảng trên!")
            else:
                cursor.execute("Update User set State = 'Hoạt động' where ID = {} and Name = '{}' and Email = '{}' and Phone = '{}' and GT = '{}' and Nation = '{}' and Username = '{}' and Password = '{}' and State = 'Khóa'".format(self.record[2][0], self.record[2][1], self.record[2][2], self.record[2][3],self.record[2][4], self.record[2][5], self.record[2][6], self.record[2][7]))
                conn.commit()
                conn.close
                for item in self.treeview.get_children():
                    self.treeview.delete(item)
                self.var_en_state.set("Hoạt động")
                self.record[2][8] = "Hoạt động"
                for item in self.treeview.get_children():
                    self.treeview.delete(item)
                self.treeview.insert('', END, values = [self.record[2][0], self.record[2][1], self.record[2][2], self.record[2][3], self.record[2][4], self.record[2][5], self.record[2][6], self.record[2][7], self.record[2][8]])
                messagebox.showinfo("Thông báo", "Bạn vừa mới hủy khóa tài khoản!")


        else:
            messagebox.showwarning("Thông báo", "Chọn một hành động để xử lí tài khoản!")
        
