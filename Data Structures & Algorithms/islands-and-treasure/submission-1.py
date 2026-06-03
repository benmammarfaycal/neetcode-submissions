class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        q=collections.deque()

        def addland(r,c):
            if(r<0 or r==rows or c<0 or c==cols or 
                grid[r][c]== -1 or (r,c) in visit):
                return
            visit.add((r,c))
            q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
                    visit.add((r,c))
        
        d=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=d

                addland(r+1,c)
                addland(r-1,c)
                addland(r,c+1)
                addland(r,c-1)

            d+=1

