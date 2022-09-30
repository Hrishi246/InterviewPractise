def lengthOfLongestSubstring(s):
    maxL = 0
    start = 0
    for index, value in enumerate(s):
        while value in s[start:index]:
            start = start + 1
        if len(s[start:index+1]) > maxL:
            maxL = len(s[start:index+1])

    return maxL


s = "pwwkew"
print(lengthOfLongestSubstring(s))