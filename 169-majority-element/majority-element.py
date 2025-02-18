class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = 0
        count =0
        for i in range(len(nums)):
            if count == 0:
                target = nums[i]
                count =1
            elif target != nums[i]:
                count -=1
            else:
                count +=1
        return target
      