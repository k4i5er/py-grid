from tkinter import Tk, LEFT, RIGHT, IntVar, BooleanVar, StringVar
from tkinter.ttk import Frame, Label, Entry, Button, Combobox, Radiobutton, Checkbutton, Notebook


# class User():
#   # Atributos

#   # Métodos

# Notebook: Widget que permite crear pestañas en un app

def save_record():
    if fb.get():
        # Deselecciona el Radiobutton
        rb_fb.state(['!selected'])

    else:
        # Deselecciona el Radiobutton
        rb_noFb.state(['!selected'])
    if chk_v1.get():
        # Deselecciona el Checkbutton
        chk_v1.set(0)


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


def delete_tab():
    ntbk_panel.forget(ntbk_panel.select())


root = Tk()
root.geometry('350x1080')

# Instanciamos a Notebook
ntbk_panel = Notebook(root)

frm_tab_userData = Frame(ntbk_panel)

lbl_name = Label(frm_tab_userData, text='Nombre')
lbl_name.grid(row=0, column=0)
entry_name = Entry(frm_tab_userData)
entry_name.grid(row=0, column=1)
lbl_lastname = Label(frm_tab_userData, text='Apellidos')
lbl_lastname.grid(row=1, column=0)
entry_lastname = Entry(frm_tab_userData)
entry_lastname.grid(row=1, column=1)
lbl_email = Label(frm_tab_userData, text='Correo electrónico')
lbl_email.grid(row=2, column=0)
entry_email = Entry(frm_tab_userData)
entry_email.grid(row=2, column=1)
lbl_fb = Label(frm_tab_userData, text='¿Cuentas con Facebook?')
lbl_fb.grid(row=3, column=0)
fb = BooleanVar()
rb_fb = Radiobutton(frm_tab_userData, text='Sí', variable=fb, value=True,
                    command=show_fb)
rb_fb.grid(row=3, column=1)
rb_noFb = Radiobutton(frm_tab_userData, text='No', variable=fb, value=False,
                      command=show_fb)
rb_noFb.grid(row=3, column=2)
lbl_fb_user = Label(frm_tab_userData, text='Usuario de Facebook')
entry_fb_user = Entry(frm_tab_userData)
lbl_other_socialnetworks = Label(
    frm_tab_userData, text='Otras redes sociales que tengas (Selecciona todas las que apliquen)')
lbl_other_socialnetworks.grid(
    row=5, column=0, columnspan=3)
chk_v1 = StringVar()
chk_v2 = StringVar()
chk_v3 = StringVar()
chk_tw = Checkbutton(frm_tab_userData, text='Twitter', variable=chk_v1,
                     command=show_value)
chk_tw.grid(row=6, column=0)
chk_insta = Checkbutton(frm_tab_userData, text='Instagram', variable=chk_v2,
                        command=show_value)
chk_insta.grid(row=7, column=0)
chk_tiktok = Checkbutton(frm_tab_userData, text='Tik Tok', variable=chk_v3,
                         command=show_value)
chk_tiktok.grid(row=8, column=0)
btn_x = Button(frm_tab_userData, text='Guardar registro', command=save_record)
btn_x.grid(row=9, column=0, columnspan=3)

frm_tab_userData.pack()

frm_tab_about = Frame(ntbk_panel)

lbl_about = Label(frm_tab_about, text='(c) Copyright 2020')
lbl_about.grid()
btn_delete_tab = Button(
    frm_tab_about, text='Eliminar esta pestaña...', command=delete_tab)
btn_delete_tab.grid()

frm_tab_about.pack()

# Agregar la pestaña al Notebook
ntbk_panel.add(frm_tab_userData, text='Datos de usuario')
ntbk_panel.add(frm_tab_about, text='Acerca de...')
# Selecciona la segunda pestaña
ntbk_panel.select(1)

ntbk_panel.pack()

root.mainloop()
