
def best_sum(targetSum, numbers, memo = None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    bestCombination = None
    for number in numbers:
        rem = targetSum - number
        res = best_sum(rem, numbers, memo)
        if res is not None:
            combination = list(res + [number])
            if bestCombination is None or len(combination) < len(bestCombination):
                bestCombination = combination
    memo[targetSum] = bestCombination
    return bestCombination

if __name__ == '__main__':
    print(best_sum(7, [5,3,4,7]))
    print(best_sum(8, [2,3,5]))
    print(best_sum(8,[1,4,5]))
    print(best_sum(100,[1,2,5,25]))