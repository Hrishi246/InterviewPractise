def findRepeatedDnaSequences(s):
    res = []
    hashmap = {}
    i = 0
    while i < len(s):
        hashmap[s[i:i + 10]] = hashmap.get(s[i:i + 10], 0) + 1
        if hashmap[s[i:i + 10]] > 1:
            if s[i:i + 10] not in res:
                res.append(s[i:i + 10])
        i = i + 1

    return res

res = findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print(res)