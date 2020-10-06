import numpy as np

class MyMatrix:
    def __init__(self):
        # nothing here
        self.N = -1     # default value
        self.matrix = None

    def check_n_range_policy(self, N):
        if 3 < N < 8:
            return True
        else:
            return False

    def read_file(self, file_name):
        file_object = open(file_name, "r")
        all_numbers = []
        for line in file_object:
            # I assumed that numbers within files are int numbers
            line = list(map(int, line.strip().split()))
            all_numbers.extend(line)

        if len(all_numbers) < self.N ** 2:
            raise Exception("[ERROR] The input file " + file_name + " has less than" + str(self.N ** 2) +
                            "number in it.")
        else:
            # Now there is two possibility here:
            # first, I have N**2 numbers
            # second, I have more than N**2 number
            # by the way, we cover both outcomes
            mat = np.zeros((self.N, self.N))  # a new N*N matrix filled by zeros
            for i in range(self.N):
                for j in range(self.N):
                    mat[i, j] = all_numbers[i*self.N + j]

            return mat

    def get_matrix(self, N, file_name):
        if self.check_n_range_policy(N) == True:
            self.N = N
        elif N < 3:
            raise ValueError("Error: ***** This dimension is out of bound. The program stops in here.\n "
                             "(*********************** End of the Program ************************)")
        else:
            raise ValueError("Error: ***** We can only handle up to 8 dimensions at this time. The program stops"
                             " in here.\n"
                             "(*********************** End of the Program ************************)")

        self.matrix = self.read_file(file_name)

        return self.matrix

    def product(self, M1, M2):
        return np.matmul(M1, M2)

    def dot_product(self, M1, M2):
        return np.dot(M1, M2)

    def division(self, M1, M2):
        with np.errstate(divide='ignore'):
            result = np.divide(M1, M2)
            result = np.round(result, decimals=4)
            # now we mask bad results caused by 'division by zero' with "undef" string
            # if an element of M2 is 0 it causes np.Inf in result matrix
            # so I can find and bad results by 'M2 != 0' or 'result==np.Inf'
            return np.where(M2 != 0, result.astype(object), "undef")

    def change_some_elements_to_zero(self, M):
        M[2,0] = 0
        M[2,3] = 0
        M[4, 1] = 0
        return M


# driver part of code

n = int(input(">> Enter the dimension of your matrix:\t").strip())

myMatrix = MyMatrix()

M1 = myMatrix.get_matrix(n, "file1.txt")
M2 = myMatrix.get_matrix(n, "file2.txt")


M1_Multiply_M2 = myMatrix.product(M1, M2)
print("\nM1_Multiply_M2:")
print(M1_Multiply_M2)

M1_DotMultiply_M2 = myMatrix.dot_product(M1, M2)
print("\nM1_DotMultiply_M2:")
print(M1_DotMultiply_M2)


M1_Divde_M2 = myMatrix.division(M1, M2)
print("\nM1_Divde_M2:")
print(M1_Divde_M2)

print("\nPart b - step 13 (division by zero)\n")
M2 = myMatrix.change_some_elements_to_zero(M2)
final = myMatrix.division(M1, M2)
print(final)

