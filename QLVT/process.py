

# class này dùng để user sử lí dữ liệu quản lí vật tư (QLVT)

from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askokcancel
import tkinter.ttk
import sqlite3
from tkinter.filedialog import askdirectory
import pandas as pd
import csv

class process:
    record = None #biến bản ghi để chứa bản ghi
    def __init__(self):
        self.createUI()
        

    def start(self): # hàm bắt đầu chạy giao diện
        self.root_process.mainloop()

    
    def createUI(self): # tạo giao diện để user dùng sử lí
        self.root_process = Tk()
        self.root_process.geometry('800x800')
        self.root_process.title("QUẢN LÍ VẬT TƯ")
        self.root_process.config(background= '#336699')
        lb_title_input = Label(self.root_process, text= "Nhập dữ liệu", font= ('Times', 18), background= "#336699", foreground= "red")
        self.frame = Frame(self.root_process, highlightthickness= 2, highlightbackground= 'red', highlightcolor= 'red')
        # label
        self.lb_name_device = Label(self.frame, text= "Tên thiết bị", font= ("Times", 12))
        self.lb_serial = Label(self.frame, text= "Số seri", font= ("Times", 12))
        self.lb_type = Label(self.frame, text= "Phân loại", font= ("Times", 12))
        self.lb_manufacturer = Label(self.frame, text= "Nhà sản xuất", font= ("Times", 12))
        self.lb_local = Label(self.frame, text= "Địa phương", font= ("Times", 12))
        self.lb_result_before_fixing = Label(self.frame, text= "Kết quả kiểm tra trước sửa chữa", font= ("Times", 12))
        self.lb_handover_status = Label(self.frame, text= "Tình trạng bàn giao đi sửa chữa", font= ("Times", 12))
        self.lb_serial_afterr_fixing = Label(self.frame, text= "Số serial sau sửa chữa", font= ("Times", 12))
        self.lb_result_after_fixing = Label(self.frame, text= "Kết quả sau sửa chữa", font= ("Times", 12))
        # set layout
        self.lb_name_device.grid(row= 0, column= 0, padx= 10, pady= 10, sticky= W)
        self.lb_serial.grid(row= 1, column= 0, padx= 10, pady= 10, sticky= W)
        self.lb_type.grid(row= 2, column= 0, padx= 10, pady= 10, sticky= W)
        self.lb_manufacturer.grid(row= 3, column= 0, padx= 10, pady= 10, sticky= W)
        self.lb_local.grid(row= 4, column= 0, padx= 10, pady= 10, sticky= W)
        self.lb_serial_afterr_fixing.grid(row= 0, column= 2, padx= 10, pady= 10, sticky= W)
        self.lb_result_before_fixing.grid(row= 1, column= 2, padx= 10, pady= 10, sticky= W)
        self.lb_handover_status.grid(row= 2, column= 2, padx= 10, pady= 10, sticky= W)
        self.lb_result_after_fixing.grid(row= 3, column= 2, padx= 10, pady= 10, sticky= W)

        # entry
        self.var_en_name_device = StringVar()
        self.en_name_device = Entry(self.frame , textvariable= self.var_en_name_device ,font= ("bold", 14))
        self.var_en_serial= StringVar()
        self.en_serial = Entry(self.frame , textvariable= self.var_en_serial,font= ("bold", 14))
        self.var_en_type= StringVar()
        self.var_en_type.set("Chọn hoặc nhập...")
        self.en_type = tkinter.ttk.Combobox(self.frame, textvariable= self.var_en_type,font= ("bold", 13), values = self.get_list_type())
        self.var_en_manufacturer= StringVar()
        self.var_en_manufacturer.set("Chọn hoặc nhập...")
        self.en_manufacturer = tkinter.ttk.Combobox(self.frame, textvariable= self.var_en_manufacturer,font= ('bold', 13), values = self.get_list_manufacturer())
        self.var_en_local= StringVar()
        self.var_en_local.set("Chọn hoặc nhập...")
        self.en_local = tkinter.ttk.Combobox(self.frame, textvariable= self.var_en_local,font= ("bold", 13), values = self.get_list_local())
        self.var_en_result_before_fixing = StringVar()
        self.var_en_result_before_fixing.set("Chọn hoặc nhập...")
        self.en_result_before_fixing = tkinter.ttk.Combobox(self.frame, textvariable= self.var_en_result_before_fixing,font= ("bold", 13), values = ("Hỏng", "Bình thường"))
        self.var_en_handover_status = StringVar()
        self.var_en_handover_status.set("Chọn hoặc nhập...")
        self.en_handover_status = tkinter.ttk.Combobox(self.frame, textvariable= self.var_en_handover_status,font= ("bold", 13), values = ["Tiếp nhận", "Không tiếp nhận", "Chưa tiếp nhận"])
        self.var_en_serial_after_fixing = StringVar()
        self.en_serial_after_fixing = Entry(self.frame, textvariable= self.var_en_serial_after_fixing,font= ("bold", 14))
        self.var_en_result_after_fixing = StringVar()
        self.var_en_result_after_fixing .set("Chọn hoặc nhập...")
        self.en_result_after_fixing = tkinter.ttk.Combobox(self.frame, textvariable= self.var_en_result_after_fixing, font= ("bold", 13), values = ["Tốt", "Không tốt"])

        #set layout
        self.en_name_device.grid(row= 0, column= 1, padx= 10, pady= 10)
        self.en_serial.grid(row= 1, column= 1, padx= 1, pady= 10)
        self.en_type.grid(row= 2, column= 1, padx= 1, pady= 10)
        self.en_manufacturer.grid(row= 3, column= 1, padx= 10, pady= 10)
        self.en_local.grid(row= 4, column= 1, padx= 10, pady= 10)
        self.en_serial_after_fixing.grid(row= 0, column= 3, padx= 10, pady= 10)
        self.en_result_before_fixing.grid(row= 1, column = 3, padx= 10, pady= 10)
        self.en_handover_status.grid(row = 2, column= 3, padx= 10, pady= 10)
        self.en_result_after_fixing.grid(row= 3, column= 3, padx= 10, pady= 10)
        lb_title_input.place(x = 10, y = 350)
        self.frame.place(x = 10, y = 380)
       
        


        # button
        self.frame1 = Frame(self.root_process, background= "#336699", highlightthickness= 2, highlightbackground= 'red', highlightcolor= 'red')
        f1 = ('Times', 12)
        self.getdata_bt = Button(self.frame1, text= "Lấy dữ liệu", font= f1, width= 8, command= self.getData)
        self.add_button = Button(self.frame1, text= "Thêm", font= f1, width= 8, command= self.addData)
        self.update_button = Button(self.frame1, text= "Cập nhật", font= f1, width= 8, command= self.update)
        #set layout
        self.getdata_bt.grid(row= 0, column= 0, padx= 10, pady= 10, sticky= W)
        self.add_button.grid(row= 0, column= 1, padx= 10, pady= 10, sticky= W)
        self.update_button.grid(row= 0, column= 2, padx= 10, pady= 10, sticky= W)
        self.frame1.place(x = 10, y = 630)

        # tạo treeview để xem dữ liệu
        self.frame2 = Frame(self.root_process, background= "#336699", highlightthickness= 2, highlightbackground= 'red', highlightcolor= 'red')
        lb_title_result = Label(self.root_process, text= "Kết quả", font= ('Times', 18), background= "#336699", foreground= "red")
        self.treeview = tkinter.ttk.Treeview(self.frame2, columns= ['#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10'], show= "headings", selectmode = "extended")
        self.treeview.heading('#1', text= "ID", anchor= CENTER)
        self.treeview.heading('#2', text= "Tên thiết bị", anchor= CENTER)
        self.treeview.heading('#3', text= "Số serial", anchor= CENTER)
        self.treeview.heading('#4', text= "Phân loại", anchor= CENTER)
        self.treeview.heading('#5', text= "Nhà sản xuất", anchor= CENTER)
        self.treeview.heading('#6', text= "Đài Viễn Thông/Điều hành/Vô Tuyến", anchor= CENTER)
        self.treeview.heading('#7', text= "Kết quả kiểm tra trước sửa chữa", anchor= CENTER)
        self.treeview.heading('#8', text= "Tình trạng bàn giao đi sửa chữa", anchor= CENTER)
        self.treeview.heading("#9", text = "Số serial sau sửa chữa")
        self.treeview.heading('#10', text= "Kết quả kiểm tra sau sửa chữa", anchor= CENTER)

        self.treeview.bind('<<TreeviewSelect>>',  self.item_select)
        self.scr_x = Scrollbar(self.frame2 , orient= HORIZONTAL, width= 18)
        self.scr_y = Scrollbar(self.frame2 , orient= VERTICAL, width= 18)
        self.treeview.config(xscrollcommand= self.scr_x.set, yscrollcommand= self.scr_y.set)
        self.scr_x.config(command = self.treeview.xview)
        self.scr_y.config(command= self.treeview.yview)
        self.scr_x.pack(side= BOTTOM, fill= X)
        self.scr_y.pack(side= RIGHT, fill= Y)
        self.treeview.pack(side= TOP)
        lb_title_result.place(x = 10, y = 10)
        self.frame2.pack(padx = 10, pady = 45 )

        self.frame3 = Frame(self.root_process, background= "#336699", highlightthickness= 2, highlightbackground= 'red', highlightcolor= 'red')
        bt_delete = Button(self.frame3, text= "Xóa bản ghi", font= f1, width= 8, command= self.delete_record)
        bt_remove_result_treeview = Button(self.frame3, text= "Xóa kết quả", font= f1, width= 8, command= self.clear_treeview)
        bt_unselected_item = Button(self.frame3, text= "Xóa chọn", font= f1, width= 8, command= self.item_unselected)
        bt_delete.grid(row = 0, column = 0, padx = 10, pady = 10)
        bt_remove_result_treeview.grid(row = 0, column = 1, padx = 10, pady = 10)
        bt_unselected_item.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.frame3.place(x = 10, y = 290)


        self.frame4 = Frame(self.root_process, background= '#336699', highlightthickness= 2, highlightbackground= 'red', highlightcolor= 'red')
        lb_title_find = Label(self.root_process, text= "Tìm kiếm bản ghi", font= ('Times', 18), background= "#336699", foreground= "red" )
        lb_find = Label(self.frame4, text= "Tìm kiếm theo", font= ('Times', 12), background= '#336699')
        lb_keyword = Label(self.frame4, text= "Từ khóa", font= ('Times', 12), background= '#336699')
        self.cbb_find = tkinter.ttk.Combobox(self.frame4, font= ('bold', 14))
        self.en_find = Entry(self.frame4, font= ('bold', 16))
        self.cbb_find.set('Chọn')
        self.cbb_find.config (values= ['Tên thiết bị', 'Số Serial', 'Phân loại', 'Nhà sản xuất', 'Đài Viễn Thông/Điều hành/Vô tuyến', "Kết quả kiểm tra trước sửa chữa", "Tình trạng bàn giao đi sửa chữa", "Số serial sau SC", "Kết quả kiểm tra sau sửa chữa"])
        bt_find = Button(self.frame4, text= "Tìm kiếm", font= ("Times", 12), width= 8, height= 1, command= self.search)
        lb_find.grid(row = 0, column = 0, padx= 10, pady= 5)
        self.cbb_find.grid(row= 0, column= 1, padx= 10, pady= 5)
        lb_keyword.grid(row= 1, column= 0, padx= 10, pady= 5)
        self.en_find.grid(row= 1, column= 1, padx= 10, pady= 5)
        bt_find.grid(row = 1 , column = 3, padx= 15, pady= 5)
        lb_title_find.place(x = 840, y = 310)
        self.frame4.place(x = 840, y = 340 )
 

        self.frame5 = Frame(self.root_process, background = "#336699", highlightthickness= 2, highlightbackground= 'red', highlightcolor= 'red')
        lb_title_import = Label(self.root_process, text = "Xuất file", font= ('Times', 18), background= "#336699", foreground= "red")
        self.lb_choose_file_type = Label(self.frame5, text = "Chọn loại file", font = ("Times", 12), background = "#336699")
        self.lb_directory_file = Label(self.frame5, text = "Đường dẫn", font = ("Times", 12), background = "#336699")
        self.lb_name_file = Label(self.frame5, text = "Tên file", font = ("Times", 12), background = "#336699")
        self.en_choose_file_type = tkinter.ttk.Combobox(self.frame5, font= ("bold", 14), width= 15)
        self.en_choose_file_type.set("Chọn")
        self.en_choose_file_type.config(values= ['xls','xlsx', 'csv'])
        self.var_en_directory = StringVar()
        self.en_directory = Entry(self.frame5, textvariable = self.var_en_directory ,font= ("bold", 14), width = 17)
        self.var_en_name_file = StringVar()
        self.en_name_file = Entry(self.frame5, textvariable = self.var_en_name_file ,font= ("bold", 14), width = 17)
        self.bt_browse_dir = Button(self.frame5, text = "Browse", command= self.get_path)
        self.bt_import = Button(self.frame5, text = "Xuất dữ liệu", command= self.save_to_file)
        self.lb_choose_file_type.grid(row = 0, column = 0, padx= 10, pady= 10, sticky= W)
        self.lb_directory_file.grid(row = 1, column= 0 , padx= 10, pady = 10, sticky= W)
        self.lb_name_file.grid(row = 2, column = 0, padx =10, pady = 10)
        self.en_choose_file_type.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.en_directory.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.en_name_file.grid(row = 2, column = 1, padx = 10, pady = 10 )
        self.bt_browse_dir.grid(row = 1, column = 3, padx = 10)
        self.bt_import.grid(row = 3, column = 1 , pady = 10)
        lb_title_import.place( x = 840, y = 450)
        self.frame5.place(x = 840, y = 480 )
     



    def addData(self): # thêm dữ liệu vào cơ sở dữ liệu vào QLVT.db
        name = self.en_name_device.get()
        serial = self.en_serial.get()
        model = self.en_type.get()
        manufacturer = self.en_manufacturer.get()
        local = self.en_local.get()
        result_before_fixing= self.en_result_before_fixing.get()
        handover_status = self.en_handover_status.get()
        serial_after_fixing = self.en_serial_after_fixing.get()
        result_after_fixing = self.en_result_after_fixing.get()
        
        if  (name == '' or serial =='' or model =='' or manufacturer =='' or local =='' ):
            messagebox.showwarning('Thông báo', 'Bạn cần nhập đủ thông tin!')
        else:
            conn = sqlite3.connect(database= 'QLVT.db')
            cursor = conn.cursor()
            command = '''INSERT INTO VATTU(ID, [Tên thiết bị], [Số Serial], [Phân loại], [Nhà sản xuất], [Đài Viễn Thông/Điều hành/Vô tuyến], [Kết quả kiểm tra trước sửa chữa], [Tình trạng bàn giao đi sửa chữa], [Số serial sau SC], [Kết quả kiểm tra sau sửa chữa]) values(?,?,?,?,?,?,?,?,?,?)'''
            dt = (name, serial, model, manufacturer, local, result_before_fixing, handover_status, serial_after_fixing, result_after_fixing )
            c = cursor.execute(command, dt)
            

            if c != None:
                messagebox.showinfo('Thông báo', 'Thêm cơ sở dữ liệu tành công!') 
            
            else:
                messagebox.showerror('Thông báo', 'Thêm vào cơ sở dữ liệu không thành công')
            conn.commit()
            conn.close()

        for item in self.treeview.get_children():
            self.treeview.delete(item)
        self.treeview.insert('', END, values= [self.en_name_device.get(), self.en_serial.get(), self.en_type.get(), self.en_manufacturer.get(), self.en_local.get(), self.en_result_before_fixing.get(), self.en_handover_status.get(), self.en_serial_after_fixing.get(), self.en_result_after_fixing.get()])


   

        
    def getData(self): # lấy toàn bộ cơ sở dữ liệu từ QLVT.db
        asker = messagebox.askokcancel("Thông báo", "Bạn có muốn lấy toàn bộ dữ liệu!")
        if asker == True:
            for item in self.treeview.get_children():
                self.treeview.delete(item)
            conn = sqlite3.connect("QLVT.db")
            cursor = conn.cursor()
            cursor.execute("select * from VATTU")
            self.rows = cursor.fetchall()
            conn.commit()
            conn.close()
            number_item = 0  
            for row in self.rows:
                self.treeview.insert('', number_item, values = row)
                number_item += 1



        

    
    def clear_treeview(self): # xóa danh sách hiện thị trên treeview
       if self.record == None:
            messagebox.showinfo("Thông báo", "Không có kết quả nào được hiện!")
       else:
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        self.var_en_name_device.set("")
        self.var_en_serial.set("")
        self.var_en_type.set("")
        self.var_en_manufacturer.set("")
        self.var_en_local.set("")
        self.var_en_result_before_fixing.set("")
        self.var_en_handover_status.set("")
        self.var_en_serial_after_fixing.set("")
        self.var_en_result_after_fixing.set("")

    def delete_record(self): # xóa bản ghi trong database QLVT.db
        if self.record ==None:
            messagebox.showwarning("Thông báo", "Bạn cần chọn bản ghi từ bảng kết quả hoặc nhập dữ liệu từ trường dữu liệu!") 
        else:
            conn = sqlite3.connect("QLVT.db")
            cursor = conn.cursor()
            c  = cursor.execute("delete from VATTU where [ID = {} and Tên thiết bị] = '{}' and [Số Serial] = '{}' and [Phân loại] = '{}' and [Nhà sản xuất] = '{}' and [Đài Viễn Thông/Điều hành/Vô tuyến] = '{}' and [] = {} and [] = {} and  [] = {} and [] = {} ".format(self.record[2][0], self.record[2][1], self.record[2][2], self.record[2][3], self.record[2][4]))
            conn.commit()
            conn.close()
            messagebox.showinfo("Thông báo", "Bạn đã xóa dữ liệu thành công!")
            
            selected_item = self.treeview.selection()
            if selected_item != []:
                self.treeview.delete(selected_item)

            self.var_en_name_device.set("")
            self.var_en_serial.set("")
            self.var_en_type.set("")
            self.var_en_manufacturer.set("")
            self.var_en_local.set("")
            self.var_en_result_before_fixing.set("")
            self.var_en_handover_status.set("")
            self.var_en_serial_after_fixing.set("")
            self.var_en_result_after_fixing.set("")
                

        
        
    
    def item_select(self, event):# Đưa các phần tử đã chọn vào list
        selected_item = self.treeview.selection()
        self.l = []  #list dùng để lưu bản ghi đã chọn
        if selected_item != ():
            for i in range(0, len(selected_item)):
                item = self.treeview.item(selected_item[i])
                self.record = list(item.values())  #Đưa các phần tử đã chọn vào list
                self.l.append(self.record[2])
                self.var_en_name_device.set(self.record[2][1])
                self.var_en_serial.set(self.record[2][2])
                self.var_en_type.set(self.record[2][3])
                self.var_en_manufacturer.set(self.record[2][4])
                self.var_en_local.set(self.record[2][5])
                self.var_en_result_before_fixing.set(self.record[2][6])
                self.var_en_handover_status.set(self.record[2][7])
                self.var_en_serial_after_fixing.set(self.record[2][8])
                self.var_en_serial_after_fixing.set(self.record[2][9]) 
            
    def item_unselected(self): #xóa chọn bản ghi trên treeview
        if self.record != None:
            self.record = None
            self.treeview.selection_remove(self.treeview.focus())
            self.var_en_name_device.set("")
            self.var_en_serial.set("")
            self.var_en_type.set("")
            self.var_en_manufacturer.set("")
            self.var_en_local.set("")
            self.var_en_result_before_fixing.set("")
            self.var_en_handover_status.set("")
            self.var_en_serial_after_fixing.set("")
            self.var_en_serial_after_fixing.set("") 
        else:
            messagebox.showinfo("Thông báo", "Không có bản ghi nào được chọn!")

    def update(self):  #cập nhật dữ liệu khi sửa trên entry
        if self.record == None:
            messagebox.showwarning("Thông báo", "Bạn cần chọn bản ghi trong bảng kết quả để cập nhât!")
        else:
            selected_item = self.treeview.selection()
            conn = sqlite3.connect("QLVT.db")
            cursor = conn.cursor()
            cursor.execute("update VATTU set [Tên thiết bị] = '{}', [Số Serial] = '{}', [Phân loại] = '{}', [Nhà sản xuất] = '{}', [Đài Viễn Thông/Điều hành/Vô tuyến] = '{}' where [Tên thiết bị] = '{}' and [Số Serial] = '{}' and [Phân loại] = '{}' and [Nhà sản xuất] = '{}' and [Đài Viễn Thông/Điều hành/Vô tuyến] = '{}'".format(self.en_name_device.get(), self.en_serial.get(), self.en_type.get(), self.en_manufacturer.get(), self.en_local.get(), self.record[2][0], self.record[2][1], self.record[2][2], self.record[2][3], self.record[2][4]))
            conn.commit()
            conn.close()
            for item in self.treeview.get_children():
                self.treeview.delete(item)
            self.record[2][1] = self.en_name_device.get()
            self.record[2][2] = self.en_serial.get()
            self.record[2][3] = self.en_type.get()
            self.record[2][4] = self.en_manufacturer.get()
            self.record[2][5] = self.en_local.get()
            self.record[2][6] = self.en_result_before_fixing.get()
            self.record[2][7] = self.en_handover_status.get()
            self.record[2][8] = self.en_serial_after_fixing.get()
            self.record[2][9] = self.en_result_after_fixing.get()
            self.treeview.insert('', END, values = [self.record[2][0], self.record[2][1], self.record[2][2], self.record[2][3], self.record[2][4], self.record[2][5], self.record[2][6], self.record[2][7], self.record[2][8], self.record[2][9]])
           
        
    def search(self):  #tìm kiếm bản ghi theo trường nào đó
        criteria = self.cbb_find.get()
        keyword = self.en_find.get()
        if criteria not in ["Tên thiết bị", "Số Serial", "Phân loại", "Nhà sản xuất", "Đài Viễn Thông/Điều hành/Vô tuyến", "Kết quả kiểm tra trước sửa chữa", "Tình trạng bàn giao đi sửa chữa", "Số serial sau SC", "Kết quả kiểm tra sau sửa chữa"]:
            messagebox.showwarning("Thông báo", "Bạn cần chọn chỉ tiêu tìm kiếm!")
        else:
            conn = sqlite3.connect("QLVT.db")
            cursor = conn.cursor()
            cursor.execute("select * from VATTU where [{}] = '{}'".format(criteria, keyword))
            rows = cursor.fetchall()
            for item in self.treeview.get_children():
                self.treeview.delete(item)
            if rows == []:
                messagebox.showinfo("Thông báo", "Không có dữ diệu khớp với từ khóa!")
            else:
                for item in self.treeview.get_children():
                    self.treeview.delete(item)
                for row in rows:
                    self.treeview.insert('', END, values= row)
    
    def get_list_manufacturer(self): #lấy danh sách các nhà sản xuất đưa vào combobox
        conn = sqlite3.connect("QLVT.db")
        cursor = conn.cursor()
        cursor.execute("select distinct [Nhà sản xuất] from VATTU")
        list_manufacturer = cursor.fetchall()
        new_list_manufacturer = []
        for element in list_manufacturer:
            for item in element:
                new_list_manufacturer.append(item)
        conn.commit()
        conn.close()
        return new_list_manufacturer


    def get_list_local(self): #lấy danh sách các địa phương, đài truyền hình đưa vào combobox
        conn = sqlite3.connect("QLVT.db")
        cursor = conn.cursor()
        cursor.execute("select distinct [Đài Viễn Thông/Điều hành/Vô tuyến] from VATTU")
        list_local = cursor.fetchall()  
        new_list_local = []
        for element in list_local:
            for item in element:
                new_list_local.append(item)
        conn.commit()
        conn.close()
        return new_list_local  


    def get_list_type(self): #lấy danh sách các loại thiết bị đưa vào combobox để chọn
        conn = sqlite3.connect("QLVT.db")
        cursor = conn.cursor()
        cursor.execute("select distinct [Phân loại] from VATTU")
        list_type = cursor.fetchall()  
        new_list_type = []
        for element in list_type:
            for item in element:
                new_list_type.append(item)
        conn.commit()
        conn.close()
        return new_list_type 
    
    def get_list_result_before_fixing(self): 
        conn = sqlite3.connect("QLVT.db")
        cursor = conn.cursor()
        cursor.execute("select distinct [Kết quả kiểm tra trước sửa chữa] from VATTU")
        list_result_before_fixing = cursor.fetchall()  
        new_list_result_before_fixing = []
        for element in list_result_before_fixing:
            for item in element:
                list_result_before_fixing.append(item)
        conn.commit()
        conn.close()
        return list_result_before_fixing
    
    def get_list_handover_status(self):
        conn = sqlite3.connect("QLVT.db")
        cursor = conn.cursor()
        cursor.execute("select distinct [Tình trạng bàn giao đi sửa chữa]  from VATTU")
        list_handover_status = cursor.fetchall()  
        new_list_handover_status = []
        for element in list_handover_status:
            for item in element:
                new_list_handover_status.append(item)
        conn.commit()
        conn.close()
        return new_list_handover_status

    def get_list_serial_after_fixing(self):
        conn = sqlite3.connect("QLVT.db")
        cursor = conn.cursor()
        cursor.execute("select distinct [Số serial sau SC] from VATTU")
        list_serial_afer_fixing = cursor.fetchall()  
        new_list_serial_after_fixing = []
        for element in list_serial_afer_fixing:
            for item in element:
                new_list_serial_after_fixing.append(item)
        conn.commit()
        conn.close()
        return new_list_serial_after_fixing

    def get_list_result_after_fixing(self):
        conn = sqlite3.connect("QLVT.db")
        cursor = conn.cursor()
        cursor.execute("select distinct [Kết quả kiểm tra sau sửa chữa] from VATTU")
        list_result_after_fixing = cursor.fetchall()  
        new_list_result_after_fixing = []
        for element in list_result_after_fixing:
            for item in element:
                new_list_result_after_fixing.append(item)
        conn.commit()
        conn.close()
        return new_list_result_after_fixing
      

    def get_path(self):  #lấy đường dẫn để xuất file
        file = askdirectory(title= "Choose destination")
        self.var_en_directory.set(file)
        
    def save_to_file(self):  #Lưu file 
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
            # if selected_item == []:
            #     messagebox.showinfo("Thông báo", "Vui lòng click một chọn bản ghi trong bảng kết quả hoặc nhấn phím Ctr + click để chọn nhiều bản ghi!")
            # elif selected_item != ():
            #     if self.en_choose_file_type.get() == "csv":
            #         f = open("{}/{}.csv".format(self.en_directory.get(), self.en_name_file.get()), "w", newline='')
            #         writer = csv.writer(f, delimiter=',')
            #         for i in range(0, len(selected_item)):
            #             item = self.treeview.item(selected_item[i])
            #             record = list(item.values())
            #             writer.writerow(record[2])
                   
                    
        
                    
                











