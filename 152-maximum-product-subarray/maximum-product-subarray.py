class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        cmax=cmin=1
        for num in nums:
            temp=cmax*num
            cmax=max(cmin*num,temp,num)
            cmin=min(temp,cmin*num,num)
            res=max(res,cmax)
        return res