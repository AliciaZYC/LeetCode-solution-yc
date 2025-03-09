class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', '{':'}','[':']'}
        for c in s:
            if c in brackets.keys():
                stack.append(c)
            elif stack and c == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack
