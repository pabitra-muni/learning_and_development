# change rows into columns and columns into rows in a [n, n] 2D array.

# 1 2 3       1 4 7
# 4 5 6   =>  2 5 8
# 7 8 9       3 6 9

# basically, we need to swap 4, 7 and 8 with 2, 3 and 6 respectively. And, keep other positions as is.
# that means, [0, 1] => [1, 0] , [0, 2] => [2, 0] and [1, 2] => [2, 1]
# so when, j > i then swap the values between [i][j] and [j][i]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matrix)
for i in range(n):
    for j in range(n):
        if j > i:
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

for i in range(n):
    print(matrix[i])