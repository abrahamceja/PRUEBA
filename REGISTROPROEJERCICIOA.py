from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root=Tk()
root.title("EJERCICIO A")

#medoto
def registrar():

    print(f'\nProducto: {Producto.get()}\nSKU: {SKU.get()}')

    if(check_1.get()==1):
        print("Departamento: A")
    
    if(check_2.get()==1):
        print("Departamento: B")
    
    if(check_3.get()==1):
        print("Departamento: C")

    print(f'Proveedor: {Proveedor.get()}')

    if(check_4.get()==1):
        print("Idioma: Inglés")
    if(check_5.get()==1):
        print("Idioma: Español")

#variables
Producto = StringVar()
SKU = StringVar()
check_1 = IntVar()
check_2 = IntVar()
check_3 = IntVar()
Proveedor = StringVar()
check_4 = IntVar()
check_5 = IntVar()

ventanaPrincipal = Frame(root, bg="#a0a0a0")
ventanaPrincipal.grid()

#titulo del root
titulo = Label(ventanaPrincipal, text="Registro \n Productos", font=("Roboto",20,"bold"), bg="#a0a0a0", fg="white")
titulo.grid(row=1, column=1, padx=10, columnspan=3)

#imagen a desplegar
imgCar = Image.open("Jigglypuff_Sing.webp")
imagen = imgCar.resize((200,150))
imag = ImageTk.PhotoImage(imagen)

miTitulo = Label(ventanaPrincipal, image=imag)
miTitulo.grid(row=2, column=1, columnspan=3, rowspan=2, pady=10, padx=10)

#etiqueta producto
titulo = Label(ventanaPrincipal, text="Producto", font=("Roboto",10,"bold"), bg="#a0a0a0", fg="white")
titulo.grid(row=4, column=1, padx=10, pady=10)

textoProducto = Entry(ventanaPrincipal, font=("Roboto",10), textvariable=Producto).grid(row=4, column=2, padx=20, pady=10)

#etiqueta de sku
titulo = Label(ventanaPrincipal, text="SKU", font=("Roboto",10,"bold"), bg="#a0a0a0", fg="white")
titulo.grid(row=5, column=1, padx=10, pady=10)

textoSku = Entry(ventanaPrincipal, font=("Roboto",10), textvariable=SKU).grid(row=5, column=2, padx=20, pady=10)

#etiqueta Departamento
titulo = Label(ventanaPrincipal, text="Departamento", font=("Roboto",10,"bold"), bg="#a0a0a0", fg="white")
titulo.grid(row=6, column=1, padx=10, pady=10)

#checkbox 1
check1 = Checkbutton(ventanaPrincipal, text="A", bg="#a0a0a0", font=("Roboto",10, "bold"), fg="red", variable=check_1).grid(row=7, column=1)

#checkbox 2
check2 = Checkbutton(ventanaPrincipal, text="B", bg="#a0a0a0", font=("Roboto",10, "bold"), fg="red", variable=check_2).grid(row=7, column=2)

#checkbox 3
check3 = Checkbutton(ventanaPrincipal, text="C", bg="#a0a0a0", font=("Roboto",10, "bold"), fg="red", variable=check_3).grid(row=7, column=3)

#proveedor
titulo = Label(ventanaPrincipal, text="Proveedor", font=("Roboto",10,"bold"), bg="#a0a0a0", fg="white")
titulo.grid(row=8, column=1, padx=10, pady=10)

Lista = ttk.Combobox(ventanaPrincipal,values=["Chevrolet","Tesla","Ford","Nissan","Honda","Toyota","Mazda","Volkswagen"], state="readonly", textvariable=Proveedor).grid(row=8, column=2)

#idioma
titulo = Label(ventanaPrincipal, text="Idioma", font=("Roboto",10,"bold"), bg="#a0a0a0", fg="white")
titulo.grid(row=9, column=1, pady=10)

#checkbox 4
check4 = Checkbutton(ventanaPrincipal, text="EN", bg="#a0a0a0", font=("Roboto",10, "bold"), fg="red", variable=check_4).grid(row=10, column=1)

#checkbox 5
check5 = Checkbutton(ventanaPrincipal, text="SP", bg="#a0a0a0", font=("Roboto",10, "bold"), fg="red", variable=check_5).grid(row=10, column=2)

#boton REGISTRAR
boton1 = Button(ventanaPrincipal, text="REGISTRAR", font=("Roboto",10), command= registrar).grid(row=11, column=1, columnspan=3, pady=20)

root.mainloop()