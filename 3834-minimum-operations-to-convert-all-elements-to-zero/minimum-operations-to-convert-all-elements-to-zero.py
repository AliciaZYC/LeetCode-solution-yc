class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # The subarry must not contain 0
        # smaller numbers exist between two identical numbers. cannot do together
        s = []
        res = 0
        for num in nums:
            while s and s[-1] > num:
                s.pop()
            if num == 0:
                continue
            if not s or s[-1] < num:
                res += 1
                s.append(num)
        return res