from tkinter import *

# Configuración de la raíz.
root = Tk()
root.title('Test tk')
root.resizable(1,1)
root.iconbitmap('@/home/jdg/git/Course-Python3/15_src/hola.xbm')

# # Variables dinámicas.
# texto = StringVar()
# texto.set('Un nuevo texto')
#
# Label(root, text='Hola mundo!').pack(anchor='nw')
#
# label = Label(root, text='Otra etiqueta!')
# label.pack(anchor='center')
# label.config(bg='green', fg='blue', font=('Verdana', 24))
# label.config(textvariable=texto)
#
# Label(root, text='Ultima etiqueta!').pack(anchor='se')

imagen = PhotoImage(file='/home/jdg/git/Course-Python3/15_src/banana.gif')
Label(root, image=imagen, bd=0).pack(side='left')

root.mainloop()
