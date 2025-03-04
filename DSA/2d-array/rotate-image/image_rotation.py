# https://leetcode.com/problems/rotate-image/?envType=problem-list-v2&envId=array

class ImageRotation:
    def rotate(self, matrix: list[list[int]]):
        n = len(matrix)
        if n > 1:
            left = 0
            right = n-1
            while left < right:
              for r in range(n-1):
                temp = matrix[left][left]
                i = left + 1
                while i <= right:
                    matrix[i-1][left] = matrix[i][left] # PUSH UP
                    i += 1

                i = left + 1
                while i <= right:
                    matrix[right][i-1] = matrix[right][i] # PUSH LEFT
                    i += 1

                i = right - 1
                while i >= 0:
                    matrix[i+1][right] = matrix[i][right] # PUSH DOWN
                    i -= 1

                i = right - 1
                while i > 0:
                    matrix[left][i+1] = matrix[left][i] # PUSH RIGHT
                    i -= 1

                matrix[left][left+1] = temp

              left += 1
              right -= 1
              n -= 2



