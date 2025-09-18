class Solution:
    def reverse(self, x: int) -> int:

        n = x<0
        num = abs(x)
        reverse_num = 0
        
        while num!=0 :
            rem = num%10
            reverse_num = (reverse_num *10)+rem
            num//=10
        
        if n:
            reverse_num =  -reverse_num
        if reverse_num<-2**31 or reverse_num >2**31-1:
            return 0
        return reverse_num
            