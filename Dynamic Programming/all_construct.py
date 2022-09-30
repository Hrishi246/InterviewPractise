import copy
def all_construct(target, wordbank, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    finalresult = []
    for word in wordbank:
        if target.startswith(word):
            rem = target[len(word):]
            res = all_construct(rem,wordbank, memo)
            res = list(map(lambda ele : [word] + ele, res))
            finalresult = finalresult + res

    memo[target] = finalresult
    return finalresult


if __name__ == '__main__':
    print(all_construct("abcdef",["ab","abc","cd","def","abcd","ef","c"]))
    print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(all_construct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
    print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee"]))
    print(all_construct("hello",["this","is","hrishikesh"]))
    print(all_construct("yellowstonenationalpark",["yellow","stone","one","st","nation","national","al","park"]))

