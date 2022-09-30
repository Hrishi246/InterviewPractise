def canPartition(nums):
    if sum(nums) % 2:
        return False
    target = sum(nums) // 2

    dp = set()
    dp.add(0)

    for i in range(len(nums) - 1, -1, -1):
        nextdp = set()
        for j in dp:
            nextdp.add(j)
            nextdp.add(j + nums[i])
        dp = nextdp

    return True if target in dp else False

print(canPartition([1,5,11,5]))