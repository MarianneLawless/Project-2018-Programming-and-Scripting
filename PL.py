# Marianne Lawless
# Project Iris Data Set
# This is a single csvfile representing the Sepal Width of the Iris data set

import numpy
mydata = numpy.genfromtxt("data/PL.csv" ,delimiter=",")

mean = numpy.mean(mydata)
# 5.8

max = numpy.max(mydata)
# 7.9

min = numpy.min(mydata)
# 4.30

sum = numpy.sum(mydata)
# 870.29




