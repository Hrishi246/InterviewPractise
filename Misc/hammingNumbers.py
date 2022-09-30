def hamming(n):
    h = [0]*n
    h[0] = 1
    x2 = 2
    x3 = 3
    x5 = 5
    i,j,k = 0,0,0
    for index in range(1, n):
        h[index] = min(x2, min(x3,x5))
        if h[index] == x2:
            i = i + 1
            x2 = 2 * h[i]
        if h[index] == x3:
            j = j + 1
            x3 = 3 * h[j]
        if h[index] == x5:
            k = k + 1
            x5 = 5 * h[i]
    return h[n-1]

hamming(10)