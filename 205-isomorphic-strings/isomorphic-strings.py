class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if len(s)!=len(t) or len(set(s))!=len(set(t)):
        #     return False
        # else:
        #     hash_map={}
        #     for i in range(len(s)):
        #         # hash_map[s[i]] = t[i]
        #         if s[i] in hash_map.keys():
        #             if t[i] not in hash_map.values() or hash_map[s[i]] != t[i]:
        #                 return False
        #         elif t[i] in hash_map.values():
        #             return False
        #         else:
        #             hash_map[s[i]] = t[i]
        #     return True
        a = set(zip(s,t))
        b = set(s)
        c = set(t)
        return len(a)==len(b)==len(c)