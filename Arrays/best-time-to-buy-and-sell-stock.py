class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                maxi = prices[j]-prices[i]
                if maxi>curr:
                    curr = maxi
        return curr
        