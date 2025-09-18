# Intuition

# Approach


# Complexity


# Code

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #############################
        # n  = len(nums)
        # pref = [1]*n
        # suf = [1]*n
        # res = [0]*n
        # for i in range(1,n):
        #     pref[i] = nums[i-1]*pref[i-1]
        # for j in range(n-2,-1,-1):
        #     suf[j] = nums[j+1]*suf[j+1]
        # for i in range(n):
        #     res[i] = pref[i]*suf[i]
        # return res
        #########################
        # n = len(nums)
        # res = [1]*n
        # for i in range(n):
        #     for j in range(n):
        #         if i!=j:
        #             res[i] = res[i]*nums[j]
        # return res
        n = len(nums)
        res = [1] * n           
        prefix = 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res