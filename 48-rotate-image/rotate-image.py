class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #overturn
        n=len(matrix)
        start=0
        end=n-1
        while start<end:
            matrix[start],matrix[end]=matrix[end],matrix[start]
            start+=1
            end-=1
        #transpose
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]