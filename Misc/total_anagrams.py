from collections import Counter


def findAnagrams(s, p):
    if len(p) > len(s):
        return []
    pCounter, sCounter = {},{}
    for i in range(len(p)):
        pCounter[p[i]] = 1 + pCounter.get(p[i],0)
        sCounter[s[i]] = 1 + sCounter.get(s[i],0)
    l = 0
    res = [0] if sCounter == pCounter else []

    for r in range(len(p), len(s)):
        sCounter[s[r]] = 1 + sCounter.get(s[r],0)
        sCounter[s[l]] = sCounter[s[l]] - 1
        if sCounter[s[l]] == 0:
            sCounter.pop(s[l])
        l = l + 1
        if sCounter == pCounter:
            res.append(l)

    return res




s = "cbaebabacd"
p = "abc"
print(findAnagrams(s,p))