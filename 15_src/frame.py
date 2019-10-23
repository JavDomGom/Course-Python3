from tkinter import *

root = Tk()

root.title('Test tk')
root.resizable(1,1)
root.iconbitmap('@/home/jdg/git/Course-Python3/15_src/hola.xbm')

frame = Frame(root, width=480, height=320)
frame.pack()
frame.config(cursor='pirate')
frame.config(bg='lightblue')
frame.config(bd=25)
frame.config(relief='sunken')
frame.pack(side=RIGHT)   # a la derecha al medio
frame.pack(anchor=SE)    # sudeste, abajo a la derecha

root.config(cursor='arrow')
root.config(bg='blue')
root.config(bd=15)
root.config(relief='ridge')

root.mainloop()
