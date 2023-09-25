import tkinter as tk
#Función para encontrar el elemento mayoritario presente en una lista dada
def findMajorityElement(caracter):
    #Crea un 'HashMap' vacio
    d= {}
    #Almacena la frecuencia de cada elemento en un diccionario
    for char in caracter:
        d[char]=d.get(char,0)+1
        #Devuelve el elemento si su cuenta es mayor que 'n/2'
    for key, value in d.items():
        if value > len(caracter)/2:
            return key
    return "No hay"
def calcular():
    data_str= data_entry.get()
    caracter=data_str.split(',')
#if __name__ == '__main__':
    #Crea un array vacio 
 #   nums = []
    #Preguntar cuantos datos tenemos
  #  datos_num=int(input("Cuantos datos tienes?"))
    #Solicitar datos y agregarlos al array
   # for i in range(datos_num):
    #    dato=int(input("Ingrese el dato #{}: ".format(i+1)))
     #   nums.append(dato)
    #Encontrar el elemento mayoritario en el array 
    #Suposicion #: Entrada valida (el elemento mayoritario esta presente)
    result = findMajorityElement(caracter)
    if result != "No hay":
            result_label.config(text=f'El elemento Mayoritario es "{result}"')
    else:
            result_label.config(text='El elemento mayoritario no existe')
ventana=tk.Tk()
ventana.geometry("300x300")
ventana.title("Elemento Mayoritario")
data_label=tk.Label(ventana, text="Introduce los caracteres separados en comas: ")
data_label.pack()
date_entry=tk.Entry(ventana,width=50)
date_entry.pack()
calculate_button=tk.Button(ventana, text="Calcular",command=calcular)
calculate_button.pack()
result_label=tk.Label(ventana,text="")
result_label.pack()
ventana.mainloop()
#Modificar el programa que tenga un array vacio
#Que pregunte cuantos datos tenemos
#Dependiendo el # de datos sea lo que aadmita en el array
#Los datos deben introducirse separados por comas
#Pedir que ingrese caracteres (ingresar una palabra y buscar el numero mayoritario, caracter)