def numDecodings(s):
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    visited = [[False] * len(board[0])] * len(board)
    print(visited)

print(numDecodings("12"))

