# create matrix A
A = np.array([(1, 2, 3), (4, 5, 6)])
print("Matrix A")
print(A)

# [[1 2 3]
#  [4 5 6]]

# create matrix B
B = np.array([(0, 5), (4, 9), (9, 0)])
print("Matrix B")
print(B)
# [[0 5]
#  [4 9]
#  [9 0]]

# product of A and B

C = Calculator.MatrixMultiply(A, B)
print("Product of A and B")
print(C)
# [[35 23]
#  [74 65]]
