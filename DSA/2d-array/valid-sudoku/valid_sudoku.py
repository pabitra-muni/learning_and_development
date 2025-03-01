#https://leetcode.com/problems/valid-sudoku/description/?envType=problem-list-v2&envId=array

class Sudoku:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        colMap = {}
        boxMap = {}
        for i in range(9):
            cRow = board[i]
            for j in range(9):
                value = cRow[j]
                if value != ".":
                    #check same row
                    if cRow.count(value) > 1:
                        return False
                    #check same column
                    if not colMap.get(j):
                        colMap[j] = self.__getColumnValues(board, j)
                    if colMap[j].count(value) > 1:
                        return False
                    #check same box
                    rowRange = self.__getBoxRange(i)
                    colRange = self.__getBoxRange(j)
                    boxKey = self.__getBoxKey(rowRange, colRange)
                    if not boxMap.get(boxKey):
                        boxMap[boxKey] = self.__getBoxValues(board, rowRange, colRange)
                    if boxMap[boxKey].count(value) > 1:
                        return False
        return True

        
    def __getColumnValues(self, board: list[list[str]], col: int) -> list[int]:
        values = []
        for row in board:
            values.append(row[col])
        return values
    
    def __getBoxValues(self, board: list[list[str]], rowRange: list[int], colRange: list[int]) -> list[int]:
        values = []
        for i in range(rowRange[0], rowRange[1] + 1):
            for j in range(colRange[0], colRange[1] + 1):
                values.append(board[i][j])
        return values
    
    def __getBoxRange(self, key: int) -> list[int]:
        val = (key // 3) * 3
        return [val, val + 2]
    
    def __getBoxKey(self, rowRange: list[int], colRange: list[int]) -> str:
        return f"{rowRange[0]}{rowRange[1]}{colRange[0]}{colRange[1]}"