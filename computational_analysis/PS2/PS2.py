# Question 1a.
def firsthalf(a):
    if len(a)>1:
        b = a[:(len(a)//2)]
        return b

#Question 1b.
def backward(a):
    reverse_a = a[::-1]
    return reverse_a

#Question 1c.
def pig_latin(a):
    a = a.lower()
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
    # largest vertical products
    vert1 = grid[0:16]
    vert2 = grid[1:17]
    vert3 = grid[2:18]
    vert4 = grid[3:19]
    vertical_product = np.amax(vert1 * vert2 * vert3 * vert4)

    # largest horizontal products
    hori1 = grid[0:16,0:16]
    hori2 = grid[1:17,1:17]
    hori3 = grid[2:18,2:18]
    hori4 = grid[3:19,3:19]
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
