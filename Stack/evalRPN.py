
def evalRPN(tokens):
    stack = []
    res = None
    for t in tokens:
        if stack and t in "+-*/":
            e1 = stack.pop()
            e2 = stack.pop()
            res = int(eval(e2+t+e1))
            stack.append(str(res))
            continue

        stack.append(t)

    return res


print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))