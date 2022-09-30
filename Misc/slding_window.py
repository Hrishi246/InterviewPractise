# Given an array of integers of size ‘n’.
# Our aim is to calculate the maximum sum of ‘k’
# consecutive elements in the array.

def maxSum(arr,k):
    n = len(arr)
    if n < k:
        print("Invalid")
        return -1
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[k+i]
        max_sum = max(window_sum, max_sum)

    return max_sum




arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, k))