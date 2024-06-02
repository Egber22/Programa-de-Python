#leer un entero "n" del teclado
n = int(input())
#crear una lista
lista = []
#en las n lineas siguientes, leer un entero
for i in range(n):
    numero = int(input())
    lista.append(numero)

#imprimir la media de los enteros leidos

print( sum(lista) / n )