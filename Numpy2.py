# Marianne Lawless 2018 Project
# Iris data Set 

import numpy

mydata = numpy.genfromtxt("data/iris2.csv" ,delimiter=",")

fcol = mydata[:,0]
meanfcol = numpy.mean(mydata[:,0])

print("Average of first column is : ", meanfcol)





