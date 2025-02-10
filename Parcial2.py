## Niedferson Vargas, Parcial Numero 2

##1. Desarrollar un programa que determine si en una lista no existen elementos repetidos (dos ejemplos)

lista = [1, 2, 3, 4, 4, 5]
for n in lista:
    m = lista.count(n)
    if m >= 2:
        print(f"{n} Esta repetido en esta lista")
    else:
        print("Este numero no esta repetido ")
    
##Desarrollar un programa que determine si en una lista se enceuntra una cadena de caracteres con dos o mas vocales. 
## Si la cadena existe debe imprimirla y si no existe debe imprimir "No existe"

listax = ["Empanada", "ey"]
vocales = ["a","e","i","o","u","A","E","I","O","U"]



##Desarrollar un programa que dadas dos listas determine que elementos tiene la primera lista que no tenga la segunda lista

lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 5]

##edsarrolar un algoritmo que calcule el promedio de un arreglo de reales

Prueba = [5,5,5]
for g in Prueba:
    g = g + g + g
    operacion = g / len(Prueba)
    print(operacion)
## desarrolar un algoritmo que determine la mediana de un arreglo de enteros. La mediana es el numero que queda en la mitad del arreglo despues de ser ordenado 