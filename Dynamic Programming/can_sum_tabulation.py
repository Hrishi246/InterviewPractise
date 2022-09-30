def can_sum(target, numbers):
    dp = [False for i in range(target+1)]
    dp[0] = True
    for i in range(target+1):
        if dp[i]:
            for number in numbers:
                if (i+number) <= target:
                    dp[i+number] = True

    return dp[target]

if __name__ == '__main__':
    print(can_sum(7, [2,3]))
    print(can_sum(7, [5,3,4,7]))
    print(can_sum(7, [2,4]))
    print(can_sum(8, [2,3,5]))
    print(can_sum(300, [12,12]))