class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        # 边界处理：空矩阵直接返回0
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])          # 列数
        # heights[i] 表示以当前行为底、第i列向上连续'1'的个数
        # 末尾额外添加0：作为哨兵，确保最后一轮单调栈能清空所有有效柱子
        heights = [0] * (n + 1)
        ans = 0
        
        for row in matrix:
            # 步骤1：动态更新柱状图高度（核心转化）
            # 若当前元素为'1'，高度+1；否则重置为0（连续性中断）
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            # heights[n] 始终保持0（哨兵），无需更新
            
            # 步骤2：对当前行的柱状图应用「单调栈」求最大矩形（LeetCode 84解法）
            stack = [-1]  # 栈存索引；-1作为左边界哨兵（利用Python负索引：heights[-1] = heights[n] = 0）
            for i in range(n + 1):  # 遍历含哨兵的完整heights
                # 维护单调递增栈：当遇到更小高度时，计算以栈顶高度为高的最大矩形
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]      # 弹出栈顶，作为矩形高度
                    w = i - stack[-1] - 1         # 宽度 = 当前位置i - 新栈顶（左边界） - 1
                    ans = max(ans, h * w)
                stack.append(i)  # 当前索引入栈
        
        return ans