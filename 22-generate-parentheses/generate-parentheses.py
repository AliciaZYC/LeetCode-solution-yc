class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []  # 存储所有有效的括号组合结果
        
        # 回溯函数：构建当前括号序列
        # cur_string: 当前括号序列（用列表存储，便于回溯操作）
        # left_count: 已使用的左括号数量
        # right_count: 已使用的右括号数量
        def backtracking(cur_string, left_count, right_count):
            # 终止条件：当前序列长度达到 2n（n对括号）
            if len(cur_string) == 2 * n:
                answer.append("".join(cur_string))  # 转为字符串存入结果
                return
            
            # 【关键剪枝1】左括号未用完时，可添加左括号
            if left_count < n:
                cur_string.append("(")
                backtracking(cur_string, left_count + 1, right_count)
                cur_string.pop()  # 回溯：撤销选择
            
            # 【关键剪枝2】右括号数量必须小于左括号（保证有效性）
            if right_count < left_count:
                cur_string.append(")")
                backtracking(cur_string, left_count, right_count + 1)
                cur_string.pop()  # 回溯：撤销选择
        
        # 从空序列、0个左右括号开始构建
        backtracking([], 0, 0)
        return answer