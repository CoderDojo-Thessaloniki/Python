from tkinter import *

def testing():
    print('Just testing!')

root = Tk()
root.title('Παράθυρο με μενού')
menu = Menu(root)
root.config(menu = menu)
yearmenu = Menu(menu)
menu.add_cascade(label = 'Έτος', menu = yearmenu)
yearmenu.add_command(label = '2015', command = testing)
yearmenu.add_command(label = '2016', command = testing)
yearmenu.add_separator()
yearmenu.add_command(label = 'Έξοδος', command = root.destroy)
helpmenu = Menu(menu)
menu.add_cascade(label = 'Βοήθεια', menu = helpmenu)
helpmenu.add_command(label = 'About...', command = testing)

root.mainloop()


        





