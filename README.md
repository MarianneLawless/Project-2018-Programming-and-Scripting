**Project-2018-Programming-and-Scripting**
==========================================
<img src="https://image.ibb.co/g96qDc/gmitlogo.jpg" alt="gmitlogo" border="0" width=450 align="center">
# The programming Language used to assist in writing code for this project
Anaconda download is a great way to install Python and all of the common Python libraries on your computer. I recommend installing version 3.6, 64-bit. https://www.python.org/

Before starting the project some programs, files and libraries were downloaded and installed:
<ol>
 <li>Python version 3.6 downloaded via Anaconda3</li>
 <li>Visual Studio Code version 1.21.1 downloaded and set up with Github</li> 
 <li>Iris dataset downloaded from UCI website or it can be done from other ways, such as via sklearn </li>
 <li>Libraries imported: csv, pandas, numpy, matplotlib,seaborn and sklearn </li>
 </ol>
 
  When a library is imported, it means that the library will be loaded into the memory and then it can be use used. To import a library the following code should be run:
 
 ``` python
 import csv
 import pandas as pd
 import numpy as np
 import seaborn as sns
 import scipy
 import sklearn
  
Some information about some of the libraries imported[1]: <br>
_Pandas_ - for data-frame management package that allows for some useful function on the dataset.<br>
_Numpy_ - package useful for lineal algebra.<br>
_Matplotlib_ - good package to contruct visualizations.<br>
_Seaborn_ - it is based on matplotlib that provides a high-level interface for drawing attractive statistical graphics.<br>
_Scipy_ - a collection of numerical algorithms including statistics.<br>
_Sklearn_ - package important to do machine learning in python.<br>
 

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

## Iris data set




In 1936 Edgar Anderson collected, 50 samples of three different types of iris, or 150 samples in total. For each sample, he measures the sepal length and width, and he measured the petal length and width, and recorded those measurements along with its species. 

The following Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format. That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns. this script also includes the type of species of Iris.

(https://![alt text](github.com/MarianneLawless/Project-2018-Programming-and-Scripting/RonaldFisherimage.jpg)

http://www.swlearning.com/quant/kohler/stat/biographical_sketches/Fisher_3.jpeg

<p align="center"><img src="https://image.ibb.co/cbYW47/anderson_edgar_pdf.png" width=222px><img src="https://image.ibb.co/jUYu4x/R_A_Fischer.jpg" width=250px></p><br>
<p align="center">Edgar Anderson and Ronald Fisher</p>


<p align="center"><img src="https://image.ibb.co/b2wYZH/iris_machinelearning.png" alt="iris_machinelearning" border="0" width=500px></p><br>
<p align="center">Three iris species/classes. From: https://goo.gl/RSwtrk</p>

 <p align="center"><img src="https://image.ibb.co/gbSzP7/irisdataset.png" align="center" width=600px></p><br>
<p align="center"> Iris attributes. From: https://rpubs.com/wjholst/322258</p>
  
 <p align="center"><img src="https://image.ibb.co/kTbs2H/2018_04_11_13_05_03_sq_Es_Wbo_png_451_592.png"></p><br>
 <p align="center">Iris Dataset characteristics. From: http://scikit-learn.org/stable/datasets/index.html#datasets</p>


