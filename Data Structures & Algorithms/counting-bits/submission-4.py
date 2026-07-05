class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            x=i
            s=0
            while x>0:
                if x%2==1:
                    s+=1
                x=x>>1
            res.append(s)
        return res