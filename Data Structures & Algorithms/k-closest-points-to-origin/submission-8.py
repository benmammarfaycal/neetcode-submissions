class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        res=[]
        for x,y in points:
            d=((x-0)**2+(y-0)**2)
            minHeap.append([d,x,y])
        heapq.heapify(minHeap)
        for i in range(0,k):
            d,x,y=heapq.heappop(minHeap)
            res.append([x,y])
        return res