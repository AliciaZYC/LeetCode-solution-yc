class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        left = {}
        right = {}
        ans = 0
        for num in nums:
            right[num] = right.get(num, 0) + 1
        for num in nums:
            right[num] -= 1
            need = num * 2
            ans = (ans + left.get(need, 0) * right.get(need, 0)) % MOD
            left[num] = left.get(num, 0) + 1
        return ans