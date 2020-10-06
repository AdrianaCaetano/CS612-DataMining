# Write an object-oriented program in python that does the following:

# Part A 
- Interactively get a positive number, “n”, from a user

If “n” is less or equal to 3 or greater  than to equal to 8 report an error and quit the program.
Otherwise, try to get n*n numbers from the first file. 
For example, if n=6 you are required to get 36 numbers from the first file in order to make a 6 by 6 matrix. 
Therefore, if there are less than 36 numbers in the file, report error and quit the program
If there are more than 36 numbers (for size 6) from the file, get the first 36 numbers, make a matrix of 6 by 6 and ignore the other numbers

# Part B
- Create an object of the class called myMatrix and do the following:

1)	N = get a size for a square matrix # enter 6 
2)	Create an object call it myMatrix
3)	M1 = myMatrix.GetMatrix(N, file1)
4)	M2 = myMatrix.GetMatrix(N, file2)
5)	Print M1
6)	Print M2
7)	M1_Multiply_M2 = myMatrix.Product(M1, M2)
8)	Print M1_Multiply_M2
9)	M1_DotMultiply_M2 = myMatrix.DotProduct(M1, M2)
10)	Print M1_DotMultiply_M2
11)	M1_Divde_M2 = myMatrix.Division(M1, M2)
12)	Print M1_Divde_M2 (show it with at least 2 significant digits) 
