class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        max_area=0
        q=collections.deque()

        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            area=1
            q.append((r,c))
            visit.add((r,c))
            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if (r<0 or r==rows or
                        c<0 or c==cols or
                        grid[r][c]==0 or
                        (r,c) in visit):
                        continue
                    visit.add((r,c))
                    q.append((r,c))
                    area+=1
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    max_area=max(max_area,bfs(r,c))
        return max_area

       