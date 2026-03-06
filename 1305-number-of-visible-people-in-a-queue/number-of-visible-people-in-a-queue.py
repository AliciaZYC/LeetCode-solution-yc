class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n          # res[i]：第i个人向右能看到的人数
        stack = []             # 单调递减栈（从栈底→栈顶：高度递减），存储右侧"可见"的人的高度
        
        # 从右向左遍历（i为原数组索引的镜像位置）
        for idx, height in enumerate(reversed(heights)):
            # 步骤1：弹出所有比当前人矮的右侧人员
            # 原因：当前人能看到这些矮的人，且这些人会被当前人"挡住"，对更左侧的人不可见
            while stack and height > stack[-1]:
                stack.pop()
                res[idx] += 1  # 每弹出1人，当前人可见人数+1
            
            # 步骤2：若栈非空，说明存在第一个≥当前人的右侧人员
            # 当前人能看到此人（视线被此人阻挡，但此人本身可见）
            if stack:
                res[idx] += 1
            
            # 步骤3：当前人入栈（作为左侧人员的潜在"阻挡者"）
            stack.append(height)
        
        # 结果需反转：因遍历时使用reversed，res[0]对应原数组最右端
        return res[::-1]