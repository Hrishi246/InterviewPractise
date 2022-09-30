def count_construct(target, wordbank, memo = None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return 1

    finalcount = 0
    for word in wordbank:
        if target.startswith(word):
            rem = target[len(word):]
            finalcount = finalcount + count_construct(rem, wordbank, memo)
            memo[target] = finalcount

    return finalcount

if __name__ == '__main__':
    print(count_construct("purple",["purp","p","ur","le","purpl"]))
    print(count_construct("abcdef",["ab","abc","cd","def","abcd"]))
    print(count_construct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
    print(count_construct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
    print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee"]))
