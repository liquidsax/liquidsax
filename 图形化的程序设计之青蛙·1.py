from tkinter import *
win =Tk()
win.title("我的窗口")
lab1 = Label(win,text = '你好',anchor ='nw')
lab1.pack()
lab2 = Label(win,bitmap= 'question')
lab2.pack()
bm = PhotoImage(file = r'C:\Users\lenovo\Pictures\OIP-C.jpg') 
lab3=Label(win,image=bm)
lab3.bm=bm
lab3.pack()
win.mainloop()