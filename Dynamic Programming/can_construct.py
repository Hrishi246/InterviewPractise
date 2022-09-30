def can_construct(target, wordbank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in wordbank:
        if target.startswith(word):
            remword = target[len(word):]
            if can_construct(remword, wordbank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False

if __name__ == '__main__':
    print(can_construct("abcdef",["ab","abc","cd","def","abcd"]))
    print(can_construct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
    print(can_construct("enterapotentpot",["a","p","ent","enter","ot","o","t"]))
    print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee"]))
