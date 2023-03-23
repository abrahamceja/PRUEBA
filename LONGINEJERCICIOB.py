from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.geometry("300x400")
root.title("entry box")

contraseñax= StringVar()
contraseñacx= StringVar()
botonhx=IntVar()
botonmx=IntVar()
botonTx=IntVar()
nombrex=StringVar()


def confirmacion():
    if botonTx.get()==1:
        if contraseñax.get()==contraseñacx.get():
            print(f'SESION INICIADA')
            framePrincipal.config(bg="#3ADF06")
            nombre.config(framePrincipal, bg="#3ADF06")

        else:
            print(f'CONTRASEÑA INCORRECTA')
            framePrincipal.config(bg="#a0a0a0")
    else:
        print(f'PARA INICIAR SESION TIENE QUE ACEPTAR LOS TERMINOS Y CONDICIONES')


framePrincipal = Frame(root, bg="#a0a0a0")
framePrincipal.pack(fill="both", expand=1)

imggiggypuf=Image.open("Jigglypuff_Sing.webp")
imagensing=imggiggypuf.resize((150,100))
imag=ImageTk.PhotoImage(imagensing)

mititulo=Label(framePrincipal, image=imag)
mititulo.place(x=70, y=10)

title = Label(framePrincipal, text="LOG IN", bg="#ffff00", font=("Roboto", 20, "bold")).place(x=100,y=130)
nombre = Label (framePrincipal, text="NOMBRE", bg="#a0a0a0").place(x=30, y=190)
contraseña = Label (framePrincipal, text="CONTRASEÑA", bg="#a0a0a0").place(x=30, y=220)
contraseñaconfirmada = Label (framePrincipal, text="CONFIRMAR\nCONTRASEÑA", bg="#a0a0a0").place(x=30, y=250)

nombretex = Entry(framePrincipal, textvariable=nombrex).place(x=140, y=190)
contraseñatexx = Entry(framePrincipal, textvariable=contraseñax).place(x=140, y=220)
contraseñactexx = Entry(framePrincipal, textvariable=contraseñacx).place(x=140, y=260)

botonh = Checkbutton(framePrincipal,text="HOMBRE",variable=botonhx,bg="#ff8000" ).place(x=60, y=290)
botonm = Checkbutton(framePrincipal,text="MUJER", variable=botonmx,bg="#ff8000" ).place(x=170, y=290)
botonT = Checkbutton(framePrincipal,text="ACEPTO TERMINOS Y CONDICIONES",variable=botonTx, bg="#ff8000" ).place(x=40, y=320)

boton=Button(framePrincipal, text="INICIAR SESION", bg="#408080", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=20, height=2, command=confirmacion).place(x=70, y=350)


root.mainloop()