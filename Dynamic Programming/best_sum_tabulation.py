def best_sum(target, numbers):
    dp = [None] * (target+1)
    dp[0] = []
    for i in range(target+1):
        if dp[i] is not None:
            for num in numbers:
                if i + num <= target and (dp[i+num] is None or len(dp[i+num]) > (len(dp[i]) + 1)):
                    dp[i+num] = dp[i] + [num]

    return dp[target]

if __name__ == '__main__':
    print(best_sum(7, [5,3,4,7]))
    print(best_sum(8, [2,3,5]))
    print(best_sum(8,[1,4,5]))
    print(best_sum(100,[1,2,5,25]))
