class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        max_area=0

        def dfs(r,c):
            area=1
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c]!= 1 or
                (r,c) in visit):
                return 0
            visit.add((r,c))
            area+=(dfs(r+1,c) +
                dfs(r-1,c) +
                dfs(r,c+1) +
                dfs(r,c-1))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    max_area=max(max_area,dfs(r,c))
        return max_area