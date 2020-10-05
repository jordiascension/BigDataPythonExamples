# -*- coding: utf-8 -*-
'''
Created on 05-oct-2020

@author: jordi
'''

#ordena l'array de forma ascendent
x = ['Python', 'programming', 'is', 'awesome!']
print(sorted(x))

#ordena l'array de forma descendent i el posa en minúscules
print(sorted(x, key=lambda arg: arg.lower()))

#filtra els valors del array amb paraules més petites que 8 caracters
print(list(filter(lambda arg: len(arg) < 8, x)))

#map sempre retorna el mateix número d'elements
#que l'array original i executa la lambda expression
print(list(map(lambda arg: arg.upper(), x)))

#reduce no retorna un nou iterable, sinó utilitza la funció
#cridada, per redui l'iterable en un sol valor
from functools import reduce
print(reduce(lambda val1, val2: val1 + val2, x))
