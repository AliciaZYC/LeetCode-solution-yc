class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # 栈：存储字符、数字片段、已解码的子串
        
        for char in s:
            # 非结束符直接入栈（包括字母、数字、'['）
            if char != "]":
                stack.append(char)
            else:
                # ===== 步骤1：弹出当前括号内的字符串（逆序拼接）=====
                curr_str = ""
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str  # 头插保证顺序
                stack.pop()  # 弹出 '['
                
                # ===== 步骤2：弹出重复次数（多位数字需逆序拼接）=====
                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num  # 头插还原数字顺序
                repeat_count = int(curr_num)
                
                # ===== 步骤3：解码并压回栈 =====
                decoded = curr_str * repeat_count
                stack.append(decoded)  # 作为整体参与外层解码
        
        # 栈中剩余元素拼接即为最终结果（无嵌套时直接是原字符）
        return "".join(stack)

# 栈变化过程：
# 初始: []
# → 遇'3','[','a','2','[','c' 全部入栈 → ['3','[','a','2','[','c']
# → 遇']'：弹出'c'+'[' → curr_str="c"；弹出'2' → decoded="cc" → 压栈 → ['3','[','a','cc']
# → 遇']'：弹出"cc"+'a'+'[' → curr_str="acc"；弹出'3' → decoded="accaccacc" → 压栈
# 最终: ["accaccacc"] → join → "accaccacc"