def maximalSquare(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    cache = {}

    def helper(r, c):
        if r >= rows or c >= cols:
            return 0
        if (r, c) not in cache:
            down = helper(r + 1, c)
            right = helper(r, c + 1)
            dia = helper(r + 1, c + 1)
            cache[(r, c)] = 0
            if matrix[r][c] == "1":
                cache[(r, c)] = 1 + min(down, right, dia)

        return cache[(r, c)]

    helper(0, 0)
    return max(cache.values()) ** 2
    # maximal = 0
    # for j in range(len(matrix)):
    #     for i in range(len(matrix[0])):
    #         h,w = j,i
    #         while h < len(matrix) and matrix[h][w] == "1":
    #             h = h + 1
    #         height = h
    #         h,w = j,i
    #         while w < len(matrix[0]) and matrix[h][w] == "1":
    #             w = w + 1
    #         width = w
    #         if (height - j) == (width - i):
    #             maximal = max(maximal, (height-j)*(width-i))
    #         elif ((height - j) != (width - i)) and matrix[j][i] == "1":
    #             maximal = 1
    #
    # return maximal


arr = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(arr))