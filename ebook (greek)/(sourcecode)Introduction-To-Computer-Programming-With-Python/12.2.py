from tkinter import *

class Application():
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.qbutton = Button(frame, text='Quit', fg='red', command=root.destroy)
        self.qbutton.pack(side=LEFT)
        self.mbutton = Button(frame, text='Message', command=self.printMessage)
        self.mbutton.pack(side=LEFT)
    def printMessage(self):
        print('Hello, World!')

root = Tk()
app = Application(root)
root.mainloop()





        





