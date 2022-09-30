def grid_traveler(m ,n, memo = {}):

    memo_k = str(m) + ',' + str(n)
    if memo_k in memo:
        return memo[memo_k]

    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    memo[memo_k] = grid_traveler(m-1,n, memo) + grid_traveler(m,n-1, memo)
    return memo[memo_k]


print(grid_traveler(100,100))