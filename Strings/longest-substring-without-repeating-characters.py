class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        char_set = set()
        maxi = 0
        n = len(s)
        while right<n:
            if s[right] not in char_set:
                char_set.add(s[right])
                maxi = max(maxi,right-left+1)
                right = right+1
            else:
                char_set.remove(s[left])
                left = left+1
        return maxi
            


        