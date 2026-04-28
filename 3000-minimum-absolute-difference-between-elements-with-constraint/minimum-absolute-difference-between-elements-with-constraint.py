class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        # Brute Force
        # n = len(nums)
        # res = float("inf")
        # for i in range(n):
        #     for j in range(i+x,n):
        #         res = min(res,abs(nums[i]-nums[j]))
        # return res
        S = SortedList()
        n = len(nums)
        res = float("inf")
        for i in range(x,n):
            S.add(nums[i-x])
            curr = nums[i]
            idx = S.bisect_left(curr)
            if idx < len(S):
                res = min(res,S[idx]-curr)
            if idx > 0:
                res = min(res,curr-S[idx-1])
            if res == 0:
                return 0
        return int(res)
