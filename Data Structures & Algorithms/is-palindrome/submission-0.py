class Solution:
    def isPalindrome(self, s: str) -> bool:
        b=""
        for a in s:
            if a.isalnum():
                b+=a
        b=b.lower()
        print(b)
        i=0
        z=len(b)
        for ch in reversed(range(z)):
            if b[i]!=b[ch]:
                return False
            i+=1
        return True