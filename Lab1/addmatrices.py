def add_matrices(mat1, mat2):
  rows, cols = len(mat1), len(mat1[0])
  result = [[mat1[i][j] + mat2[i][j] for j in range(cols)] for i in range(rows)]
  return result
  
  
rows, cols = map(int, input("Enter the number of rows and columns: ").split())
print("Enter the elements of the first matrix row-wise: ")
matrix1 = [list(map(int, input().split())) for _ in range(rows)]
print("Enter the elements of the second matrix row-wise: ")
matrix2 = [list(map(int, input().split())) for _ in range(rows)]


result = add_matrices(matrix1, matrix2)
print("Resultant matrix: ")
for row in result: 
  print(row)
  