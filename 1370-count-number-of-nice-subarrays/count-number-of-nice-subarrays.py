class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 将所有数字转换为0（偶数）或1（奇数）
        # 这样问题就转化为：找出和为k的子数组个数
        for i in range(len(nums)):
            nums[i] %= 2
        
        # prefix_count[i] 表示前缀和为i的子数组个数
        # 初始化数组，长度为 len(nums) + 1，因为前缀和最大可能为 len(nums)
        prefix_count = [0] * (len(nums) + 1)
        
        # 前缀和为0的子数组初始有1个（空数组）
        prefix_count[0] = 1
        
        # s: 当前的前缀和（即从开始到当前位置的奇数个数）
        # ans: 最终答案，记录满足条件的子数组个数
        s, ans = 0, 0
        
        # 遍历数组中的每个元素
        for num in nums:
            # 更新前缀和（如果是奇数则+1，偶数则+0）
            s += num
            
            # 如果当前前缀和 >= k，说明可能存在满足条件的子数组
            # 寻找所有前缀和为 s-k 的位置，它们到当前位置的子数组恰好包含k个奇数
            if s >= k:
                ans += prefix_count[s-k]
            
            # 更新前缀和为s的子数组个数
            prefix_count[s] += 1
        
        return ans

"""
算法思路：
1. 问题转化：将原数组中的偶数变为0，奇数变为1，问题转化为寻找和为k的子数组个数

2. 前缀和思想：
   - 如果从位置i到位置j的子数组包含k个奇数
   - 那么 prefix_sum[j] - prefix_sum[i-1] = k
   - 即 prefix_sum[i-1] = prefix_sum[j] - k

3. 使用哈希表（这里用数组）记录每个前缀和出现的次数
   - 遍历到位置j时，查找有多少个位置的前缀和等于 current_sum - k
   - 这些位置都可以作为子数组的起始位置

时间复杂度：O(n)，只需要遍历一次数组
空间复杂度：O(n)，需要存储前缀和计数数组
"""