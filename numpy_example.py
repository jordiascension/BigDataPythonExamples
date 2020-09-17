# -*- coding: utf-8 -*-
'''
Created on 16-sep-2020

@author: jordi
'''
#Numpy es un paquete que provee a Python con arreglos multidimensionales de alta eficiencia y 
#diseñados para cálculo científico.
#Un array puede contener:
#tiempos discretos de un experimento o simulación.
#señales grabadas por un instrumento de medida.
#pixeles de una imagen, etc.
import numpy as np

b = np.array([[0, 1, 2], [3, 4, 5]]) # arreglo 2 x 3
print(b)

#mostrar el número de dimensiones
print('El número de dimensiones es ' + str(b.ndim))

#longitud de las dimensiones
print('la longitud de las dimensiones es ' + str(b.shape))

#generar un arreglo de 0 a 10
a = np.arange(10)
print(a)

#cortar arreglo
print(a[2:9])

#Si copiamos una lista en Python... si modificamos la copia, no se modifica la lista originalmente copiada:
a = [1, 2, 3]
b = a[:]
print(b)
b[0] = 100
print(b)
print(a)


#Si trabajamos con arreglos de NumPy, el comportamiento es diferente (cuando copiamos, en realidad,
#estamos haciendo una vista al objeto original, apuntamos al mismo objeto):
a = np.array([1, 2, 3])
b = a[:]
print(b)
b[0] = 100
print(b)
print(a)

#Sumar todos los elementos de un array
x = np.array([1, 2, 3, 4])
print(x.sum()) # np.sum(x)   

#Cálculo de media aritmética
x = np.array([1, 2, 3, 1])
print(x.mean())

#Cálculo desviación estandard
x = np.array([1, 2, 3, 1])
print(x.mean())

#max and min
print(x.max())
print(x.min())

print(np.random.rand(5, 5)) # números aleatorios uniformes [0,1]


