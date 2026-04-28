class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        # pre[i] 表示：在位置 i-1 左侧（包括i-1），最后一个 '0' 出现的位置索引
        # pre[0] = -1 表示初始状态，没有找到0
        pre = [-1] * (n+1)
        
        # 预处理：构建 pre 数组
        # 如果当前位置是第一个字符或者前一个字符是 '0'，则当前位置就是最后一个0的位置
        # 否则继承前面记录的最后一个0的位置
        for i in range(n):
            if i == 0 or s[i-1] == "0":
                pre[i+1] = i
            else:
                pre[i+1] = pre[i]
        
        res = 0  # 结果计数器
        
        # 固定右端点为 i-1（即考虑以 s[i-1] 结尾的所有子串）
        for i in range(1, n+1):
            # cnt0 初始化为右端点本身是否为 '0'
            cnt0 = 1 if s[i-1] == "0" else 0
            
            # j 表示当前考虑的子串左端点的下一个位置
            j = i
            
            # 枚举子串中 '0' 的个数，当 0 的个数的平方超过字符串总长度时停止
            while j > 0 and cnt0 * cnt0 <= n:
                # 计算当前子串中 '1' 的个数
                # (i - pre[j]) 是从最后一个0到右端点的长度
                cnt1 = (i - pre[j]) - cnt0
                
                # 检查是否满足主导条件：0的个数的平方 <= 1的个数
                if cnt0 * cnt0 <= cnt1:
                    # 计算满足条件的子串数量
                    # min(j-pre[j], cnt1-cnt0*cnt0+1) 表示可以向左扩展的最大步数
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                
                # 移动到前一个 '0' 的位置，增加0的计数
                j = pre[j]
                cnt0 += 1
        
        return res