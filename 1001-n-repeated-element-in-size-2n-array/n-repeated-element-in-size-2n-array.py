class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set(nums)
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                return num