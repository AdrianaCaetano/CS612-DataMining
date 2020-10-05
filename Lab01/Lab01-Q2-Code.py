'''
    CS 612 Data Mining
    Lab 01 - Q2
    @author: Adriana Caetano - Farnaz Tajadod
    Created on 09/05/2020
'''

import numpy as np

# A. Read data into a matrix from file "data.txt"
matrix0 = np.loadtxt("data.txt", dtype=int, delimiter='\t')
print("Original Matrix: \n", matrix0, "\n")

# B. Select columns: 3, 1, 9. Sort column 3 in ascending order and create a 10 by 3 matrix 1
matrix1 = matrix0[:, 2]             # column 3

col = matrix0[:, 0]                 # column 1
matrix1 = np.vstack((matrix1, col))

col = matrix0[:, 8]                 # column 9
matrix1 = np.vstack((matrix1, col))

matrix1 = np.transpose(matrix1)
matrix1 = matrix1[np.argsort(matrix1[:, 0])] #sorted by column 0
print("Matrix 1: \n", matrix1, "\n")

# C. Select columns 5, 2, 7. Sort column 5 in descending order and create a 10 by 3 matrix 2
matrix2 = matrix0[:, 4]             # column 5

col = matrix0[:, 1]                 # column 2
matrix2 = np.stack((matrix2, col))

col = matrix0[:, 6]                 # column 7
matrix2 = np.vstack((matrix2, col))

matrix2 = np.transpose(matrix2)
matrix2 = matrix2[np.argsort(matrix2[:, 0])]
matrix2 = matrix2[: : -1]                      # reversed array

print("Matrix 2: \n", matrix2, "\n")

# D. Add the two matrices into a matrix 3
matrix3 = np.add(matrix1, matrix2)
print("Matrix 3: \n", matrix3, "\n")

# E. Add matrix3 rows into a 10 by 1 into a matrix 4
matrix4 = np.sum(matrix3, axis=1)               # sum of each row
matrix4 = matrix4.reshape(-1, 1)

# F. Sort matrix 4 in ascending order
matrix4.sort(axis=0)
print("Matrix 4: \n", matrix4, "\n")

