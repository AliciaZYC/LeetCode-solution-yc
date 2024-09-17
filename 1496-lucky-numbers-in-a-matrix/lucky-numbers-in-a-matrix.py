class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # return [x] if (x:=max(min(row) for row in matrix))==min(max(col) for col in zip(*matrix)) else []
        res=[]
        maxCol=[]
        m=len(matrix)
        n=len(matrix[0])
        for c in range(n):
            maxCol.append(max(matrix[x][c] for x in range(m)))
        for r in range(m):
            minVal=min(matrix[r])
            minIndex= matrix[r].index(minVal)
            if minVal == maxCol[minIndex]:
                res.append(minVal)
        return res