def coinChange(coins, amount):
    if amount == 0:
        return []
    if amount < 0:
        return None

    bestcombination = None
    for c in coins:
        rem = amount - c
        res = coinChange(coins, rem)
        if res is not None:
            combination = res + [c]
            if bestcombination is None or len(combination) < len(bestcombination):
                bestcombination = combination

    return bestcombination

print(coinChange([1,2,5],11))

