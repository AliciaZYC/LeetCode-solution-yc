class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowSet = set()
        colSet = set()
        for i in range(len(matrix)):  # Iterate over rows
            for j in range(len(matrix[0])):  # Iterate over columns
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
        for row in range(len(matrix)):
            if row in rowSet:
                for j in range(len(matrix[0])):
                    matrix[row][j]=0
        for col in range(len(matrix[0])):
            if col in colSet:
                for i in range(len(matrix)):
                    matrix[i][col]=0

        