class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        res=sorted(count,key=count.get,reverse=True)
        i=0
        a=[]
        while i<k:
            a.append(res[i])
            i+=1
        return a