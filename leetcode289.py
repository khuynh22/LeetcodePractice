class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        '''
        ori || new || hold
        0      0      0
        1      0      1
        0      1      2
        1      1      3
        '''
        rows = len(board)
        cols = len(board[0])

        def countNeighbors(r, c):
            neighbors = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i == r and j == c) or i < 0 or j < 0 or i >= rows or j >= cols:
                        continue
                    else:
                        if board[i][j] in [1, 3]:
                            neighbors += 1
            return neighbors

        for r in range(rows):
            for c in range(cols):
                neighbors = countNeighbors(r, c)
                if board[r][c]:
                    if neighbors in [2, 3]:
                        board[r][c] = 3
                elif neighbors == 3:
                    board[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1
