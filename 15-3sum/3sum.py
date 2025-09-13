from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.nSumTarget(nums,3,0,0)
    def nSumTarget(self, nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
        l = len(nums)
        res = []
        if n<2 or n>l:
            return res
        # base case
        if n == 2:
            low,high=start,l-1
            while low<high:
                sum_val = nums[low]+nums[high]
                left=nums[low]
                right=nums[high]
                if sum_val<target:
                    while low<high and nums[low]==left:
                        low+=1
                elif sum_val>target:
                    while low<high and nums[high]==right:
                        high -=1
                else:
                    res.append([left,right])
                    while low<high and nums[low]==left:
                        low+=1
                    while low<high and nums[high]==right:
                        high -=1
        else:
            for i in range(start,l):
                if i>start and nums[i]==nums[i-1]:
                    continue
                sub = self.nSumTarget(nums,n-1,i+1,target-nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
        return res