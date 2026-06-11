class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit=set()

        def dfs(n):
            if n in visit:
                return
            visit.add(n)
            for j in adj[n]:
                dfs(j)

        res=0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res+=1
        return res
