**Project-2018-Programming-and-Scripting**
==========================================
<img src="https://image.ibb.co/g96qDc/gmitlogo.jpg" alt="gmitlogo" border="0" width=450 align="center">

# The programming Language used to assist in writing code for this project is Python
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

## Because the iris data is so popular in machine learning it is frequently used in python.

## What is the famous iris data set, and how does it relate to machine learning.

First of all lets have a look at what I mean by machine learning.
Machine learning is a method of data analysis that automates analytical model building. It is a branch of artificial intelligence based on the idea that systems can learn from data, identify patterns and make decisions with minimal human intervention.

Most industries working with large amounts of data have recognized the value of machine learning technology. By gleaning insights from this data – often in real time – organizations are able to work more efficiently or gain an advantage over competitors.

Based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines.

### Therefore, How do we describe a data set using machine language?
### What are the four key requirements / variables gathered?

In 1936 Edgar Anderson collected, 50 samples of three different types of iris, or 150 samples in total. For each sample, he measures the sepal length and width, and he measured the petal length and width, and recorded those measurements along with its species. 

## Edgar Anderson

<img src="https://image.ibb.co/cbYW47/anderson_edgar_pdf.png" width=222px align=center>

The dataset contains a set of 150 records under 5 attributes - Petal Length , Petal Width , Sepal Length , Sepal width and Class.
Iris versicolor, Iris virginica

<img src="https://image.ibb.co/gbSzP7/irisdataset.png" align="center" width=600px>

<img src="https://image.ibb.co/b2wYZH/iris_machinelearning.png" alt="iris_machinelearning" border="0" width=500px>

In 1936 using this data collected, Ronald Fisher wrote a paper on the linear discriminant analysis, which could be accurately distinguish the three types from one another using only the sepal and petal measurements.

##  Ronald Fisher
<img src="https://image.ibb.co/jUYu4x/R_A_Fischer.jpg" width=250px align=center>

In other words, Fisher coined this as a supervised learning problem, in which we are attempting to predict the species of a particular iris using the available data collected.

This is supervised learning, where we are attempting to learn the relationship between the data, namely the iris measurements, and the outcome, which is the species of iris. If this was unlabelled data, meaning that we only had the measurements not the species, we might coin this as unsupervised learning by attempting to cluster the samples, into meaningful groups.

Iris data set has become a famous data set for machine learning, because it turns out to be an easy supervised learning task, there is a strong relationship between the species and the measurements, and thus various machine learning modules can accurately predict the species given the measurements. The data set is described in more depth in the UCI learning repository, which is a repository of hundreds of data sets suitable for machine learning tasks. 

This data set consists of one hundred and fifty rows with five columns, including the name of the species of the iris type. Each row represents one flower.
The other four columns each contain, the four measurements collected.

## Machine Learning Terminology
Each row is known as an observation, some equivalent terms are sample, examples, instance and records. Thus, the iris data set has one hundred and fifty observations.
Each column is known as a feature, some equivalent terms are predictor, attribute, independent variable, input, regressor and covariate. The iris data set has four features. 








The following Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format. That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns. this script also includes the type of species of Iris.













  



