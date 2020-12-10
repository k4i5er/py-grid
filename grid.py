from tkinter import Tk, LEFT, RIGHT, IntVar, BooleanVar, StringVar
from tkinter.ttk import Frame, Label, Entry, Button, Combobox, Radiobutton, Checkbutton


class User():
  # Atributos

  # Métodos


def show_fb():
    if fb.get():
        lbl_fb_user.grid(row=4, column=0)
        entry_fb_user.grid(row=4, column=1)
    else:
        lbl_fb_user.grid_remove()
        entry_fb_user.grid_remove()


def show_value():
    if chk_v1.get():
        print(f'Tienes Twitter')
    if chk_v2.get():
        print(f'Tienes Instagram')
    if chk_v3.get():
        print(f'Tienes Tik Tok')


root = Tk()
root.geometry('350x300')
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
Label(root, text='Otras redes sociales que tengas (Selecciona todas las que apliquen)').grid(
    row=5, column=0, columnspan=3)
chk_v1 = StringVar()
chk_v2 = StringVar()
chk_v3 = StringVar()
Checkbutton(root, text='Twitter', variable=chk_v1,
            command=show_value).grid(row=6, column=0)
Checkbutton(root, text='Instagram', variable=chk_v2,
            command=show_value).grid(row=7, column=0)
Checkbutton(root, text='Tik Tok', variable=chk_v3,
            command=show_value).grid(row=8, column=0)
btn_x = Button(root, text='Guardar registro')
btn_x.grid(row=9, column=0, columnspan=3)
root.mainloop()
