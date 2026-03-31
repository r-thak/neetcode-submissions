class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIZE = 9
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for i in range (SIZE):
            for j in range (SIZE):
                cur = board[i][j]
                stup = (i // 3, j // 3)
                if cur == ".": continue
                if cur in rows[i] or cur in cols[j] or cur in sqrs[stup] : return False;
                else:
                    rows[i].add(cur)
                    cols[j].add(cur)
                    sqrs[stup].add(cur)

        return True