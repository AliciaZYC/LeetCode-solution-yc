class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        count = 0
        while fast < len(nums):
            if nums[fast]!= nums[slow]:
                slow +=1
                nums[slow] = nums[fast]
            elif slow < fast and count < 2:
                slow +=1
                nums[slow] = nums[fast]
            fast +=1
            count +=1
            if fast < len (nums) and nums[fast]!=nums[fast-1]:
                count =0
        return slow+1