class Solution:
    def _helper(self, nums, cur, res):
        if len(nums) == 0:
            res.append(cur)
            return

        for i in range(len(nums)):
            self._helper(nums[:i] + nums[i + 1:], cur + [nums[i]], res)

    def permute(self, nums):
        res = []
        self._helper(nums, [], res)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1,2,3]))