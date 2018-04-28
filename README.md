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

### Fisher's Iris Data
Dataset Order 	Sepal length 	Sepal width 	Petal length 	Petal width 	Species
1 	5.1 	3.5 	1.4 	0.2 	I. setosa
2 	4.9 	3.0 	1.4 	0.2 	I. setosa
3 	4.7 	3.2 	1.3 	0.2 	I. setosa
4 	4.6 	3.1 	1.5 	0.2 	I. setosa
5 	5.0 	3.6 	1.4 	0.3 	I. setosa
6 	5.4 	3.9 	1.7 	0.4 	I. setosa
7 	4.6 	3.4 	1.4 	0.3 	I. setosa
8 	5.0 	3.4 	1.5 	0.2 	I. setosa
9 	4.4 	2.9 	1.4 	0.2 	I. setosa
10 	4.9 	3.1 	1.5 	0.1 	I. setosa
11 	5.4 	3.7 	1.5 	0.2 	I. setosa
12 	4.8 	3.4 	1.6 	0.2 	I. setosa
13 	4.8 	3.0 	1.4 	0.1 	I. setosa
14 	4.3 	3.0 	1.1 	0.1 	I. setosa
15 	5.8 	4.0 	1.2 	0.2 	I. setosa
16 	5.7 	4.4 	1.5 	0.4 	I. setosa
17 	5.4 	3.9 	1.3 	0.4 	I. setosa
18 	5.1 	3.5 	1.4 	0.3 	I. setosa
19 	5.7 	3.8 	1.7 	0.3 	I. setosa
20 	5.1 	3.8 	1.5 	0.3 	I. setosa
21 	5.4 	3.4 	1.7 	0.2 	I. setosa
22 	5.1 	3.7 	1.5 	0.4 	I. setosa
23 	4.6 	3.6 	1.0 	0.2 	I. setosa
24 	5.1 	3.3 	1.7 	0.5 	I. setosa
25 	4.8 	3.4 	1.9 	0.2 	I. setosa
26 	5.0 	3.0 	1.6 	0.2 	I. setosa
27 	5.0 	3.4 	1.6 	0.4 	I. setosa
28 	5.2 	3.5 	1.5 	0.2 	I. setosa
29 	5.2 	3.4 	1.4 	0.2 	I. setosa
30 	4.7 	3.2 	1.6 	0.2 	I. setosa
31 	4.8 	3.1 	1.6 	0.2 	I. setosa
32 	5.4 	3.4 	1.5 	0.4 	I. setosa
33 	5.2 	4.1 	1.5 	0.1 	I. setosa
34 	5.5 	4.2 	1.4 	0.2 	I. setosa
35 	4.9 	3.1 	1.5 	0.2 	I. setosa
36 	5.0 	3.2 	1.2 	0.2 	I. setosa
37 	5.5 	3.5 	1.3 	0.2 	I. setosa
38 	4.9 	3.6 	1.4 	0.1 	I. setosa
39 	4.4 	3.0 	1.3 	0.2 	I. setosa
40 	5.1 	3.4 	1.5 	0.2 	I. setosa
41 	5.0 	3.5 	1.3 	0.3 	I. setosa
42 	4.5 	2.3 	1.3 	0.3 	I. setosa
43 	4.4 	3.2 	1.3 	0.2 	I. setosa
44 	5.0 	3.5 	1.6 	0.6 	I. setosa
45 	5.1 	3.8 	1.9 	0.4 	I. setosa
46 	4.8 	3.0 	1.4 	0.3 	I. setosa
47 	5.1 	3.8 	1.6 	0.2 	I. setosa
48 	4.6 	3.2 	1.4 	0.2 	I. setosa
49 	5.3 	3.7 	1.5 	0.2 	I. setosa
50 	5.0 	3.3 	1.4 	0.2 	I. setosa
51 	7.0 	3.2 	4.7 	1.4 	I. versicolor
52 	6.4 	3.2 	4.5 	1.5 	I. versicolor
53 	6.9 	3.1 	4.9 	1.5 	I. versicolor
54 	5.5 	2.3 	4.0 	1.3 	I. versicolor
55 	6.5 	2.8 	4.6 	1.5 	I. versicolor
56 	5.7 	2.8 	4.5 	1.3 	I. versicolor
57 	6.3 	3.3 	4.7 	1.6 	I. versicolor
58 	4.9 	2.4 	3.3 	1.0 	I. versicolor
59 	6.6 	2.9 	4.6 	1.3 	I. versicolor
60 	5.2 	2.7 	3.9 	1.4 	I. versicolor
61 	5.0 	2.0 	3.5 	1.0 	I. versicolor
62 	5.9 	3.0 	4.2 	1.5 	I. versicolor
63 	6.0 	2.2 	4.0 	1.0 	I. versicolor
64 	6.1 	2.9 	4.7 	1.4 	I. versicolor
65 	5.6 	2.9 	3.6 	1.3 	I. versicolor
66 	6.7 	3.1 	4.4 	1.4 	I. versicolor
67 	5.6 	3.0 	4.5 	1.5 	I. versicolor
68 	5.8 	2.7 	4.1 	1.0 	I. versicolor
69 	6.2 	2.2 	4.5 	1.5 	I. versicolor
70 	5.6 	2.5 	3.9 	1.1 	I. versicolor
71 	5.9 	3.2 	4.8 	1.8 	I. versicolor
72 	6.1 	2.8 	4.0 	1.3 	I. versicolor
73 	6.3 	2.5 	4.9 	1.5 	I. versicolor
74 	6.1 	2.8 	4.7 	1.2 	I. versicolor
75 	6.4 	2.9 	4.3 	1.3 	I. versicolor
76 	6.6 	3.0 	4.4 	1.4 	I. versicolor
77 	6.8 	2.8 	4.8 	1.4 	I. versicolor
78 	6.7 	3.0 	5.0 	1.7 	I. versicolor
79 	6.0 	2.9 	4.5 	1.5 	I. versicolor
80 	5.7 	2.6 	3.5 	1.0 	I. versicolor
81 	5.5 	2.4 	3.8 	1.1 	I. versicolor
82 	5.5 	2.4 	3.7 	1.0 	I. versicolor
83 	5.8 	2.7 	3.9 	1.2 	I. versicolor
84 	6.0 	2.7 	5.1 	1.6 	I. versicolor
85 	5.4 	3.0 	4.5 	1.5 	I. versicolor
86 	6.0 	3.4 	4.5 	1.6 	I. versicolor
87 	6.7 	3.1 	4.7 	1.5 	I. versicolor
88 	6.3 	2.3 	4.4 	1.3 	I. versicolor
89 	5.6 	3.0 	4.1 	1.3 	I. versicolor
90 	5.5 	2.5 	4.0 	1.3 	I. versicolor
91 	5.5 	2.6 	4.4 	1.2 	I. versicolor
92 	6.1 	3.0 	4.6 	1.4 	I. versicolor
93 	5.8 	2.6 	4.0 	1.2 	I. versicolor
94 	5.0 	2.3 	3.3 	1.0 	I. versicolor
95 	5.6 	2.7 	4.2 	1.3 	I. versicolor
96 	5.7 	3.0 	4.2 	1.2 	I. versicolor
97 	5.7 	2.9 	4.2 	1.3 	I. versicolor
98 	6.2 	2.9 	4.3 	1.3 	I. versicolor
99 	5.1 	2.5 	3.0 	1.1 	I. versicolor
100 	5.7 	2.8 	4.1 	1.3 	I. versicolor
101 	6.3 	3.3 	6.0 	2.5 	I. virginica
102 	5.8 	2.7 	5.1 	1.9 	I. virginica
103 	7.1 	3.0 	5.9 	2.1 	I. virginica
104 	6.3 	2.9 	5.6 	1.8 	I. virginica
105 	6.5 	3.0 	5.8 	2.2 	I. virginica
106 	7.6 	3.0 	6.6 	2.1 	I. virginica
107 	4.9 	2.5 	4.5 	1.7 	I. virginica
108 	7.3 	2.9 	6.3 	1.8 	I. virginica
109 	6.7 	2.5 	5.8 	1.8 	I. virginica
110 	7.2 	3.6 	6.1 	2.5 	I. virginica
111 	6.5 	3.2 	5.1 	2.0 	I. virginica
112 	6.4 	2.7 	5.3 	1.9 	I. virginica
113 	6.8 	3.0 	5.5 	2.1 	I. virginica
114 	5.7 	2.5 	5.0 	2.0 	I. virginica
115 	5.8 	2.8 	5.1 	2.4 	I. virginica
116 	6.4 	3.2 	5.3 	2.3 	I. virginica
117 	6.5 	3.0 	5.5 	1.8 	I. virginica
118 	7.7 	3.8 	6.7 	2.2 	I. virginica
119 	7.7 	2.6 	6.9 	2.3 	I. virginica
120 	6.0 	2.2 	5.0 	1.5 	I. virginica
121 	6.9 	3.2 	5.7 	2.3 	I. virginica
122 	5.6 	2.8 	4.9 	2.0 	I. virginica
123 	7.7 	2.8 	6.7 	2.0 	I. virginica
124 	6.3 	2.7 	4.9 	1.8 	I. virginica
125 	6.7 	3.3 	5.7 	2.1 	I. virginica
126 	7.2 	3.2 	6.0 	1.8 	I. virginica
127 	6.2 	2.8 	4.8 	1.8 	I. virginica
128 	6.1 	3.0 	4.9 	1.8 	I. virginica
129 	6.4 	2.8 	5.6 	2.1 	I. virginica
130 	7.2 	3.0 	5.8 	1.6 	I. virginica
131 	7.4 	2.8 	6.1 	1.9 	I. virginica
132 	7.9 	3.8 	6.4 	2.0 	I. virginica
133 	6.4 	2.8 	5.6 	2.2 	I. virginica
134 	6.3 	2.8 	5.1 	1.5 	I. virginica
135 	6.1 	2.6 	5.6 	1.4 	I. virginica
136 	7.7 	3.0 	6.1 	2.3 	I. virginica
137 	6.3 	3.4 	5.6 	2.4 	I. virginica
138 	6.4 	3.1 	5.5 	1.8 	I. virginica
139 	6.0 	3.0 	4.8 	1.8 	I. virginica
140 	6.9 	3.1 	5.4 	2.1 	I. virginica
141 	6.7 	3.1 	5.6 	2.4 	I. virginica
142 	6.9 	3.1 	5.1 	2.3 	I. virginica
143 	5.8 	2.7 	5.1 	1.9 	I. virginica
144 	6.8 	3.2 	5.9 	2.3 	I. virginica
145 	6.7 	3.3 	5.7 	2.5 	I. virginica
146 	6.7 	3.0 	5.2 	2.3 	I. virginica
147 	6.3 	2.5 	5.0 	1.9 	I. virginica
148 	6.5 	3.0 	5.2 	2.0 	I. virginica
149 	6.2 	3.4 	5.4 	2.3 	I. virginica
150 	5.9 	3.0 	5.1 	1.8 	I. virginica

The following Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format. That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns. this script also includes the type of species of Iris.


<img src="https://image.ibb.co/cbYW47/anderson_edgar_pdf.png" width=222px><img src="https://image.ibb.co/jUYu4x/R_A_Fischer.jpg" width=250px



<img src="https://image.ibb.co/b2wYZH/iris_machinelearning.png" alt="iris_machinelearning" border="0" width=500px></p><br>


<img src="https://image.ibb.co/gbSzP7/irisdataset.png" align="center" width=600px>

  



