class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        if s == reversed(s):
            return len(s)
        result = ""
        result_len = 0
        for i in range(len(s)):
            left,right = i,i
            #odd
            while left>=0 and right<len(s) and s[left] == s[right]:
                if (right-left+1)>result_len:
                    result = s[left:right+1]
                    result_len = right-left+1
                left = left-1
                right = right +1


            # even
            left,right = i,i+1
        
            while left>=0 and right<len(s) and s[left] == s[right]:
                if (right-left+1)>result_len:
                    result = s[left:right+1]
                    result_len = right-left+1
                left = left-1
                right = right +1

        return result

        