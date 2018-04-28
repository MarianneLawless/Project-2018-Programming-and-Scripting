
import numpy # Read data file into array 

data = numpy.genfromtxt('data/iris.csv', delimiter=',')

firstcol = data[:,0]
meanfirst = numpy.mean(data[:,0])

print ("Average of first Column is: ", meanfirst)