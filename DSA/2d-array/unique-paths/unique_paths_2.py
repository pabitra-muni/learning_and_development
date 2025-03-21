#https://leetcode.com/problems/unique-paths-ii/?envType=problem-list-v2&envId=array

class UniquePath2:
    def __init__(self):
        self.path_count = {}
    
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        return self.__calculatePathCount(obstacleGrid, 0, 0)


    def __calculatePathCount(self, obstacleGrid: list[list[int]], row:int, col: int) -> int:
        rowCount = len(obstacleGrid)
        colCount = len(obstacleGrid[0])
        
        key = self.__getKey(row, col)
        if obstacleGrid[row][col] == 1:
            # its a dead end
            return 0
        if key in self.path_count:
            # value already calculated
            return self.path_count.get(key)
        
        if row == rowCount - 1 and col == colCount - 1:
            # reached end element
            return 1
        
        # move down -> row increases but col remains same
        # move right -> col increases but row remains same
        down = 0 if row >= rowCount - 1 else self.__calculatePathCount(obstacleGrid, row + 1, col)
        right = 0 if col >= colCount - 1 else self.__calculatePathCount(obstacleGrid, row, col + 1)
        pathCount = down + right
        self.path_count[key] = pathCount
        return pathCount
        
        
    def __getKey(self, row:int, col:int) -> str:
        return f"r{row}c{col}"

    def __calculatePathCountUsingDP(self, obstacleGrid: list[list[int]]) -> int:

        """
        This function calculates the number of unique paths from the top-left corner to the bottom-right corner
        of a grid, considering obstacles. The grid is represented by a 2D list where 1 represents an obstacle
        and 0 represents a free space.

        The algorithm uses dynamic programming to solve the problem efficiently. Here's a step-by-step explanation:

        1. Determine the number of rows (rowCount) and columns (colCount) in the obstacleGrid.
        2. Check if the starting cell (top-left corner) has an obstacle. If it does, return 0 because no paths are possible.
        3. Initialize a 1D list (dp) of size colCount with all elements set to 0. This list will store the number of unique paths to each cell in the current row.
        4. Set the first element of dp to 1, as there is exactly one way to reach the starting cell (if it is not an obstacle).
        5. Iterate through each cell in the grid using nested loops:
            a. For each cell (i, j), check if it contains an obstacle (obstacleGrid[i][j] == 1). If it does, set dp[j] to 0 because no paths can pass through this cell.
            b. If the cell does not contain an obstacle and it is not in the first column (j > 0), update dp[j] by adding the value of the previous cell in the same row (dp[j-1]). This accounts for the paths coming from the left.
        6. After processing all cells, the last element of dp (dp[colCount-1]) will contain the number of unique paths to the bottom-right corner of the grid.
        7. Return the value of dp[colCount-1] as the result.

        Example:
        Consider the following grid:
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        The dp array will be updated as follows:
        Initial dp: [1, 0, 0]
        After processing row 0: [1, 1, 1]
        After processing row 1: [1, 0, 1]
        After processing row 2: [1, 1, 2]
        The number of unique paths to the bottom-right corner is 2.
        """

        rowCount = len(obstacleGrid)
        colCount = len(obstacleGrid[0])
        
        # If the starting cell has an obstacle, then return 0 as there are no paths.
        if obstacleGrid[0][0] == 1:
            return 0
        
        # Initialize the DP array with 0s.
        dp = [0] * colCount
        dp[0] = 1
        
        # Fill the dp array
        for i in range(rowCount):
            for j in range(colCount):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        
        return dp[colCount-1]