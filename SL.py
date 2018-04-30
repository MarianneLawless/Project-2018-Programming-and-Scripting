# Marianne Lawless
# Project Iris Data Set
# This is a single csvfile representing the Sepal Lenght of the Iris data set

import numpy as np
mydata = numpy.genfromtxt("data/SL.csv" ,delimiter=",")

mean = numpy.mean(mydata)
# 5.8 

max = numpy.max(mydata)
# 7.9

min = numpy.min(mydata)
# 4.30

sum = numpy.sum(mydata)
# 870.299




