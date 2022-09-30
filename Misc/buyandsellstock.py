def maxProfit(prices):
    left = 0
    right = 1
    maxProfit = 0

    if len(prices) == 1:
        return prices[0]

    while left < len(prices) and right < (len(prices)) and left < right:
        currProfit = prices[right] - prices[left]
        if currProfit > maxProfit:
            maxProfit = currProfit

        if currProfit <= 0:
            left = right
        right = right + 1

maxProfit([2,1,2,1,0,1,2])