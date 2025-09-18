class Solution:
    def isPalindrome(self, x: int) -> bool:
        org = x
        if x<0:
            return False
        reverse_num = 0
        while x!=0:
            rem = x%10
            reverse_num = (reverse_num*10)+rem
            x = x//10
        if reverse_num == org:
            return True
        else:
            return False


        