#https://leetcode.com/problems/unique-paths-ii/?envType=problem-list-v2&envId=array

class UniquePath2:
    def __init__(self):
        self.path_count = {}
        self.dead_ends = []
    
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        return self.__calculatePathCount(obstacleGrid, 0, 0)


    def __calculatePathCount(self, obstacleGrid: list[list[int]], row:int, col: int) -> int:
        rowCount = len(obstacleGrid)
        colCount = len(obstacleGrid[0])
        
        if row >= rowCount or col >= colCount:
            # out of bound indices
            return 0
        
        key = self.__getKey(row, col)
        if key in self.dead_ends:
            return 0
        if obstacleGrid[row][col] == 1:
            # its a dead end
            self.dead_ends.append(key)
            return 0
        if key in self.path_count:
            # value already calculated
            return self.path_count.get(key)
        
        if row == rowCount - 1 and col == colCount - 1:
            # we reached end element
            return 1
        
        # move down -> row increases but col remains same
        # move right -> col increases but row remains same
        pathCount = self.__calculatePathCount(obstacleGrid, row + 1, col) + self.__calculatePathCount(obstacleGrid, row, col + 1)
        self.path_count[key] = pathCount
        return pathCount
        
        
    def __getKey(self, row:int, col:int) -> str:
        return f"r{row}c{col}"

