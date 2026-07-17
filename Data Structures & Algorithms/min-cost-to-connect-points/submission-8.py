class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges=collections.defaultdict(list)
        for p1 in points:
            for p2 in points:
                if p1==p2:
                    continue
                x1,y1=p1
                x2,y2=p2
                d=abs(x1-x2)+abs(y1-y2)
                edges[(x1,y1)].append(((x2,y2),d))
        visit=set()
        x,y=points[0]
        minheap=[(0,(x,y))]
        res=0
        while minheap:
            w1,p1=heapq.heappop(minheap)
            if p1 in visit:
                continue
            res+=w1
            visit.add(p1)
            if len(visit)==len(points):
                break
            for p2,w2 in edges[p1]:
                if p2 not in visit:
                    heapq.heappush(minheap,(w2,p2))

        return res