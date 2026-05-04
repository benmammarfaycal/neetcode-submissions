class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[[] for _ in range(9)]
        col=[[] for _ in range(9)]
        box=[[] for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val==".":
                    continue
                box_index=(r//3)*3+ (c//3)
                if val in row[r] or val in col[c] or val in box[box_index]:
                    return False
                row[r].append(val)
                col[c].append(val)
                box[box_index].append(val)
        return True