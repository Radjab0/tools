matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2],]
new_matrix = [ [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0])) ]
print(new_matrix)
