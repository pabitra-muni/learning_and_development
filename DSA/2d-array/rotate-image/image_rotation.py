# https://leetcode.com/problems/rotate-image/?envType=problem-list-v2&envId=array

"""
the idea is to rotate the outer boundary first i.e. (0, 0) and (n-1, n-1)
then move to the next inner boundary and rotate it i.e. (1, 1) and (n-2, n-2)
....
....
keep moving the inner boundaries and rotate them until size=2
"""

class ImageRotation:
    def rotate(self, matrix: list[list[int]]):
        n = len(matrix)
        if n > 1:
            x = 0
            y = n-1
            while x < y:
              for rotation in range(n-1):
                temp = matrix[x][x]
                i = x + 1
                while i <= y:
                    matrix[i-1][x] = matrix[i][x] # PUSH UP
                    i += 1

                i = x + 1
                while i <= y:
                    matrix[y][i-1] = matrix[y][i] # PUSH LEFT
                    i += 1

                i = y - 1
                while i >= x:
                    matrix[i+1][y] = matrix[i][y] # PUSH DOWN
                    i -= 1

                i = y - 1
                while i > x:
                    matrix[x][i+1] = matrix[x][i] # PUSH RIGHT
                    i -= 1

                matrix[x][x+1] = temp

              x += 1
              y -= 1
              n -= 2



