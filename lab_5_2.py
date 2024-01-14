rows = 7
columns = 7

matrix = [[0] * columns for _ in range(rows)]

for i in range(rows):
  for j in range(columns):
    if i + j < rows:
      matrix[i][j] = i + j + 1

# Виведення масиву на екран
for i in range(rows):
  for j in range(columns):
    print(matrix[i][j], end=' ')
  print()
