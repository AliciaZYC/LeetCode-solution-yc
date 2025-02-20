class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        end = 0
        far = 0
        jumps = 0
        for i in range(n-1):
            far = max(nums[i]+i,far)
            if end == i:
                jumps +=1
                end = far
        return jumps