class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
        }   

        for c in s:
            if c in mapping:  # parenthèse fermante
                if not stack or stack[-1] != mapping[c]:
                    return False
                stack.pop()
            else:  # parenthèse ouvrante
                stack.append(c)

        return len(stack) == 0