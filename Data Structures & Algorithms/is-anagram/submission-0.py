class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=sorted(s)
        t2=sorted(t)
        if s1==t2:
            return True
        else:
            return False