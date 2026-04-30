class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 初始化最小前缀和数组，索引代表模k的余数
        # minSum[r] 表示所有索引模k等于r的位置中，最小的前缀和
        # 初始时 minSum[0] = 0（空前缀），其他为无穷大
        minSum = [inf]*(k-1)+[0]
        
        prefix, ans = 0, -inf  # prefix: 当前前缀和，ans: 最大子数组和
        
        for i, x in enumerate(nums):
            prefix += x  # 累加当前元素到前缀和
            
            ik = i % k  # 计算当前索引模k的余数
            
            # 关键思路：如果两个位置 i 和 j 满足 i%k == j%k，
            # 则子数组 [j+1, i] 的长度是 k 的倍数
            # 当前前缀和减去同余数的最小前缀和，就是符合条件的子数组和
            ans = max(ans, prefix - minSum[ik])
            
            # 更新该余数对应的最小前缀和
            minSum[ik] = min(prefix, minSum[ik])
        
        return ans