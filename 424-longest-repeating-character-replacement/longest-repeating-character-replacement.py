class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        freq = {}
        max_freq = 0
        res = 0
        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end],0)+1
            max_freq = max(max_freq,freq[s[end]])
            is_valid = (end+1-start-max_freq<=k)
            if not is_valid:
                freq[s[start]]-=1
                start+=1
            res = end+1-start
        return res