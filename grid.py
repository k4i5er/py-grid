from tkinter import Tk, LEFT, RIGHT, IntVar, BooleanVar
from tkinter.ttk import Frame, Label, Entry, Button, Combobox, Radiobutton


def show_fb():
    if fb.get():
        lbl_fb_user.grid(row=4, column=0)
        entry_fb_user.grid(row=4, column=1)
    else:
        lbl_fb_user.grid_remove()
        entry_fb_user.grid_remove()


root = Tk()
root.geometry('350x100')
Label(root, text='Nombre').grid(row=0, column=0)
Entry(root).grid(row=0, column=1)
Label(root, text='Apellidos').grid(row=1, column=0)
Entry(root).grid(row=1, column=1)
Label(root, text='Correo electrónico').grid(row=2, column=0)
Entry(root).grid(row=2, column=1)
Label(root, text='¿Cuentas con Facebook?').grid(row=3, column=0)
fb = BooleanVar()
Radiobutton(root, text='Sí', variable=fb, value=True,
            command=show_fb).grid(row=3, column=1)
Radiobutton(root, text='No', variable=fb, value=False,
            command=show_fb).grid(row=3, column=2)
lbl_fb_user = Label(root, text='Usuario de Facebook')
entry_fb_user = Entry(root)
btn_x = Button(root, text='Guardar registro')
btn_x.grid(row=5, column=0, columnspan=3)
root.mainloop()


# Nombre:              __________________
# Apellidos:           __________________
# Correo electrónico:  __________________
# ¿Cuentas con Facebook? o Si o No
# Usuario de Facebook: _________________
#            ___________________
#           | Guardar registro |
#            ------------------
