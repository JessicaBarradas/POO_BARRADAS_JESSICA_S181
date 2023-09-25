import tkinter as tk
# Función para encontrar el elemento mayoritario presente en una lista de caracteres dada
def findMajorityElement(chars):
    # Crea un 'HashMap' vacío
    d = {}
    
    # Almacena la frecuencia de cada carácter en un diccionario
    for char in chars:
        d[char] = d.get(char, 0) + 1
        
    # Devuelve el carácter si su cuenta es mayor que 'n/2'
    for key, value in d.items():
        if value > len(chars) / 2:
            return key
        
    return "Ninguno"

# Función para manejar el botón de calcular
def calcular():
    data_str = data_entry.get()

    
    # Verificar si el elemento mayoritario está presente
    result = findMajorityElement(data_str)
    
    if result != "Ninguno":
        result_label.config(text=f'El elemento mayoritario es "{result}"')
    else:
        result_label.config(text='El elemento mayoritario no existe')

# Crear la ventana de Tkinter
window = tk.Tk()
window.geometry("500x150")
window.title("Encontrar Elemento Mayoritario")

# Etiqueta para ingresar los datos
data_label = tk.Label(window, text="Introduce los caracteres separados por comas:")
data_label.pack()

# Entrada de datos
data_entry = tk.Entry(window, width=50)
data_entry.pack()

# Botón para calcular
calculate_button = tk.Button(window, text="Calcular", command=calcular)
calculate_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(window, text="")
result_label.pack()

# Iniciar el bucle de Tkinter
window.mainloop()