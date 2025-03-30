class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        if digits=="":
            return []
        def backtrack(combination,next_digit):
            if not next_digit:
                res.append(combination)
                return
            for letter in d[next_digit[0]]:
                backtrack(combination+letter,next_digit[1:])
        backtrack('',digits)
        return res