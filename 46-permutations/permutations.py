class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 定义回溯函数，用于生成从 start 开始的所有排列
        def backtrack(start):
            # 如果 start 到达了 nums 的末尾，说明生成了一个完整的排列
            if start == len(nums):
                res.append(nums[:])  # 将当前排列加入结果（注意要使用 nums[:] 复制列表）
                return
            
            # 遍历所有可以交换的位置
            for i in range(start, len(nums)):
                # 交换当前位置 start 和 i，使 i 元素放到当前位置
                nums[start], nums[i] = nums[i], nums[start]
                # 继续递归处理下一个位置
                backtrack(start + 1)
                # 回溯：将交换的元素换回来，恢复现场
                nums[start], nums[i] = nums[i], nums[start]

        res = []  # 用于存储所有的排列结果
        backtrack(0)  # 从索引 0 开始生成排列
        return res  # 返回所有排列
