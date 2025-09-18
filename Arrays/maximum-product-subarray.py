# Intuition


# Approach


# Complexity


# Code

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = float('-inf')
        prefix = 1
        suffix = 1
        prod = 1
        n = len(nums)
        for i in range(n):
            if prefix==0:
                prefix = 1
            if suffix==0:
                suffix=1
            prefix = prefix*nums[i]
            suffix = suffix*nums[n-i-1]
            maxi = max(maxi,max(prefix,suffix))
        return maxi