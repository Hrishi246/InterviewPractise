
def numPairsDivisibleBy60(time):
    res = 0
    ref = {}
    for t in time:
        rem = t % 60
        if rem == 0:
            if 0 in ref:
                res = res + ref[0]
        elif (60 - rem) in ref:
            res = res + ref[60 - rem]

        ref[rem] = ref.get(rem, 0) + 1

    return res

numPairsDivisibleBy60([60,60,60])