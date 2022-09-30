def twosum(arr, target):
    start = 0
    end = len(arr)-1
    while start < end:
        sum = arr[start] +  arr[end]
        if sum < target:
            start = start + 1
        elif sum > target:
            end = end - 1
        else:
            return arr[start],arr[end]

def maxSumFixedWindow(arr, k):
    start = 0
    end = k
    currSum = sum(arr[start:end])
    maxSum = 0
    for i in range(0, len(arr)-k):
        currSum = currSum - arr[i] + arr[i + k]
        if currSum > maxSum:
            maxSum = currSum
    return maxSum



# print(twosum([2,7,11,15,8,16], 27))
print(maxSumFixedWindow([2,1,5,1,3,2,61,15,3,3],3))