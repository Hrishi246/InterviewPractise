from collections import *

def longestcommonsub(text1, text2):
    text1dict = defaultdict(list)
    text2dict = defaultdict(list)
    maxL = 0
    for i in range(len(text1)-1):
        if text1[i] not in text2:
            continue
        else:
            maxL = 1
        for j in range(i+1,len(text1)):
            if text1[j] in text2:
                text1dict[text1[i]].append(text1[j])

    for i in range(len(text2)-1):
        if text2[i] not in text1:
            continue
        else:
            maxL = 1
        for j in range(i+1,len(text2)):
            if text2[j] in text1:
                text2dict[text2[i]].append(text2[j])

    print(text1dict)
    print(text2dict)

    textdict = text1dict if len(text1dict) > len(text2dict) else text2dict

    othertextdict = text2dict if textdict == text1dict else text1dict

    for key in textdict.keys():
        if key in othertextdict.keys():
            if textdict[key].sort() == othertextdict[key].sort():
                maxL = max(maxL, 1 + len(textdict[key]))

    return maxL
print(longestcommonsub("ezupkr","ubmrapg"))
