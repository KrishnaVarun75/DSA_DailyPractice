class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        n1 = n*(n+1)//2
        sum = 0
        for i in range(n):
            sum = sum+nums[i]
        return n1-sum
