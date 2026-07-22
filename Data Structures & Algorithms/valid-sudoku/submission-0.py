class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R = defaultdict(list)
        C = defaultdict(list)
        B = defaultdict(list)

        for row, rval in enumerate(board):
            for col, num in enumerate(rval):

                if num == ".":
                    continue

                if row//3 == 0:
                    box = row//3 + col//3
                elif row//3 == 1:
                    box = row//3 + col//3 + 2
                else:
                    box = row//3 + col//3 + 5

                if num in R[row] or num in C[col] or num in B[box]:
                    return False
                else:
                    R[row].append(num)
                    C[col].append(num)
                    B[box].append(num)
        return True
