import numpy as np
import ex2module as ex2m
import math

# Question 2(a)
# Setting the seed to produce repeatable results
seed = 300
np.random.seed(seed)

# Declaring parameters of a lognormally distributed random variable scores
# Randomly generating 10,000 draws from lognormal distribution
scores = np.random.normal(math.log(70), 0.2, 10000)
# Running the 10,000 draws through three outlier scrubs 
scrubbed_scores = ex2m.threescrubs(scores)

# Question 2(c)
# Calculating the number of elements in the returned array
elements = len(scrubbed_scores)
# Calculating the mean of elements in the returned array
mean = np.mean(scrubbed_scores)
# Calculating the standard deviation of elements in the returned array
std = np.std(scrubbed_scores)

print('2c. Number of elements in the array returned by the function threescrubs(): ',
      elements)

print('2c. Mean of elements in the array returned by the function threescrubs(): ',
      mean)

print('2c. Standard deviation of elements in the array returned by the function threescrubs(): ',
      std)
