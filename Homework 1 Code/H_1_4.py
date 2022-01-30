#Homework 1 Problem 3 Michael Bartlett
import numpy as np

def make_matrix(m, n):
    '''

    :param m: The number of rows in the matrix
    :param n: The number of columns in the matrix
    :return: A matrix with each position filled with 2i + j
    '''

    temp = np.empty((m, n))
    #Loop through the array
    for i in range(m):
        for j in range (n):
            temp[i, j] = 2*(i+1) + (j+1)
    return temp

if __name__ == '__main__':
    print(make_matrix(3, 4))