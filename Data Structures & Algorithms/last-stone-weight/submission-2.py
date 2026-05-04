class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap)>1:
            a=heapq.heappop(maxHeap)
            b=heapq.heappop(maxHeap)
            val=a-b
            if val!=0:
                heapq.heappush(maxHeap,val)
        if maxHeap:
            res=-heapq.heappop(maxHeap)
        else:
            res=0
        return res    