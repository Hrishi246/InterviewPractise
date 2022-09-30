def exist(board, word):
    rows = len(board)
    cols = len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i] or (r, c) in path):
            return False

        path.add((r, c))
        res = dfs(r + 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c - 1, i + 1)
        path.remove((r, c))
        return res

    return dfs(0, 0, 0)

def findWords(board, words):
    res = []
    for word in words:
        if exist(board, word):
            res.append(word)

    return res


f = findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
["eat"])
print(f)