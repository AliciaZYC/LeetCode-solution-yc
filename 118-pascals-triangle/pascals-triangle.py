class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1])
        for i in range(numRows -1):
            newRow = [1]
            for j in range(i):
                newRow.append(res[i][j]+res[i][j+1])
            newRow.append(1)
            res.append(newRow)
        return res