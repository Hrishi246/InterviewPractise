def longestIncreasingSubsequence(str):
    lis = [1]*len(str)
    for i in range(1,len(str)):
        sunproblems = [lis[k] for k in range(i) if str[i] > str[k]]
        lis[i] = 1 + max(sunproblems, default=0)

    return max(lis, default=0)


print(longestIncreasingSubsequence([11,12,14,13]))