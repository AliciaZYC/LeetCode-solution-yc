class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        plus=0
        for i in range(len(nums)):
            if plus <0:
                plus=0
            plus+=nums[i]
            res=max(res,plus)
        return res