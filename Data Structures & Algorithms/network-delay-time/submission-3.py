class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #djikistra:
        edges=collections.defaultdict(list)
        for u,v,t in times:
            edges[u].append((v,t))
        minheap=[(0,k)]
        visit=set()
        t=0
        while minheap:
            t1,n1=heapq.heappop(minheap)
            if n1 in visit:
                continue
            t=max(t,t1)
            visit.add(n1)
            for n2,t2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap,(t1+t2,n2))
        return t if len(visit)==n else -1


