from tkinter import *

root = Tk()

Label(root, text='Ετικέτα-1:').grid(row=0, sticky=W)
Label(root, text='Ετικέτα-2:').grid(row=1, sticky=W)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

cb = Checkbutton(root, text='Επιλογή')
cb.grid(row=2, columnspan=2, sticky=W)

root.mainloop()


