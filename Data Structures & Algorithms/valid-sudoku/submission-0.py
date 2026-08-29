class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        for row in board:
            seen = set()
            for char in row:
                if char == ".":
                    continue
                if char in seen:
                    return False
                seen.add(char)
        
        for col_idx in range(9):
            seen = set()
            for row_idx, row in enumerate(board):
                char = board[row_idx][col_idx]
                if char == ".":
                    continue
                if char in seen:
                    return False
                seen.add(char)
        
        for row_idx in range(0, 9, 3):
            for col_idx in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        char = board[row_idx + i][col_idx + j]
                        if char == ".":
                            continue
                        if char in seen:
                            return False
                        seen.add(char)
        return True
