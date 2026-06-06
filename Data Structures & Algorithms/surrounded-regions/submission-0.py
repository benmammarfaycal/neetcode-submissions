class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board),len(board[0])
        visit=set()

        def dfs(r,c,visit):
            if (r<0 or r==rows or
                c<0 or c==cols or
                board[r][c]=="X" or
                (r,c) in visit):
                return
            visit.add((r,c))
            dfs(r+1,c,visit)
            dfs(r-1,c,visit)
            dfs(r,c+1,visit)
            dfs(r,c-1,visit)

        for c in range(cols):
            if board[0][c]=="O":
                dfs(0,c,visit)
            if board[rows-1][c]=="O":
                dfs(rows-1,c,visit)
        for r in range(rows):
            if board[r][0]=="O":
                dfs(r,0,visit)
            if board[r][cols-1]=="O":
                dfs(r,cols-1,visit)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O" and (r,c) not in visit:
                    board[r][c]="X" 