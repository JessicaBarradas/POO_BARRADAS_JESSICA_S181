#Hacer un array vacio que se va a llenar con datos que solicite el programa
#Pedir numero de datos en una ventana
#Ingresar dtos individuales en una ventana
#Imprimer datos aleatorios en una ventana
from random import randrange
#Funcion de utilidad para intercambiarr elementos 'A[i]' y 'A[j]' en una lista
def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp
    #Funcion para barajar una lista 'A'
def shuffle(A):
    #Lista de lectura desde el inicio mas bajo hasta el mas alto
    for i in range (len(A)-1):
        #Genera un numero aleatorio 'j' tal que 'i<=j<n'
        j=randrange(i,len(A))
        #intercambiar el elemento actual con el indice generado aleatoriamente
        swap(A,i,j)
if __name__ == '__main__':
    A=[1,2,3,4,5,6]
    shuffle(A)
    #Imprime la lista barajada
    print(A)