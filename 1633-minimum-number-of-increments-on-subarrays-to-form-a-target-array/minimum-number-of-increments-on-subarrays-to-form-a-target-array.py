class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        prev = 0
        for x in target:
            if x > prev:
                res += x - prev
            prev = x
        return res