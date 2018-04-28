# Marianne Lawless
#Programming and Scripting Project 2018
# Iris dataset downloaded from https://archive.ics.uci.edu/ml/datasets/iris

import numpy # Read data file into array 
data = numpy.genfromtxt('data/iris.csv', delimiter=',')

data[0] # Access the first line of data file#

(data[:,0]) # Access the first column of the data file ..Sepal Lenght

(data[:,1]) # Access the second column of the data file ..Sepal Width

(data[:,2]) # Access the third column of the data file ..Petal Lenght

(data[:,3]) # Access the fouth column of the data file ..Petal width


numpy.mean(data[:,0]) # Average / Mean of Sepal Lenght
5.8433333333333337

numpy.mean(data[:,1])
3.0540000000000003 # Average / Mean of Sepal Width

numpy.mean(data[:,2])
3.7586666666666662 # Average / Mean of Petal Lenght

numpy.mean(data[:,3]) # Average / Mean of Petal Width 
1.1986666666666668

numpy.max (data[:,0]) # Maximum lenght of the Sepal Lenght
7.9000000000000004

numpy.max (data[:,1]) # Maximum Lenght of the Sepal Width
4.4000000000000004

numpy.max (data[:,2])
6.9000000000000004 # Maximum Lenght of the Petal Lenght

numpy.max (data[:,3]) # Maximum Lenght of the Petal Width
2.5 

numpy.min (data[:,0])
4.2999999999999998 # Mininmum Lenght Sepal Lenght

numpy.min (data[:,1]) # Minimum Lenght Sepal Width
2.0

numpy.min (data[:,2]) # Minimum Lenght Petal Lenght
1.0

numpy.min (data[:,3]) # Minimum Lenght Petal Width
0.10000000000000001



















