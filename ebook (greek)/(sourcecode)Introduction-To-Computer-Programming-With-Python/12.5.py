from tkinter import *

root = Tk()

textfr = Frame(root)
textfr.pack(side = TOP)
text = Text(textfr, height = 5, width = 15, font = 'Arial 22')
text.pack(side = LEFT)
text.insert(END, 'Γεια σου κόσμε!')

root.mainloop()


