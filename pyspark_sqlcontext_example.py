# -*- coding: utf-8 -*-
'''
Created on 06-oct-2020

@author: jordi
'''
from pyspark.sql import SparkSession


#Initialization of a Spark Session
sc = SparkSession.builder.appName("PySparkExample")\
    .config ("spark.sql.shuffle.partitions", "50") \
    .config("spark.driver.maxResultSize","5g") \
    .config ("spark.sql.execution.arrow.pyspark.enabled", "true")\
    .getOrCreate()

#JSON
dataframe = sc.read.json('dataset/nyt2.json')

dataframe.show(10)

# Select Operation

dataframe.select("author").show(10) #Show all entries in title column

dataframe.select("author", "title", "rank", "price").show(10)  #Show all entries in title, author, rank, price columns

# Show rows with specified authors if in the given options

dataframe [dataframe.author.isin("John Sandford","Emily Giffin")].show(5)

# Show author and title is TRUE if title has " THE " word in titles

dataframe.select("author", "title", dataframe.title.like("% THE %")).show(15)

dataframe.select("author", "title", dataframe.title.startswith("THE")).show(5)

dataframe.select("author", "title", dataframe.title.endswith("NT")).show(5)


dataframe.select(dataframe.author.substr(1, 6).alias("title")).show()

dataframe.select(dataframe.author.substr(1, 3).alias("title")).show(5)

dataframe.select(dataframe.author.substr(3, 6).alias("title")).show(5)

dataframe.select(dataframe.author.substr(1, 6).alias("title")).show(5)