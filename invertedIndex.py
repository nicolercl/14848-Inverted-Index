#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sys
from pyspark import SparkContext, SparkConf

conf = SparkConf()
sc = SparkContext.getOrCreate(conf=conf)

sc._jsc.hadoopConfiguration().set('my.mapreduce.input.fileinputformat.input.dir.recursive', 'True')

stopList = ["they", "she", "he", "it", "the", "as", "is", "and"]


# In[9]:


# (term, filename), count -> aggregate count -> term, [(filename, count)] -> aggregate (filename, count) list
postLists = sc.wholeTextFiles("Data/*/*").flatMap(lambda file: [((term, file[0]), 1) for term in file[1].lower().split(" ") if term not in stopList])    .reduceByKey(lambda a, b: a+b)    .map(lambda x: (x[0][0], [(x[0][1], x[1])]))    .reduceByKey(lambda a, b: a+b)    .saveAsTextFile("output/")




