class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        res = set()
        for i in range(len(s) - k + 1):
            if s[i:i+k] not in res:
                res.add(s[i:i+k])
        return len(res) == 2**k