# https://leetcode.com/problems/pascals-triangle/description/?envType=problem-list-v2&envId=array

class PascalTriangle:
    def createPascalTriangle(self, numRows: int) -> list[list[int]]:
        rowNumber = 1
        result = []
        while rowNumber <= numRows:
            cRow = []
            if len(result) == 0:
                cRow.append(1)
            else:
                pRow = result[rowNumber - 2] # as array index is zero based
                pLength = len(pRow)
                for i in range(pLength + 1): # because next row would have one additional element
                    if i == 0 or i == pLength:
                        cRow.append(1)
                    else:
                        cRow.append(pRow[i] + pRow[i - 1])

            result.append(cRow)
            rowNumber += 1
        return result

        
