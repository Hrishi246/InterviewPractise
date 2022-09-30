from collections import *

def groupAnagrams(strs):
    resdict = defaultdict(list)
    for string in strs:
        counter = [0] * 26
        for char in string:
            counter[ord(char) - ord("a")] =+ 1
        resdict[tuple(counter)].append(string)

    return resdict.values()
print(groupAnagrams(["ddddddddddg","dgggggggggg"]))