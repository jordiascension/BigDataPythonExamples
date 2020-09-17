# -*- coding: utf-8 -*-

'''
Created on 14-sep-2020

@author: jordi
'''


'''
Introducción
Pandas es una librería de python destinada al análisis de datos, que proporciona unas estructuras de datos flexibles y 
que permiten trabajar con ellos de forma muy eficiente. Pandas ofrece las siguientes estructuras de datos:

Series: Son arrays unidimensionales con indexación(arrays con índice o etiquetados), similar a los diccionarios. 
Pueden generarse a partir de diccionarios o de listas.
 
DataFrame: Son estructuras de datos similares a las tablas de bases de datos relacionales como SQL.
 
Panel, Panel4D y PanelND: Estas estructuras de datos permiten trabajar con más de dos dimensiones. Dado que es 
algo complejo y poco utilizado trabajar con arrays de más de dos dimensiones no trataremos los paneles 
en estos tutoriales de introdución a Pandas.

Para ver los ejemplos que vamos a mostrar en este tutorial y en el resto relacionados con la librería de Pandas,
es necesario descargarnos esta librería (y la librería de Numpy). Para ello lo podemos descargar a través del
repositorio de paquetes PyPi (con pip) de la siguiente manera:

$ pip install pandas
'''
 
import pandas as pd


# El primer ejemplo que vamos a poner va a ser el de definir una estructura de datos "Series"
# que como ya comentamos es un array de datos unidimensional con indexaci�n. Las "Series" se definen
# de la siguiente manera:
spanishPlayers = pd.Series(
    ['Casillas', 'Ramos', 'Pique', 'Puyol', 'Capdevila', 'Xabi Alonso', 'Busquets', 'Xavi Hernandez', 'Pedrito',
     'Iniesta', 'Villa'], index=[1, 15, 3, 5, 11, 14, 16, 8, 18, 6, 7])
print("Spanish Football Players: \n%s" % spanishPlayers)

#sino ponemos índices el nos lo crea empezando desde 0
spanishPlayers = pd.Series(
    ['Casillas', 'Ramos', 'Pique', 'Puyol', 'Capdevila', 'Xabi Alonso', 'Busquets', 'Xavi Hernandez', 'Pedrito',
     'Iniesta', 'Villa'])
print("Spanish Football Players: \n%s" % spanishPlayers)

#Creación de una estructura de datos a partir de un diccionario (pares clave-valor), si lo realizamos a partir
#de una lista, el índice se generará automáticamente
dictPlayers = {1: 'Casillas', 15: 'Ramos', 3: 'Pique', 5: 'Puyol', 11: 'Capdevila', 14: 'Xabi Alonso',
               16: 'Busquets', 8: 'Xavi Hernandez', 18: 'Pedrito', 6: 'Iniesta', 7: 'Villa'}
players2series = pd.Series(dictPlayers)
# Insert new player
players2series[10] = 'Cesc'
print("Spanish Football Players through dictionary: \n%s" % players2series)

#Creación de un diccionario con los datos de las criptomoneds
dictCripto = {10881.55: 'Bitcoin', 361.5095: 'Ethereum',
              0.2408: 'XRP', 72.11:"Dash"}
Criptoseries = pd.Series(dictCripto)
print("Cripto Values through dictionary: \n%s" % Criptoseries)

#Los DataFrame es una estructura de datos similar a una tabla de base de datos
#o una tabla de excel
spanishPlayersDF = pd.DataFrame(
    {
        'name': ['Casillas', 'Ramos', 'Pique', 'Puyol', 'Capdevila', 'Xabi Alonso', 'Busquets', 'Xavi Hernandez',
                 'Pedrito', 'Iniesta', 'Villa'],
        'demarcation': ['Goalkeeper', 'Right back', 'Centre-back', 'Centre-back', 'Left back', 'Defensive midfield',
                        'Defensive midfield', 'Midfielder', 'Left winger', 'Right winger', 'Centre forward'],
        'team': ['Real Madrid', 'Real Madrid', 'FC Barcelona', 'FC Barcelona', 'Villareal', 'Real Madrid',
                 'FC Barcelona', 'FC Barcelona', 'FC Barcelona', 'FC Barcelona', 'FC Barcelona']
    }, columns=['name', 'demarcation', 'team'], index=[1, 15, 3, 5, 11, 14, 16, 8, 18, 6, 7]
)

print(spanishPlayersDF);