from tkinter import *
from tkinter import ttk
import tkinter as tk

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
btnInsert=Button(pestana1,text="Agregar Bebida").pack()

panel.add(pestana1,text="ALTA DE BEBIDA")
panel.add(pestana2,text="BAJA DE BEBIDA")
panel.add(pestana3,text="CONSULTA DE BEBIDAS")
panel.add(pestana4,text="ACTUALIZACION DE BEBIDA")
panel.add(pestana5,text="OPERACIONES DE BEBIDA")
ventana.mainloop()