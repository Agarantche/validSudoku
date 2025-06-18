class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for r in range(9):
            row_seen = set()
            for c in range(9):
                char = board[r][c]
                if char != '.':
                    if char in row_seen:
                        return False
                    row_seen.add(char)

        # Check columns
        for c in range(9):
            col_seen = set()
            for r in range(9):
                char = board[r][c]
                if char != '.':
                    if char in col_seen:
                        return False
                    col_seen.add(char)

        # Check 3x3 sub-boxes
        for i in range(3):
            for j in range(3):
                box_seen = set()
                # Iterate through each cell in the current 3x3 sub-box
                for r in range(i * 3, i * 3 + 3):
                    for c in range(j * 3, j * 3 + 3):
                        char = board[r][c]
                        if char != '.':
                            if char in box_seen:
                                return False
                            box_seen.add(char)
        return True
