from tkinter import *

root = Tk()

cbfr = Frame(root)
cbfr.pack(side = TOP)
var = IntVar()
c = Checkbutton(cbfr, text = 'Eπιλογή', state = NORMAL, variable = var)
c.pack(side = LEFT)

root.mainloop()





