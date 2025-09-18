class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)
        k = k%n
        temp = nums[:k + 1]
        for i in range(k + 1, n):
            nums[i - k - 1] = nums[i]
        for j in range(k):
            nums[n - k + j] = temp[j]
        return nums

    


        