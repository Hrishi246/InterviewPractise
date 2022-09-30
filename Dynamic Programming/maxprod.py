

def maxProduct(nums):
    maxP, minP = 1, 1
    res = max(nums)

    for i in range(len(nums)):
        if nums[i] == 0:
            maxP, minP = 1, 1
        temp = maxP * nums[i]
        maxP = max(nums[i], maxP * nums[i], minP * nums[i])
        minP = min(nums[i], temp, minP * nums[i])
        res = max(res, maxP)

    return res




if __name__ == '__main__':
    maxProduct([-2,3,-4])