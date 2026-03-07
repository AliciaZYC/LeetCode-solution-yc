class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] 定义：以 nums[i] 结尾的最长严格递增子序列的长度
        # 初始化：每个元素自身构成长度为1的子序列
        dp = [1] * len(nums)
        
        # 外层遍历：计算每个位置 i 的 dp 值
        for i in range(len(nums)):
            # 内层遍历：检查 i 之前所有位置 j
            for j in range(i):
                # 状态转移：若 nums[i] > nums[j]（严格递增）
                # 则可将 nums[i] 接在以 nums[j] 结尾的子序列后，长度+1
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # 全局最优解：dp 数组中的最大值即为答案
        return max(dp)