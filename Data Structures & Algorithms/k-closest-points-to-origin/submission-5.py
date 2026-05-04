class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        res=[]
        for x,y in points:
            d=((x-0)**2+(y-0)**2)
            minHeap.append([d,x,y])
        heapq.heapify(minHeap)
        while 0<k:
            y=heapq.heappop(minHeap)
            res.append([y[1],y[2]])
            k-=1
        return res