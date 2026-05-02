class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        cnt = 0
        while len(nums) > 1:
            isSorted = True
            minSum = float("inf")
            targetIndex = -1
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    isSorted = False
                pair = nums[i] + nums[i + 1]
                if pair < minSum:
                    minSum = pair
                    targetIndex = i
            if isSorted:
                break
            cnt += 1
            nums[targetIndex] = minSum
            nums.pop(targetIndex + 1)
        return cnt
                