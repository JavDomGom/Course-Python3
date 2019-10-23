from tkinter import *

# Configuración de la raíz.
root = Tk()
root.title('Test tk')
root.resizable(1,1)
root.iconbitmap('@/home/jdg/git/Course-Python3/15_src/hola.xbm')

label = Label(root, text='Nombre')
label.grid(row=0, column=0, sticky='w', padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify='right', state='normal')

label2 = Label(root, text='Contraseña')
label2.grid(row=1, column=0, sticky='w', padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify='center', show='*')

root.mainloop()
