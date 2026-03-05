from collections import deque  # 需确保导入（题目代码隐含）

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()      # 双端队列：存储「窗口内元素的索引」，队首始终是当前窗口最大值的索引
        result = []
        
        for i in range(len(nums)):
            # 步骤1：移除队首过期索引（已滑出窗口左边界）
            # 窗口范围 [i-k+1, i]，若队首索引 ≤ i-k 则失效
            if dq and dq[0] <= i - k:
                dq.popleft()
            
            # 步骤2：维护单调递减队列（从队尾弹出所有 ≤ 当前值的索引）
            # 原理：若 nums[j] ≤ nums[i] 且 j < i，则 j 永远不可能成为后续窗口的最大值
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            
            # 步骤3：当前索引入队（此时队列保持「索引递增、对应值递减」）
            dq.append(i)
            
            # 步骤4：窗口形成后（i ≥ k-1），记录当前窗口最大值（队首索引对应值）
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result