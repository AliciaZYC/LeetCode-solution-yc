class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 边界条件：如果t为空或s长度小于t，不可能包含t的所有字符
        if t == "" or len(s) < len(t): 
            return ""
        # needmap: 记录字符串t中每个字符需要的数量
        # havemap: 记录当前窗口中每个字符的数量
        needmap, havemap = {}, {}         
        # 统计t中每个字符出现的次数
        for c in t:
            needmap[c] = needmap.get(c, 0) + 1
            havemap[c] = 0         
        # need: t中不同字符的种类数
        # have: 当前窗口中已经满足数量要求的字符种类数
        need, have = len(needmap), 0         
        # 滑动窗口的左指针
        l = 0         
        # res: 存储最小窗口子串
        # resLen: 最小窗口的长度，初始化为无穷大
        res, resLen = "", float("infinity")        
        # 右指针遍历字符串s
        for r in range(len(s)):
            # 如果当前字符是t中需要的字符
            if s[r] in needmap:
                havemap[s[r]] += 1
                # 如果当前字符的数量刚好满足需求
                if havemap[s[r]] == needmap[s[r]]: 
                    have += 1             
            # 当窗口包含了t的所有字符时，尝试收缩窗口
            while(have == need): 
                # 更新最小窗口
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = s[l:r+1]                
                # 左指针右移，缩小窗口
                if s[l] in havemap:
                    havemap[s[l]] -= 1
                    # 如果移除后不再满足该字符的数量要求
                    if needmap[s[l]] > havemap[s[l]]: 
                        have -= 1
                l += 1        
        return res