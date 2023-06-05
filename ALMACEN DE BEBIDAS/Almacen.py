from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorAlmB import *
#Creamos un objeto de tipo controlador
controlador = controladorBebi()
#Procedemos a guardar usuarios usando el metodo GuardarBebidas() del objeto controlador
def ejecutaInsert():
    controlador.insertarBebida(varNom.get(),varCla.get(),varMar.get(),varPre.get())
def ejecutaEliminarB():
    conf=messagebox.askyesno("ELIMINAR BEBIDA","¿Seguro que desea eliminar el usuario?")
    if (conf==True):
        try:
             controlador.EliminarBebida(Bedid.get())
        except sqlite3.OperationalError:
            messagebox.showerror("ERROR","Error en la consulta")
def ejecutaSelectB():
    Bebida= controlador.consultaBebida(Bedid.get())
    for beb in Bebida:
        cadena=str(beb[0])+" "+beb[1]+" "+beb[2]+" "+beb[3]+" "+str(beb[4])
    if(Bebida):
        textBed.insert("0.0",cadena)
    else:
        messagebox.showinfo("No encontrado", "Usuario no registrado en la BD")
def ejecutaConsultaBebi():
    consulta=controlador.consultarB()
    tabB.delete(*tabB.get_children())
    for BEBI in consulta:
        tabB.insert("",tk.END,text="",values=BEBI)
def ejecutaActualizar():
    rsBebida=controlador.consultaBebida(BebiID.get())
    if(rsBebida):
        controlador.actualizarB(BebiNom.get(),BebiCla.get(),BebiMar.get(),BebiPre.get())
    else:
        messagebox.showerror("ERROR","No hay usuario registrado en la BD")
def ejecutaCantidadMar():
    cantidadMar = controlador.cantidadBebidaMar(varCanM.get())
    
    txtCanM.delete("1.0", "end")
    for mar in cantidadMar:
        cadena = "La cantidad total de bebidas de la marca es: "+ str(mar[0])
    if(cantidadMar):
        txtCanM.insert("0.0", cadena)
    else:
        messagebox.showinfo("No encontrado", "Marca no registrada en la BD")

def ejecutaCantidadClas():
    cantidadClasi = controlador.cantidadBebidaClas(varClasB.get())
    
    txtClasB.delete("1.0", "end")
    for mar in cantidadClasi:
        cadena = "La cantidad total de bebidas por clasificación es: "+ str(mar[0])
    if(cantidadClasi):
        txtClasB.insert("0.0", cadena)
    else:
        messagebox.showinfo("No encontrado", "Marca no registrada en la BD")

def EjecutaProm():
    prome = controlador.Prome()
    
    txtPro.delete("1.0", "end")
    cadena = str(prome)
    if(prome):
        txtPro.insert("0.0", cadena)
    else:
        messagebox.showinfo("No encontrado", "Marca no registrada en la BD")


ventana=Tk()
ventana.title("Almacen de Bebidas")
ventana.geometry("650x300")
panel=ttk.Notebook(ventana)
panel.pack(fill="both",expand="yes")

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)
pestana5=ttk.Frame(panel)

