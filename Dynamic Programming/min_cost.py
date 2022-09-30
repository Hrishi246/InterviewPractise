from functools import lru_cache


def mincostTickets(days, costs):
    dayset = set(days)
    durations = [1, 7, 30]

    @lru_cache(None)
    def dp(i):
        if i > 365:
            return 0
        elif i in dayset:
            return min(dp(i + d) + c
                       for c, d in zip(costs, durations))
        else:
            return dp(i + 1)

    return dp(1)

if __name__ == '__main__':
    mincostTickets([1,4,6,7,8,20],[2,7,15])