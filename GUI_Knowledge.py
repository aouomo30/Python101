from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI = Tk()
GUI.title('โปรแกรมอธิบายคำสั่งใน EP.2')
GUI.geometry ('400x400')

L1 = Label(GUI,text='โปรแกรมอธิบายคำสั่งใน EP.2',font=('JasmineUPC',30),fg='blue')
L1.place(x=30,y=20)

def Button1():
    text = 'กำหนดค่าขนาดหน้าต่างโปรแกรม'
    
    messagebox.showinfo('geometry',text)
           
FB1 = Frame(GUI) #คล้ายกระดาน หรือ Contrainer ถ้าไม่ใส่ frame ปุ่มจะเล็ก
FB1.place(x=130,y=70)

s = ttk.Style()
s.configure('my.TButton', font=('JasmineUPC',20),foreground='blue')
B1 = ttk.Button(FB1,text='geometry',style='my.TButton',command=Button1)


#B2.pack(ipadx=20,ipady=10) # .pack() ทำให้ปุ่มอยู่ตรงกลาง ด้านบนหน้าจอ
B1.pack(ipadx=10,ipady=10)


def Button2():
    s1 = ttk.Style()
    s1.configure('TMessageBox.TLabel',font=('JasmineUPC',20))
  #  text = 'กำหนดให้ปุ่มอยู่ตรงกลาง ด้านบนหน้าจอ'
    messagebox.showinfo(message='กำหนดให้ปุ่มอยู่ตรงกลาง ด้านบนหน้าจอ',title='pack',parent=GUI)

FB2 = Frame(GUI) #คล้ายกระดาน หรือ Contrainer ถ้าไม่ใส่ frame ปุ่มจะเล็ก
FB2.place(x=130,y=130)
            
B2 = ttk.Button(FB2,text='pack',style='my.TButton',command=Button2)
B2.pack(ipadx=10,ipady=10)

def Button3():
    text = 'กำหนดกรอบครอบปุ่ม ไม่ให้ปุ่มมีขนาดเล็ก'
    messagebox.showinfo('Frame',text)

FB3 = Frame(GUI) #คล้ายกระดาน หรือ Contrainer ถ้าไม่ใส่ frame ปุ่มจะเล็ก
FB3.place(x=130,y=190)
            
B3 = ttk.Button(FB3,text='Frame',style='my.TButton',command=Button3)
B3.pack(ipadx=10,ipady=10)

def Button4():
    text = 'ขยาย pad ด้านข้าง ซ้าย ขวา'
    messagebox.showinfo('ipadx',text)

FB4 = Frame(GUI) #คล้ายกระดาน หรือ Contrainer ถ้าไม่ใส่ frame ปุ่มจะเล็ก
FB4.place(x=130,y=250)
            
B4 = ttk.Button(FB4,text='ipadx',style='my.TButton',command=Button4)
B4.pack(ipadx=10,ipady=10)

def Button5():
    text = 'ขยาย pad ด้าน บน ล่าง'
    messagebox.showinfo('ipady',text)

FB5 = Frame(GUI) #คล้ายกระดาน หรือ Contrainer ถ้าไม่ใส่ frame ปุ่มจะเล็ก
FB5.place(x=130,y=310)
            
B5 = ttk.Button(FB5,text='ipady',style='my.TButton',command=Button5)
B5.pack(ipadx=10,ipady=10)

GUI.mainloop()
