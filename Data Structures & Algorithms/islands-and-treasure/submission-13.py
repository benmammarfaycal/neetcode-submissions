class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        q=collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
        
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        m=1
        while q:
            for _ in range(len(q)):
                row,col=q.popleft()
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if(r<0 or r==rows or
                        c<0 or c==cols or
                        grid[r][c]!=(2**31 - 1)):
                        continue
                    q.append((r,c))
                    grid[r][c]=m
            m+=1

