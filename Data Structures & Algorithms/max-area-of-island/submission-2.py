class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        max_area=0
        visit=set()
        rows,cols=len(grid),len(grid[0])

        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            visit.add((r,c))
            area=1
            while q:
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                row,col=q.popleft()
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c]==1  and
                        (r,c) not in visit):
                        area+=1
                        visit.add((r,c))
                        q.append((r,c))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    max_area=max(max_area,bfs(r,c))
        return max_area