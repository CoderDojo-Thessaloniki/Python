from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

listbox = Listbox(root)
listbox.pack()

for i in range(20):
    listbox.insert(END, i)

listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

root.mainloop()


