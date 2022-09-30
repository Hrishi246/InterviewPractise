
def permutations(s):
    if len(s) == 1:
        return [s]
    final_res = []
    for i in range(len(s)):
        res = permutations(s[:i] + s[i+1:])
        res = list(map(lambda x : x + s[i], res))
        final_res = final_res + res

    return final_res

def checkInclusion(s1,s2):

    start = 0
    end = len(s1)

    res = permutations(s1)
    print(res)
    while start <= end and end <= len(s2):
        if s2[start:end] in res:
            return True
        start = start + 1
        end = end + 1

    return False

res = checkInclusion("adc","dcda")
print(res)