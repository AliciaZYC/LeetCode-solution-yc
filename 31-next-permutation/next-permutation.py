class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 步骤1：从后向前找第一个「相邻升序对」的左索引 i（即 nums[i] < nums[i+1]）
        # 此时 [i+1, end] 区间必为非递增序列（降序或相等）
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # 步骤2：若找到有效 i（非完全降序），在 [i+1, end] 中从后向前找第一个 > nums[i] 的元素
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:  # 注意：需严格大于（处理重复值）
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # 交换，使排列增大
        
        # 步骤3：将 [i+1, end] 区间反转（原为降序 → 反转为升序）
        # 作用：使后半部分变为最小字典序，确保得到「下一个」最小排列
        # 特殊情况：若 i = -1（完全降序），此步直接反转整个数组 → 得到最小排列
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        # 例如【3，4，2，1】。第一步找到3的位置。然后找到4，交换3和4，得到【4，3，2，1】，再反转得到【4，1，2，3】