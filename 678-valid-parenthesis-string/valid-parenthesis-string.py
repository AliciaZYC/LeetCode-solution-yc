class Solution:
    def checkValidString(self, s: str) -> bool:
        brackets = []
        stars = []
        for i,ch in enumerate(s):
            if ch == '(':
                brackets.append(i)
            elif ch == "*":
                stars.append(i)
            else:
                if brackets:
                    brackets.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        while brackets and stars:
            if brackets.pop()>stars.pop():
                return False
        return not brackets