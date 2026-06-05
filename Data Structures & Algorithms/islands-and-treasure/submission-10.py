class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        q=collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0 and (r,c) not in visit:
                    q.append((r,c))
                    visit.add((r,c))
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        d=1
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if (row<0 or row==rows or
                        col<0 or col==cols or
                        grid[row][col]== -1 or
                        (row,col) in visit):
                        continue
                    grid[row][col]=d
                    q.append((row,col))
                    visit.add((row,col))
            d+=1



