
def twoSum(nums, target):

    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i,j]

    hashT = {}

    for num, i in enumerate(nums):
        if num in hashT.keys():
            return [i, hashT[num]]
        else:
            hashT[target - num] = i

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    twoSum(nums,target)