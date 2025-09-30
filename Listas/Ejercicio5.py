'''
Generar una lista con 100 números aleatorios entre 100 y 1000 
Calcular el promedio de los valores de la lista
Calcular el mayor y menor de los números
'''
import random

numeros = []
for i in range(100):
    aleatorio = random.randint(100,1000)
    numeros.append(aleatorio)

suma = 0 
for i in numeros:
    suma = suma + i

