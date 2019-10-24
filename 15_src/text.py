from tkinter import *

# Configuración de la raíz.
root = Tk()
root.title('Test tk')
root.resizable(1,1)
root.iconbitmap('@/home/jdg/git/Course-Python3/15_src/hola.xbm')

texto = Text(root)
texto.pack()
texto.config(width=30, height=10, font=('Courier New', 12), padx=5, pady=5, selectbackground='red')

root.mainloop()