#Pestana 1: Insertar Material
titulo=Label(pestana1,text="Alta de Bebida",fg="#8BD172",font=("Dongle",18)).pack()
#Nombre
varNom=tk.StringVar()
lblNom=Label(pestana1,text="Nombre: ").pack()
txtNom=Entry(pestana1,textvariable=varNom).pack()
#Clasificacion
varCla=tk.StringVar()
lblCla=Label(pestana1,text="Clasificacion: ").pack()
txtCla=Entry(pestana1,textvariable=varCla).pack()
#Marca
varMar=tk.StringVar()
lblMar=Label(pestana1,text="Marca: ").pack()
txtMar=Entry(pestana1,textvariable=varMar).pack()
#Precio
varPre=tk.StringVar()
lblPre=Label(pestana1,text="Precio: ").pack()
txtPre=Entry(pestana1,textvariable=varPre).pack()
#Boton
btnInsert=Button(pestana1,text="Agregar Bebida",command=ejecutaInsert).pack()
#Pestaña 2: Eliminar Bebida
titulo2 = Label(pestana2, text = "Eliminar Bebida", fg = "#D73F3F", font = ("Modern", 18)).pack()
Bedid=tk.StringVar()
idbed=Label(pestana2,text="ID de la Bebida: ").pack()
idtext=Entry(pestana2,textvariable=Bedid).pack()
btnBuscarBeb=Button(pestana2,text="Buscar",command=ejecutaSelectB).pack()
BedBuscar=Label(pestana2,text="Registrado: ",fg="#5DD73F",font=("Modern",15)).pack()
textBed=tk.Text(pestana2,height=5,width=52)
textBed.pack()
btnEliminar=Button(pestana2,text="Eliminar",command=ejecutaEliminarB).pack()
#Pestaña 3: Consultar todas las bebidas
titulo3=Label(pestana3,text="Consultar Materiales",fg="red",font=("Modern",18)).pack()
btnConsulta=Button(pestana3,text="Consultar",command=ejecutaConsultaBebi).pack()
#Tabla
columns=("IDBed","Nombre","Clasificacion","Marca","Precio")
tabB=ttk.Treeview(pestana3,columns=columns,show="headings")
tabB.column("IDBed",anchor=tk.W,width=30)
tabB.column("Nombre",anchor=tk.W,width=150)
tabB.column("Clasificacion",anchor=tk.W,width=150)
tabB.column("Marca",anchor=tk.W,width=150)
tabB.column("Precio",anchor=tk.W,width=150)
tabB.heading("IDBed",text="ID")
tabB.heading("Nombre",text="NOMBRE")
tabB.heading("Clasificacion",text="CLASIFICACION")
tabB.heading("Marca",text="MARCA")
tabB.heading("Precio",text="PRECIO")
tabB.pack()
#Pestaña 4: Actualizar Usuario
titulo4 = Label(pestana4, text = "Actualizar Bebida", fg = "#84A7E5", font = ("Modern", 18)).pack()
BebiID = tk.StringVar()
BebiNom = tk.StringVar()
BebiCla = tk.StringVar()
BebiMar = tk.StringVar()
BebiPre = tk.StringVar()
Bedidaid = Label(pestana4, text = "ID de Bebida: ").pack()
textid = Entry(pestana4, textvariable = BebiID).pack()
BebidaNom = Label(pestana4, text = "Escribe el nuevo nombre de Bebida: ").pack()
textNom = Entry(pestana4, textvariable = BebiNom).pack()
BebidaCla = Label(pestana4, text = "Escribe la nueva clasificacion: ").pack()
textCla = Entry(pestana4, textvariable = BebiCla).pack()
BebidaMar = Label(pestana4, text = "Escribe la nueva Marca: ").pack()
textMar = Entry(pestana4, textvariable = BebiMar).pack()
BebidaPre = Label(pestana4, text = "Escribe el nuevo precio: ").pack()
textPre = Entry(pestana4, textvariable = BebiPre).pack()
btnActualizar=Button(pestana4,text="Actualizar").pack()
#Pestaña 4: Operaciones
titulo5 = Label(pestana5, text = "Operaciones Basicas", fg = "#84A7E5", font = ("Modern", 18)).pack()
#Promedio Bebida
varPro=tk.StringVar()
lblPro=Label(pestana5,text="Precio promedio de Bebida: ").pack()
txtPro=Entry(pestana5,textvariable=varPro).pack()
btnCalcular=Button(pestana5,text="Calcular",command=EjecutaProm).pack()
#Cantidad bebida de una Marca
varCanM=tk.StringVar()
lblCanM=Label(pestana5,text="Cantidad de bebida por Marca: ").pack()
txtCanM=Entry(pestana5,textvariable=varCanM).pack()
btnMostrar=Button(pestana5,text="Mostrar",command=ejecutaCantidadMar).pack()
#Cantidad por clasificacion
varClasB=tk.StringVar()
lblClasB=Label(pestana5,text="Cantidad de bebida por Clasificacion: ").pack()
txtClasB=Entry(pestana5,textvariable=varClasB).pack()
btnMostrar1=Button(pestana5,text="Mostrar",command=ejecutaCantidadClas).pack()


panel.add(pestana1,text="ALTA DE BEBIDA")
panel.add(pestana2,text="BAJA DE BEBIDA")
panel.add(pestana3,text="CONSULTA DE BEBIDAS")
panel.add(pestana4,text="ACTUALIZACION DE BEBIDA")
panel.add(pestana5,text="OPERACIONES DE BEBIDA")

ventana.mainloop()