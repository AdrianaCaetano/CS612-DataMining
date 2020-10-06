You have been given a data file called “AlzheimerData.xlsx”. It is a matrix file with 25 rows (representing Drugs) and 16 columns (representing properties of the drug) for Alzheimer Disease to do data mining and create a model to predict if a drug can be used for Alzheimer disease or not. Step 1 is to clean the data. You are required to write a python program that does the following:

-	OriginalMatrix = read the data from the file
-	Print OriginalMatrix 

## Matrix1
- Use OriginalMatrix to remove the columns that only include Zero.
- Print Matrix1

## Matrix2
- Use Matrix1 to remove the columns in which they have at least 5 cells which are junks (non-numbers). 
- Otherwise, if they have less than 5 junk values, replace the junk values with zeros.
- Print Matrix2

## Matrix3
- Use Matrix2 to remove the rows in which they have at least 5 cells which are junks (non-numbers). 
- Otherwise, if they have less than 5 junk values, replace the junk values with zeros.
- Print Matrix3

## RescaledMatrix
- Do Rescaling (Standardization) of Matrix3. 
- The code for Standardization is: **x_standarization = (x – mean(X)) / (StdDev(X))**
- Print RescaledMatrix

## NormalizedMatrix 
- Normalize Matrix3. 
- The code for normalization is:
- The code for Standardization is: **x_Normalization = (x – min(X)) / ((max(X) – min(X)))**
- Print NormalizedMatrix
