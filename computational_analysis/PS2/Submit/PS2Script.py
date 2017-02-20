import pandas as pd
import numpy as np

# Question 1a.
def firsthalf(a):
    '''
    --------------------------------------------------------------------
    This function accepts an input string of two or more characters and
    return the first half of it, excluding the middle characters if there
    is an odd number of characters.
    --------------------------------------------------------------------
    INPUTS:
    a = input string

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN THIS FUNCTION:
    b = first half of input string

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: b
    --------------------------------------------------------------------
    '''

    if len(a)>1:
        b = a[:(len(a)//2)]
        return b

#Question 1b.
def backward(a):
    '''
    --------------------------------------------------------------------
    This function accepts an input string and reverses the order of its
    characters.
    --------------------------------------------------------------------
    INPUTS:
    a = input string

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN THIS FUNCTION:
    reverse_a = reversed order of input string

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: reverse_a
    --------------------------------------------------------------------
    '''

    reverse_a = a[::-1]
    return reverse_a

#Question 1c.
def pig_latin(a):
    '''
    --------------------------------------------------------------------
    This function accepts an input string, that is a single word, and
    translates it into Pig Latin, then returns the translated word.
    --------------------------------------------------------------------
    INPUTS:
    a = input string

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN THIS FUNCTION:
    pig = translated Pig Latin word.

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: pig
    --------------------------------------------------------------------
    '''
    # set input string to lowercase
    a = a.lower()
    # define vowel
    vowel = ['a', 'e', 'i', 'o', 'u']
    hay = 'hay'
    ay = 'ay'
    i = 0
    if a[i] in vowel:
        pig = a + hay
    else:
        for index in range(len(a)):
            if a[i] not in vowel:
                i += 1
        b = a[:i]
        c = a[i:]
        pig = c + b + ay
    return pig

# Question 1d.
grid = np.load('grid.npy')
def max_prod(grid):
    '''
    --------------------------------------------------------------------
    This function accepts a 20*20 grid and finds the maximum product of
    four adjacent numbers in the grid.
    --------------------------------------------------------------------
    INPUTS:
    grid = 20*20 grid

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN THIS FUNCTION:
    a = maximum product of four adjacent numbers
    FILES CREATED BY THIS FUNCTION: None

    RETURNS: a
    --------------------------------------------------------------------
    '''

    # largest vertical products
    vert1 = grid[0:17]
    vert2 = grid[1:18]
    vert3 = grid[2:19]
    vert4 = grid[3:20]
    vertical_product = np.amax(vert1 * vert2 * vert3 * vert4)

    # largest horizontal products
    hori1 = grid[0:20,0:17]
    hori2 = grid[0:20,1:18]
    hori3 = grid[0:20,2:19]
    hori4 = grid[0:20,3:20]
    horizontal_product = np.amax(hori1 * hori2 * hori3 * hori4 )

    #diagonal down products
    diag_down_1 = grid[0:17,0:17]
    diag_down_2 = grid[1:18,1:18]
    diag_down_3 = grid[2:19,2:19]
    diag_down_4 = grid[3:20,3:20]
    diag_down_prod = np.amax(diag_down_1 * diag_down_2 * diag_down_3 * diag_down_4)

    #diagonal up products
    diag_up_1 = grid[3:20,0:17]
    diag_up_2 = grid[2:19,1:18]
    diag_up_3 = grid[1:18,2:19]
    diag_up_4 = grid[0:17,3:20]
    diag_up_prod = np.amax(diag_up_1 * diag_up_2 * diag_up_3 * diag_up_4)

    #printing the largest 4 adjacent numbers product
    a = np.amax([vertical_product, horizontal_product, diag_down_prod, diag_up_prod])
    return a

print('1d. Greatest product of four adjacent numbers: ',
      max_prod(grid))


#Question 3a
#defining matrices A, B, C
A = np.array([[0,2,4],[1,3,5]])
B = np.array([[3,0,0], [3,3,0], [3,3,3]])
C = np.array([[-2,0,0],[0,-2,0],[0,0,-2]])

#defining function ipmstack
def ipmstack(A, B, C):
        '''
        --------------------------------------------------------------------
        This function accepts an input string, that is a single word, and
        translates it into Pig Latin, then returns the translated word.
        --------------------------------------------------------------------
        INPUTS:
        A = input matrix 1
        B = input matrix 2
        C = input matrix 3

        OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

        OBJECTS CREATED WITHIN THIS FUNCTION:
        D = block matrix

        FILES CREATED BY THIS FUNCTION: None

        RETURNS: D
        --------------------------------------------------------------------
        '''

    third = np.hstack((B, np.zeros((B.shape)), C))

    second = np.hstack((A, np.zeros((A.shape[0], third.shape[1]-A.shape[1]))))

    identity = np.identity(A.T.shape[0])

    first = np.hstack((np.zeros((A.T.shape[0], third.shape[1]-A.T.shape[1]-identity.shape[1])),A.T, identity))

    D = np.vstack((first, second, third))

    return D

x = ipmstack(A, B, C)
print('3a.')
print(x)

# Question 3b(i)
df = pd.read_csv("popagesex2015.csv", header = 4,
                 names=['gender', 'age', 'pop10','pop11','pop12', 'pop13',
                        'pop14', 'pop15'],
                 converters = {'gender': str}).replace({"gender" : {'0': "both", '1': "male", '2': "female"}})[
                 pd.read_csv("popagesex2015.csv", header = 4,names=['gender', 'age', 'pop10','pop11','pop12', 'pop13','pop14', 'pop15'])['age']<999
                             ].set_index(["gender", "age"])
# Question 3b(ii)
gender_prop = df.ix[['male', 'female']].groupby(level =['gender']).sum()/df.ix[['male', 'female']].sum()
print('3b(ii).')
print(gender_prop)

# Question 3b(iii)
pop_by_age = df.ix['both'].sum(axis=1).groupby(level = 'age').sum()/df.ix['both'].sum(axis=1).sum()
print('3b(iii).')
print(pop_by_age)
