"""
    CS 612 Data Mining
    Lab 03
    @author: Adriana Caetano
    Created on 09/16/2020 - edited on 09/19/20
"""

import numpy as np
import pandas as pd
from tabulate import tabulate

# Set print options with 2 significant digits
pd.set_option('precision', 2)
np.set_printoptions(precision= 2)

class myMatrix:
    # Constructor
    def __init__(self):
        self.myMatrix = myMatrix

    ''' 
    Function get_dimension
    Description: 
        Get a number from the user. Check if it is a number, exits if not a number.
    Returns: 
        number(int) 
    '''
    def get_dimension():
        number = input("Enter the dimension of your matrix: ")
        if number.isdigit():
            return int(number)
        else:
            print("ERROR: This is not a number.")
            exit()

    '''
        Function: check_dimension
        Description: 
            Test validity of the number for building a matrix
    '''
    def check_dimension(number):
        if number <= 3:
            print("ERROR: This dimension is out of bound. This program stops here.")
            exit()
        elif number >= 8:
            print("We can only handle up to 8 dimensions at this time. This program stops here.")
            exit()
        return

    '''
    Function getMatrix
    Description: 
        Create a matrix from file with fixed size
    Parameters:
        size(int): size of matrix for rows and columns
        file(string): path to file
    Returns:
        matrix(numpy array)        
    '''
    def getMatrix(size, file):
        # Check dimension
        myMatrix.check_dimension(size)

        # Check if file has enough values
        matrix = np.loadtxt(file, delimiter='\t', dtype=int).flatten()
        if int(matrix.size) < size * size:
            print("ERROR: File do not have enough elements")
            exit()
        matrix = matrix[:size*size].reshape((size,size))
        return matrix

    '''
    Function product
    Description:
        Calculate the product of two arrays element by element.
    Parameters: 
        matrix1: first numpy array
        matrix2: second numpy array
    Returns:
        (numpy array) of the result
    '''
    def product(matrix1,matrix2):
        return np.multiply(matrix1, matrix2)

    '''
    Function dot_product
    Description:
        Calculate the dot product of two arrays
    Parameters: 
        matrix1: first numpy array
        matrix2: second numpy array
    Returns:
        (numpy array) of the result
    '''
    def dot_product(matrix1, matrix2):
        return np.dot(matrix1, matrix2)

    '''
       Function division
       Description:
           Calculate the division of two arrays. Before calculating, check for 
           zeros to avoid runtime errors by zero division
       Parameters: 
           matrix1: first numpy array (numerator)
           matrix2: second numpy array (denominator)
       Returns:
           (numpy array) of the result with 2 significant digits
       '''
    def division(matrix1, matrix2):
        # Change array to dtype float
        matrix1 = np.asarray(matrix1, dtype='float')
        matrix2 = np.asarray(matrix2, dtype ='float')

        # Search for zeros in matrix2 and change it to undefined to avoid runtime errors
        matrix2[matrix2 == 0] = np.nan
        result = np.divide(matrix1, matrix2).round(decimals=2)

        result = pd.DataFrame(result)
        result = result.replace(np.nan, 'undef', regex= True)

        return result

    '''
    Function calculate
    Description:
        Show matrices content.
        Call functions myMatrix.product, myMatrix.dot-product, and myMatrix.division 
        and print tabulated results.
    Parameters: 
        matrix1: first numpy array
        matrix2: second numpy array
    '''
    def calculate(matrix1, matrix2):
        print("The content of the first matrix is: \n", tabulate(matrix1), '\n')
        print("The content of the second matrix is: \n", tabulate(matrix2), '\n')

        product = myMatrix.product(matrix1, matrix2)
        print("The product of the two matrices is: \n", tabulate(product), '\n')

        dot_product = myMatrix.dot_product(matrix1, matrix2)
        print("The dot product of the two matrices is: \n", tabulate(dot_product), '\n')

        division = myMatrix.division(matrix1, matrix2)
        print("The division of matrix1 divided by matrix2 is: \n", tabulate(division), '\n')


def main():
    # Get number from user
    n = myMatrix.get_dimension()
    print()

    # Define files
    file1 = "file1.txt"
    file2 = "file2.txt"
    file3 = "file3.txt"

    # Create matrices from files
    M1 = myMatrix.getMatrix(n, file1)
    M2 = myMatrix.getMatrix(n, file2)
    modM2 = myMatrix.getMatrix(n, file3)

    # Perform calculations
    myMatrix.calculate(M1, M2)

    for x in range(3):
        print("****************************************************************************")

    # Perform new calculations with modified second matrix
    print("\nNew Execution:\n")
    myMatrix.calculate(M1, modM2)

    print("**************************** End of the program ****************************")
    return

if __name__ == "__main__":
    main()