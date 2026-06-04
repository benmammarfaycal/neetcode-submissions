class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        q=collections.deque()
        visit=set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                    visit.add((r,c))
        def addcell(r,c):
            if(r<0 or r>=rows or
                c<0 or c>=cols or
                (r,c) in visit or
                grid[r][c]== 0):
                return 0
            q.append((r,c))
            visit.add((r,c))
            return 1
        
        m=0
        while q:
            rot=0
            for i in range(len(q)):
                r,c=q.popleft()
                state=(addcell(r+1,c) +
                addcell(r-1,c) +
                addcell(r,c+1) +
                addcell(r,c-1))
                if state>0:
                    rot+=1
            if rot>0:
                m+=1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    return -1
        if m>0:
            return m
        else:
            return 0