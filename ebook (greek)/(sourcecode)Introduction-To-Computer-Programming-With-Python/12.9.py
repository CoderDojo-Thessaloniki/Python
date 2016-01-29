from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()

def getFunction():
    t = e.get()
    print(t)
def insertFunction():
    e.delete(0,10)
    print(e.insert(0, 'Hello'))
def clearFunction():
    e.delete(0,10)
    
b1 = Button(root, text = 'Εισαγωγή', width = 10, command = getFunction)
b1.pack()
b2 = Button(root, text = 'Εμφάνιση', width = 10, command = insertFunction)
b2.pack()
b3 = Button(root, text = 'Καθαρισμός', width = 10, command = clearFunction)
b3.pack()

root.mainloop()

