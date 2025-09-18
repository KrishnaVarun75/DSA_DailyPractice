class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        while(n>0):
            if(int(num[n-1])%2 !=0):
                return num[0:n]
            else:
                n = n-1
        if (n == 1):
            if(int(num[n-1])%2 !=0):
                return num[0]
        else:
            return ""
            