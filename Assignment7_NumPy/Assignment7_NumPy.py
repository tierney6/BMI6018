# Hi TAs! I have also included a .ipynb version in the same folder in case you prefer that format. Thanks!



#### Question 1 ######
# import numpy library 
import numpy as np

# print version
f"Numpy Version is {np.__version__}"

#### Question 2 ######

# Create a 1-D array of numbers from 0-9
# use the arange function
# it automatically starts with 0, and is end exclusive, so we provide 10 as the input to get 0-9
np.arange(10)


#### Question 3 #######
# Import a dataset with numbers and texts keeping the text intact in python numpy.

# import iris.txt using numpy's load text, using relative path since they are in the same directory
# numpy array only allows a single datatype, so convert everything to string
# data are comma-delimited
data = np.loadtxt("iris.txt", dtype = "str", delimiter = ",")


#### Question 4
# Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset. 

# first extract the 4th column
petal = data[:, [3]]
petal = petal.astype("float")

index = np.where(petal > 1.0)[0][0]

f"The first occurrence of a value greater than 1.0 in petalwidth, 4th column is at the {index} index."



### Question 5
# From the array a, replace all values greater than 30 to 30 and less than 10 to 10.


np.random.seed(100)
a = np.random.uniform(1,50, 20)
print(a)

# replace all values greater than 30 with 30
a[a > 30] = 30
a[a < 10] = 10
a