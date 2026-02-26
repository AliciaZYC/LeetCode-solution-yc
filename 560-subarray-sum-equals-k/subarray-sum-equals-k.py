class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0          # 记录满足条件的子数组数量
        psum = 0           # 当前前缀和（从索引0到当前位置的累加和）
        hashmap = {0: 1}   # 哈希表：key=前缀和, value=该前缀和出现的次数；初始化{0:1}处理从开头开始的子数组
        
        for num in nums:
            psum += num    # 更新当前前缀和
            
            # 【核心逻辑】若存在前缀和 psum - k，说明有子数组和为k
            # 例如：当前psum=10, k=3 → 需找psum=7的位置，10-7=3即为目标子数组
            count += hashmap.get(psum - k, 0)
            
            # 记录当前前缀和出现次数（为后续查找提供依据）
            hashmap[psum] = hashmap.get(psum, 0) + 1
        
        return count