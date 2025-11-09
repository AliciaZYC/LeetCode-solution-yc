class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        low,high = matrix[0][0],matrix[-1][-1]
        while low < high:
            mid = low + (high-low)//2
            count = 0
            col = n-1
            for row in range(n):
                while col >= 0 and matrix[row][col]>mid:
                    col-=1
                count += (col+1)
            if count <k:
                low = mid+1
            else:
                high = mid
        return low