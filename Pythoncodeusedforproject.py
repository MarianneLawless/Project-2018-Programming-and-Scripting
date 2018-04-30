# Let us dive into building of our ML project. We will be using Python to understand and train our model. Numpy, Pandas and SciKit Learn are some of the inbuilt libraries in Python.

import numpy as np

import pandas as pd

import matlotlib.pyplot as plt
import matplotlib.pyplot as pl
from sklearn.svm import SVC
 from sklearn.neighbors import KNeighborsClassifier
 from sklearn.esemble import RandomForestClassifier
 from sklearn.linear_model import LogisticRegression
 from sklearn.metrics import accuracy_score
 # Iris dataset is already available in SciKit Learn library and we can directly import it with the following code: 

from sklearn import datasets

In [17]: iris = datasets.load_iris()

In [18]: iris_data= iris.data

In [19]: iris_data = pd.DataFrame(iris_data, columns= iris.feature_names)

iris_data.head()
 sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
In [23]: iris.target_names
Out[23]:
array(['setosa', 'versicolor', 'virginica'],
      dtype='<U10')

In [24]: print (iris_data.shape)
(150, 4)
In [25]: iris_data.describe()
Out[25]:
       sepal length (cm)  sepal width (cm)  petal length (cm)  \
count         150.000000        150.000000         150.000000
mean            5.843333          3.054000           3.758667
std             0.828066          0.433594           1.764420
min             4.300000          2.000000           1.000000
25%             5.100000          2.800000           1.600000
50%             5.800000          3.000000           4.350000
75%             6.400000          3.300000           5.100000
max             7.900000          4.400000           6.900000

       petal width (cm)
count        150.000000
mean           1.198667
std            0.763161
min            0.100000
25%            0.300000
50%            1.300000
75%            1.800000
max            2.500000

In [26]: import seaborn as sns
sns.boxplot(dat = iris_data,width=0.5,fliersize=5)









