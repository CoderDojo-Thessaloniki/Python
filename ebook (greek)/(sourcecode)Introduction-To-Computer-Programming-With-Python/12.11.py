from tkinter import *

def add_function():
    e3.insert(0, str(int(e1.get())+int(e2.get())))

def clear_entries():
    e1.delete(0,10)
    e2.delete(0,10)
    e3.delete(0,10)

root = Tk()

l1 = Label(root, text='1ος αριθμός:')
l1.grid(row=0, sticky=W)
e1 = Entry(root)
e1.grid(row=0, column=1)
l2 = Label(root, text='2ος αριθμός:')
l2.grid(row=1, sticky=W)
e2 = Entry(root)
e2.grid(row=1, column=1)
b1 = Button(root, text='Πρόσθεση', fg='navy', command=add_function)
b1.grid(row=2, sticky=W)
e3 = Entry(root)
e3.grid(row=2, column=1)
b2 = Button(root, text='Καθαρισμός', fg='navy', command=clear_entries)
b2.grid(row=3, sticky=W)

root.mainloop()


