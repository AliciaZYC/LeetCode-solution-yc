class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        # dict_trans = {}
        # for i in range(len(pattern)):
        #     if pattern[i] in dict_trans:
        #         if dict_trans[pattern[i]] != s[i]:
        #             return False
        #     else:
        #         if s[i] in dict_trans.values():
        #             return False
        #         dict_trans[pattern[i]] = s[i]
        # return True
        a = set(zip(s,pattern))
        b = set(s)
        c = set(pattern)
        return len(a)==len(b)==len(c)

        
