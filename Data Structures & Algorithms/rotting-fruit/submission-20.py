class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        q=collections.deque()
        fresh=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))
                    
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        m=0
        while q and fresh>0:
            for i in range(len(q)):
                row,col=q.popleft()
                for dr,dc in directions:
                    r,c=row+dr,col+dc
                    if(r<0 or c<0 or
                        r==rows or c==cols or
                        grid[r][c]!=1):
                        continue
                    q.append((r,c))
                    grid[r][c]=2
                    fresh-=1
            m+=1

        if fresh>0:
            return -1
        else:
            return m


