# https://leetcode.com/problems/rotate-image/?envType=problem-list-v2&envId=array

class ImageRotation:
    def rotate(self, matrix: list[list[int]]):
        n = len(matrix)
        if n > 1:
            for r in range(n-1):
              temp = matrix[0][0]
              i = 1
              while i <= n-1:
                  matrix[i-1][0] = matrix[i][0] # PUSH UP
                  i += 1

              i = 1
              while i <= n-1:
                  matrix[n-1][i-1] = matrix[n-1][i] # PUSH LEFT
                  i += 1

              i = n-2
              while i >= 0:
                  matrix[i+1][n-1] = matrix[i][n-1] # PUSH DOWN
                  i -= 1

              i = n-2
              while i > 0:
                  matrix[0][i+1] = matrix[0][i] # PUSH RIGHT
                  i -= 1

              matrix[0][1] = temp



