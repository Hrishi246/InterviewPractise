def grid_traveler(m,n):
    table = [[0] * (n+1) for j in range(m+1)]
    table[1][1] = 1
    for row in range(m+1):
        for col in range(n+1):
            if (row + 1) <= m and (col + 1) <= n:
                table[row + 1][col] += table[row][col]
                table[row][col + 1] += table[row][col]
            elif (row + 1) <= m:
                table[row + 1][col] += table[row][col]
            elif (col + 1) <= n:
                table[row][col+1] += table[row][col]


    return table[m][n]


if __name__ == '__main__':
    print(grid_traveler(1,1))
    print(grid_traveler(2,3))
    print(grid_traveler(3,2))
    print(grid_traveler(3,3))
    print(grid_traveler(18,18))
