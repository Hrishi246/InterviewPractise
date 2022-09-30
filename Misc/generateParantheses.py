class Solution:
    def generateParantheses(self,n):
        stack = []
        res = []

        def backtracking(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtracking(openN+1,closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtracking(openN,closeN+1)
                stack.pop()

        backtracking(0,0)
        return res

if __name__ == '__main__':
    obj = Solution()
    ans = obj.generateParantheses(3)
    print(ans)