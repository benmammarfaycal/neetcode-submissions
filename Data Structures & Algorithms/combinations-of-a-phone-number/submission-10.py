class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        curStr=[]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i):
            if i >= len(digits):
                res.append("".join(curStr))
                return
            for c in digitToChar[digits[i]]:
                curStr.append(c)
                backtrack(i + 1)
                curStr.pop()

        if digits:
            backtrack(0)
        return res