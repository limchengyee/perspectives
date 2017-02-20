# Question 2(b) and (d)
import numpy as np

def kill_outliers(array1):
    '''
    --------------------------------------------------------------------
    This function deletes all elements of the array that are greater than
    three standard deviations above or below the mean of the series, the
    mean, and returns the one-dimensional array with the remaining
    elmeents.
    --------------------------------------------------------------------
    INPUTS:
    array1 = one-dimensional NumPy array, first array passed into function

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN THIS FUNCTION:
    array2 = array of elements that are within three standard deviations
    from the mean of array1

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: array2
    --------------------------------------------------------------------
    '''
    std = np.std(array1)
    mean = np.mean(array1)
    high = (3*std + mean)
    low = (mean - 3*std)
    a = array1[array1 <= high]
    array2 = a[a >= low]
    return array2

def threescrubs(w):
    '''
    --------------------------------------------------------------------
    This function runs three consecutive filters of kill_outliers().
    --------------------------------------------------------------------
    INPUTS:
    w = one-dimensional numpy array, first array passed into function

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN THIS FUNCTION:
    w = array of elements after three recursions of kill_outliers

    FILES CREATED BY THIS FUNCTION: kill_outliers

    RETURNS: w
    --------------------------------------------------------------------
    '''
    x = kill_outliers(w)
    y = kill_outliers(x)
    z = kill_outliers(y)
    return z
