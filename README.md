**Project-2018-Programming-and-Scripting**
==========================================
<img src="https://image.ibb.co/g96qDc/gmitlogo.jpg" alt="gmitlogo" border="0" width=450 align="center">

# The programming Language used to assist in writing code for this project
Anaconda download is a great way to install Python and all of the common Python libraries on your computer. I recommend installing version 3.6, 64-bit. https://www.python.org/
## The following project concerns the well-known Fisher’s Iris data set
### Project Overview

The following project concerns the well-known Fisher's Iris data set. The project entails the researching of the data set, and then writing documnentation and code in the Python programmining language based on that research
I have broken down this project into several smaller tasks that are easier to solve, and plugged these together after they have been completed.
i have done this by using the following guidelines:

* Research background information about the data setand write a summary about it.
* Keep a list of references that I am using in completing this project.
* I have downloaded the data set and written some Python code to investigate it.
* I have also written code that I hace been using throughout this module and tested it on the Iris data set
* Summarise the data set by, calculating the maximum, minimum and mean of each column of data set. I have imported *numpy*
to assist with these calculations.
* Wtite a summary of my investigations
* Included supporting tables and graphics of which I have used.

# Iris data set

## What is the famous iris data set, and how does it relate to machine learning.

First of all lets have a look at what I mean by machine learning.
Machine learning is a method of data analysis that automates analytical model building. It is a branch of artificial intelligence based on the idea that systems can learn from data, identify patterns and make decisions with minimal human intervention.

Most industries working with large amounts of data have recognized the value of machine learning technology. By gleaning insights from this data – often in real time – organizations are able to work more efficiently or gain an advantage over competitors.

Based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines.

### Therefore, How do we describe a data set using machine language?
### What are the four key requirements / variables gathered?

In 1936 Edgar Anderson collected, 50 samples of three different types of iris, or 150 samples in total. For each sample, he measures the sepal length and width, and he measured the petal length and width, and recorded those measurements along with its species. 

The dataset contains a set of 150 records under 5 attributes - Petal Length , Petal Width , Sepal Length , Sepal width and Class.
Iris versicolor, Iris virginica

In 1936 using this data collected, Ronal Fisher wrote a paper on the linear discriminant analysis, which could be accurately distinguish the three types from one another using only the sepal and petal measurements.

In other words, Fisher coined this as a supervised learning problem, in which we are attempting to predict the species of a particular iris using the available data collected.

This is supervised learning, where we are attempting to learn the relationship between the data, namely the iris measurements, and the outcome, which is the species of iris. If this was unlabelled data, meaning that we only had the measurements not the species, we might coin this as unsupervised learning by attempting to cluster the samples, into meaningful groups.

Iris data set has become a famous data set for machine learning, because it turns out to be an easy supervised learning task, there is a strong relationship between the species and the measurements, and thus various machine learning modules can accurately predict the species given the measurements. The data set is described in more depth in the UCI learning repository, which is a repository of hundreds of data sets suitable for machine learning tasks. 

Because the iris data is so popular in machine learning it is frequently used in python, lets load into python and examine it, so we can use a machine learning model, so we can predict the species using the iris measurements.

This data set consists of one hundred and fifty rows with five columns, including the name of the species of the iris type. Each row represents one flower.
The other four columns each contain, the four measurements collected.
## Machine Learning Terminology
Each row is known as an observation, some equivalent terms are sample, examples, instance and records. Thus, the iris data set has one hundred and fifty observations.
Each column is known as a feature, some equivalent terms are predictor, attribute, independent variable, input, regressor and covariate. The iris data set has four features. 

Let’s put out an attribute of the iris object called the feature names, as you can imagine this represents the names of the four features, you can think of this as column headings for the data.
Now let’s put out two more attributes called target and target names, the target represents what we are going to predict, which is a zero, representing zetosa, and one representing versolic, or two representing virginica.
Some equivalent terms for target are response, outcome, label and dependent variable. 
WE will use response.
Two types of supervised learning, which are classification and regression.
A classification problem, is one in which the response been predicted is categorical, meaning that its values are in a finite unordered set, predicting the species of iris is an example of a classification problem as is predicting whether an email is spam or ham.
In contrast a regression problem, is one in which the response been predicted is ordered and continuous, such as the price of a house or the height of a person.

When looking at iris target, you might be wondering how you can tell, that this is a classification problem and not a regression problem, since all you can see is the number 0, 1 and 2. The answer is you cannot tell the difference, as a machine learning practioner, you have to understand how your data is encoded and decide whether your response variable is suited for regression or classification.
In this case we know that the numbers 0, 1, and 2 represent unordered categories, unless we know to use classification techniques and not regression techniques in to solve this problem, if you remember the  first video in the series we talked about how the first step in machine learning is for the model to learn the relationship between the features and the response we actually do this in the next video, but we have to make  sure that the features and the response are in the appropriate form.
There are four key requirements needed, so keep in mind as follows; first the features and the response should be passed into the machine learning model, as separate objects. 
Iris dot data 
Iris dot target fulfil this condition, since they are stored separately, secondly python is only expecting to see numbers in the features and response objects, this is exactly why iris target is stored as zeros, ones and twos, instead of the strings soTosa, Versicolor and virginica in python the response object should always be numeric regardless whether it’s a regression problem or classification problem, also the feature and the response should be stored as numpy arrays.

Numpy is a library for scientific computing that implements a homogenous multi-dimensional array known as an ende array that has been optimized for fast computation it out that both iris dot data and iris dot target are already stored as nd arrays, fourth the feature and response objects are expected to have certain shapes, specifically the feature object should have two dimensions, in which the first dimension, represented by rows is the number of observations and the second dimension is represented by columns is the number of features all numpy arrays have a shape attribute so we can verify the shape of iris data is 150 by 4. The response object is expected to have a single dimension and that dimension should have the same magnitude as the first dimension of the feature object in other words there should be one response corresponding to each observation, we can indeed verify that the shape of iris dot target is simply 150. 
L refers to the long data type that python is using to represent the data, we have now verified that iris dot data and iris dot target meet all the requirements needed for feature and response object to run in python.
The feature of python is the feature data to be stored as a variant in X and for the response data to be stored in a variant named Y, thus we will store iris dot data in X and iris dot target in Y. 

Numpy can be used to speed up the numerical computing in python browsing
Pandas which is an extremely popular python library for data exploration and manipulation.







The following Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format. That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns. this script also includes the type of species of Iris.


<img src="https://image.ibb.co/cbYW47/anderson_edgar_pdf.png" width=222px><img src="https://image.ibb.co/jUYu4x/R_A_Fischer.jpg" width=250px



<img src="https://image.ibb.co/b2wYZH/iris_machinelearning.png" alt="iris_machinelearning" border="0" width=500px></p><br>


<img src="https://image.ibb.co/gbSzP7/irisdataset.png" align="center" width=600px>

  



