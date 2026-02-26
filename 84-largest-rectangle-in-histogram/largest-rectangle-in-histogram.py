class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # left[i]：柱子i左侧第一个「严格小于」heights[i]的柱子索引（无则为-1）
        left = [-1] * n
        # right[i]：柱子i右侧第一个「严格小于」heights[i]的柱子索引（无则为n）
        right = [n] * n
        
        # ===== 步骤1：计算left数组（从左向右扫描）=====
        stack = []
        for i in range(n):
            # 维护单调递增栈：弹出所有≥当前高度的索引（确保栈顶是左侧最近的小于值）
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # 栈顶即为左侧边界（若栈空则保持-1）
            if stack:
                left[i] = stack[-1]
            stack.append(i)  # 当前索引入栈
        
        # ===== 步骤2：计算right数组（从右向左扫描）=====
        stack = []
        for i in range(n - 1, -1, -1):
            # 同样维护单调递增栈（从右视角）
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        # ===== 步骤3：计算最大矩形面积 =====
        max_area = 0
        for i in range(n):
            # 宽度 = (右侧边界 - 左侧边界 - 1) → 即能以heights[i]为高的连续区间长度
            width = right[i] - left[i] - 1
            max_area = max(max_area, width * heights[i])
        
        return max_area