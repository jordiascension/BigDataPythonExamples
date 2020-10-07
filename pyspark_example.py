# -*- coding: utf-8 -*-
'''
Created on 30-sep-2020

@author: jordi
'''

#Creem una connexió a Spark mitjançant un SparkContext
from pyspark import SparkContext
sc = SparkContext()

#Ara que tenim el context Creat, llavors creem una col·lecció de dades
#anomenada RDD (Resilent Distributed Dataset) amb tolerància a errades  
#i capaç d'operar en paral·lel.Aquest dataset
#es paral·lelitza en tot el clúster.
nums= sc.parallelize([1,2,3,4])

#apliquem una transformació de dades, amb una funció lambda, que
#retorna el cuadrat dels nombres de la matriu
squared = nums.map(lambda x: x*x).collect()

#mostrem el cuadrat per la pantalla
for num in squared:
    print('%i ' % (num))
    