class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = defaultdict(int)
        for i in range(len(s) - minSize + 1):
            substr = s[i:i + minSize]
            unique = set(substr)
            if len(unique) <= maxLetters:
                freq[substr] += 1
        return max(freq.values(),default=0)