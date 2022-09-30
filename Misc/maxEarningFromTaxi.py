def maxTaxiEarnings(n, rides):
    def bisect(val, arr):
        low = 0
        high = len(arr)
        while (low < high):
            mid = low + (high - low) // 2
            if (arr[mid] > val):
                high = mid
            else:
                low = mid + 1
        return (low)

    arr = [[e, s, t] for s, e, t in rides]
    arr.sort(key=lambda x: x[0])
    ends = []
    for i in arr:
        ends.append(i[0])
    dp = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        point = bisect(arr[i][1], ends)
        dp[i + 1] = max(dp[i], dp[point] + arr[i][0] - arr[i][1] + arr[i][2])
    return (dp[-1])

maxTaxiEarnings(20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]])