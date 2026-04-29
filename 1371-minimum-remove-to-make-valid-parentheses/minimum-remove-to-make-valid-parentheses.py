class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # stores indices of unmatched '('
        res = list(s)
        
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    res[i] = ""  # unmatched ')', remove in place
        
        for i in stack:
            res[i] = ""  # unmatched '(', remove in place
        
        return "".join(res)