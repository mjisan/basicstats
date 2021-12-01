#!/usr/bin/env python
# coding: utf-8

# ## Script to calculate Basic Statistics

# ### Equation for the mean:   $\mu_x = \sum_{i=1}^{N}\frac{x_i}{N}$
# 
# ### Equation for the standard deviation:  $\sigma_x = \sqrt{\sum_{i=1}^{N}\left(x_i - \mu \right)^2}\frac{1}{N-1}$
# 
# 
# **Instructions:**
# 
# **(1) Before you write code, write an algorithm that describes the sequence of steps you will take to compute the mean and standard deviation for your samples.  The algorithm can be written in pseudocode or as an itemized list.***
# 
# **(2) Use 'for' loops to help yourself compute the average and standard deviation.**
# 
# **(3) Use for loops and conditional operators to count the number of samples within $1\sigma$ of the mean.**
# 
# **Note:** It is not acceptable to use the pre-programmed routines for mean and st. dev., e.g. numpy.mean()

# ### Edit this box to write an algorithm for computing the mean and std. deviation.
# 
# #### Average
# 
# **(a) calculate length of the list**
# 
# **(b) calculate summation of elements in the list.**
# 
# **(c) calculate average by diving the sum of the elements by the length of elements.**
# 
# #### Standard Deviation
# 
# 
# **(d) calculate variance for all the elements of the list and divide it by the number of elements.**
# **(e) Finally, take square root of the variance to calcualte the value of standard deviation**
# 
# 
# 
# 
# 
# 
# 

# ### Write your code using instructions in the cells below.

# In[1]:


# Put your Header information here.  Name, creation date, version, etc.
from datetime import date
from datetime import datetime



print("Name: {}".format('Mansur Ali Jisan'))

create_date = date.today()
print("Creation date:", create_date)

now = datetime.now()
 
print("now =", now)
dt_string = now.strftime("%B %d, %Y %H:%M:%S")

print("date and time =", dt_string)	


# In[2]:


# Import the matplotlib module here.  No other modules should be used.
import matplotlib.pyplot as plt


# In[3]:


#-- created function to calculate length, sum, mean, variance and standard deviations

def calc_sum(num):
    """returns sum of a list
    """    
    sum_num = 0
    
    for t in num:
        sum_num = sum_num + t           
        
    return sum_num

def calc_length(num):
    """returns the length of a list
    """
    count = 0
    
    for t in num:

        count += 1

    return count

def calc_avg(num):
    """returns average of a list
    """    
    avg = calc_sum(num) / calc_length(num)

    return avg
    
def variance(data):
    """returns variance 
    """ 
    n = calc_length(data)
    mean = calc_sum(data) / n
    return sum((x - calc_avg(data)) ** 2 for x in data) / (n - 1)

def variance_sk(data):
    """used for calculating variance in skewness equation 
    """ 
    n = calc_length(data)
    mean = calc_sum(data) / n
    return sum((x - calc_avg(data)) ** 3 for x in data) / (n - 1)

def stdev(data):
    """returns standard deviation
    """ 
    var = variance(data)
    std_dev = (var)**(1/2)
    return std_dev


# In[4]:


# Create a list variable that contains at least 25 elements.  You can create this list any number of ways.  
# This will be your sample.

