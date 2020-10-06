"""
    CS 612 Data Mining
    Lab 02
    @author: Adriana Caetano
    Created on 09/08/2020 - Edited on 09/10/2020
"""

import pandas as pd
from openpyxl.workbook import Workbook
from tabulate import tabulate


# 	OriginalMatrix = read the data from the file
data = pd.read_excel("AlzheimerData.xlsx", skiprows=[0])  # Pandas DataFrame

#	Print OriginalMatrix
print("Original data: \n", data, "\n")

#	Matrix1 = Use OriginalMatrix to remove the columns that only include Zero
matrix1 = data.loc[:, (data != 0).any(axis=0)]

#	Print Matrix1
print("Matrix 1: \n", tabulate(matrix1), "\n")

#	Matrix2 = Use Matrix1 to remove the columns in which they have at least 5 cells which are junks (non-numbers).
matrix2 = (matrix1.apply(pd.to_numeric, errors='coerce'))  # Change "junk values" into NaN

#matrix2 = matrix2.dropna(axis=1, thresh=5)  # drop columns with at least 5 NaN    THIS IS NOT WORKING
#matrix2 = matrix2.drop(columns=['X7', 'X12'])   THIS WORKS!
print("NaN in each column of Matrix2: \n", matrix2.isnull().sum(), sep='\n')

matrix2 = matrix2.loc[:, matrix2.isna().sum() < 5]
matrix2 = matrix2.fillna(0) # change Nan into zero

#	Print Matrix2
print("\nMatrix 2: \n", tabulate(matrix2), "\n")

#	Matrix3 = Use Matrix2 to remove the rows in which they have at least 5 cells which are junks (non-numbers).
#matrix3 = matrix2.dropna(axis=0, thresh=5)   THIS DOES NOT WORK
matrix3 = matrix2.loc[matrix2.isna().sum(axis=1) < 5, :]
print("NaN in each row of Matrix3: \n", matrix3.isnull().sum(), sep='\n')

#	Print Matrix3
print("\nMatrix 3: \n", tabulate(matrix3), "\n")

# Find mean, stdDev, min, and max of the population. Do not include column Y
target = matrix3.iloc[:, 0]
target = target.to_frame()
print("Target:\n", target, "\n")

matrix4 = matrix3.drop(matrix3.columns[0], axis=1)
print("Matrix 4: \n", tabulate(matrix4), "\n")
print("X Samples:\n", matrix4.describe(), "\n")

mean = matrix4.stack().mean()
std = matrix4.stack().std()
min = matrix4.stack().min()
max = matrix4.stack().max()

print("X Population")
print("Mean: ", mean)
print("Standard Deviation: ", std)
print("Minimun: ", min)
print("Maximun: ", max)
print("\n")

#	RescaledMatrix = Do Rescaling (Standardization) of Matrix3.
#	The code for Standardization is: x_standardization = (x – mean(X)) / (StdDev(X))
rescaled_matrix = target.join((matrix4 - mean) / std)

#	Print RescaledMatrix
print("Rescaled Matrix: \n", tabulate(rescaled_matrix), "\n")

#	NormalizedMatrix = Normalize Matrix3. The code for normalization is: x_Normalization = (x – min(X)) / ((max(X) – min(X)))
normalized_matrix = target.join((matrix4 - min) / max - min)

#	Print NormalizedMatrix
print("Normalized Matrix: \n", tabulate(normalized_matrix), "\n")

# Save output to excel file, each matrix in a different tab
with pd.ExcelWriter("Lab02-Q2-Excel_Output.xlsx") as writer:
    matrix1.to_excel(writer, sheet_name="Matrix_1")
    matrix2.to_excel(writer, sheet_name="Matrix_2")
    matrix3.to_excel(writer, sheet_name="Matrix_3")
    rescaled_matrix.to_excel(writer, sheet_name="Rescaled_Matrix")
    normalized_matrix.to_excel(writer, sheet_name="Normalized_Matrix")
