from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.nSumTarget(nums, 3, 0, 0)
    def nSumTarget(self, nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
        sz = len(nums)
        res = []
        if n < 2 or sz < n:
            return res
        if n == 2:
            lo, hi = start, sz - 1
            while lo < hi:
                sum_val = nums[lo] + nums[hi]
                left, right = nums[lo], nums[hi]
                if sum_val < target:
                    # use while since there may be same value
                    while lo < hi and nums[lo] == left:
                        lo += 1
                elif sum_val > target:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                else:
                    res.append([left, right])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
        else:
            for i in range(start, sz):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sub = self.nSumTarget(nums, n - 1, i + 1, target - nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
        return res