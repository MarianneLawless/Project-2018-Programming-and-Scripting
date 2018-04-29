# Marianne Lawless
# Exercise 5 
# Iris dataset downloaded from https://archive.ics.uci.edu/ml/datasets/iris

with open("data/iris.csv") as f: #Open the file and automatically close 
  for line in f: #loops through each line in the file, and prints the lines in the following format
    print('{:4} {:4} {:4} {:4}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
    
    