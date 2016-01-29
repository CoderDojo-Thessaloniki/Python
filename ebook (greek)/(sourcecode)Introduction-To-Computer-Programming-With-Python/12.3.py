from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=200)
canvas.pack()
canvas.create_line(0, 0, 200, 200)
canvas.create_rectangle(50, 50, 100, 100, fill = 'yellow')
canvas.create_rectangle(100, 100, 150, 150, fill = 'blue')

root.mainloop()




        





