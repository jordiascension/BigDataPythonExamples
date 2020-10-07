# -*- coding: utf-8 -*-
'''
Created on 05-oct-2020

@author: jordi
'''


#Creem una connexió a Spark mitjançant un SparkContext
from pyspark import SparkContext
sc = SparkContext()

#Llegir el fitxer dunwich.txt en sistema operatiu Windows
miRDD = sc.textFile("llibres/dunwich.txt")

#inline funtions
#Obtenim les frases amb més de 71 caràcters
def miFuncion(record):
    if len(record) > 71:
        return True 
    else:
        return False

#filtra el llibre amb la funció mifuncion
nuevoRDD = miRDD.filter(miFuncion)

print('El nombre de frases amb més 71 caràcters és ' + str(nuevoRDD.count()))

#mostrar les dades
i = 0
for valor in nuevoRDD.collect():
    i = i + 1
    print(str(i) + ". " + valor)

