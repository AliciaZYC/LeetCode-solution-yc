class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        left =0
        res = float('inf')
        for right in range(len(nums)):
            s += nums[right]
            while s >= target:
                res = min(res,right -left +1)
                s -= nums[left]
                left +=1
        return 0 if res ==float('inf') else res
