

#Question 3a
#defining matrices A, B, C
A = np.array([[0,2,4],[1,3,5]])
B = np.array([[3,0,0], [3,3,0], [3,3,3]])
C = np.array([[-2,0,0],[0,-2,0],[0,0,-2]])

#defining function ipmstack
def ipmstack(A, B, C):
    third = np.hstack((B, np.zeros((B.shape)), C))

    second = np.hstack((A, np.zeros((A.shape[0], third.shape[1]-A.shape[1]))))

    identity = np.identity(A.T.shape[0])

    first = np.hstack((np.zeros((A.T.shape[0], third.shape[1]-A.T.shape[1]-identity.shape[1])),A.T, identity))

    D = np.vstack((first, second, third))

    return D

x = ipmstack(A, B, C)
print('Q3a.')
print(x)
