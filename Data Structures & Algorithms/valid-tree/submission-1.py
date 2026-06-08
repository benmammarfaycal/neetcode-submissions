class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj={i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit=set()
        def dfs(n,prev):
            if n in visit:
                return False
            visit.add(n)
            for j in adj[n]:
                if j==prev:
                    continue
                if not dfs(j,n):
                    return False
            return True
        return dfs(0,-1) and len(visit)==n
                
            

