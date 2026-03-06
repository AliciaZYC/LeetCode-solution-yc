class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 排序策略：宽度升序 + 高度降序
        # 原因：宽度相同时，高度降序可避免相同宽度的信封被选入同一序列（因高度需严格递增）
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        res = []  # 维护高度的"潜在LIS"：res[i] = 长度为i+1的递增子序列的最小末尾高度
        
        for _, h in envelopes:  # 宽度已由排序保证，仅处理高度
            # 二分查找：在res中找第一个 >= h 的位置（严格递增LIS需替换相等值）
            l, r = 0, len(res) - 1
            while l <= r:
                mid = (l + r) //2
                if res[mid] >= h:
                    r = mid - 1
                else:
                    l = mid + 1
            idx = l  # l即为插入位置（第一个>=h的位置）
            
            # 更新res：维持"最小末尾高度"性质
            if idx == len(res):
                res.append(h)  # 可扩展LIS长度
            else:
                res[idx] = h   # 替换使后续更易接续（含相等高度：严格递增需替换）
        
        return len(res)  # res长度 = 最长严格递增子序列长度 = 最大嵌套层数