class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 辅助函数：判断能否将数组分割成 ≤k 段，且每段和 ≤ lim
        def canSplit(lim: int, nums, k):
            curr_sum = 0  # 当前子数组累加和
            piece = 1     # 子数组计数（初始为1段）
            for num in nums:
                # 若加入当前数会超限 → 开启新子数组
                if curr_sum + num > lim:
                    curr_sum = num  # 新子数组从当前数开始
                    piece += 1
                    # 子数组数量已超k，无法满足条件
                    if piece > k:
                        return False
                else:
                    curr_sum += num  # 累加到当前子数组
            return True  # 成功分割为 ≤k 段
        
        # 二分搜索边界初始化
        left = max(nums)   # 下界：至少为单个元素最大值（k = len(nums)时）
        right = sum(nums)  # 上界：整个数组和（k = 1时）
        
        # 二分搜索：寻找满足条件的最小最大子数组和
        while left < right:
            mid = left + (right - left) // 2  # 防溢出写法（Python虽无需，但为良好习惯）
            # 验证：若mid可作为最大子数组和上限
            if canSplit(mid, nums, k):
                right = mid  # 尝试更小的上限（答案在左半区）
            else:
                left = mid + 1  # mid太小，需增大上限（答案在右半区）
        
        return left  # left即为最小化的最大子数组和