class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = set()
        n = len(nums)
        for i in range(n):
            x.add(nums[i])
        uniq_x = list(x)
        uniq_x.sort()

        for i in range(len(uniq_x)):
            nums[i] =uniq_x[i]

        return len(uniq_x)

        
        