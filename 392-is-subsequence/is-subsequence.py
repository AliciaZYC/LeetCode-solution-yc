class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        for i in range(len(t)):
            if j==len(s):
                return True
            elif t[i] == s[j]:
                j+=1
        return j==len(s)  