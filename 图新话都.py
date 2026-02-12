from tkinter import *
root = Tk()
def callbutton1():
    for i in listb.curselection():
        listb2.insert(0,listb.get(i))

def callbutton2():
    for i in listb2.curselection():
        listb2.delete(i)

li =['C','Python','cat','holy','shit']
listb =Listbox(root)
listb2=Listbox(root)
for items in li:
    listb.insert(0,items)
listb.grid(row=0,column=0,rowspan=2)
b1=Button(root,text ='添加>>',command=callbutton1,width=20)
b2=Button(root,text='删除<<',command=callbutton2,width=20)
b1.grid(row=0,column=1,rowspan=2)
b2.grid(row=1,column=1,rowspan=2)
listb2.grid(row=0,column=2,rowspan=2)
root.mainloop()