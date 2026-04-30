class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # 理论是：
        # 偶数个负数的话，是所有abs的和
        # 奇数个负数的话，是除了最大负数的所有abs之和 + 这个最大负数
        n = len(matrix)
        count = 0
        track = float("inf")
        res = 0
        for x in range(n):
            for y in range(n):
                res += abs(matrix[x][y])
                if matrix[x][y] <= 0:
                    count += 1
                track = min(track,abs(matrix[x][y]))
        if count%2 != 0:
            res -= 2* track
        return res