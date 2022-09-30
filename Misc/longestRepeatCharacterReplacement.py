def characterReplacement(s,k):
    res = 0
    left = 0
    freq = {}
    for right in range(len(s)):
        freq[s[right]] = 1 + freq.get(s[right],0)
        while (right-left + 1) - max(freq.values()) > k:
            freq[s[left]] = freq[s[left]] - 1
            left = left + 1

        res = max(res, right-left+1)

    return res

print(characterReplacement("AABABBA",2))

