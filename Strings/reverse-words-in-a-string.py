# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = s[::-1]
#         words  = s.split(" ")
#         reversed_words = [word[::-1] for word in words if word]
#         result = " ".join(reversed_words)
#         return result


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        words = s.split()
        for word in words:
            arr.append(word)
        rev = []
        while arr:
            rev.append(arr.pop())
        return " ".join(rev)
        # temp = ""
        # result = ""
        # left = 0
        # right = len(s)-1
        # while left<=right and s[left]==" ":
        #     left = left+1
        # while right>=0 and s[right] ==" ":
        #     right = right-1
        # while(left<=right):
        #     if s[left]!=" ":
        #         temp = temp+s[left]
        #     else:
        #         if temp!="":

        #             if result!="":
        #                 result = temp+" "+result
        #             else:
        #                 result = temp
        #             temp = ""
        #     left = left+1
        # if temp != "":
        #     if result != "":
        #         result = temp + " " + result
        #     else:
        #         result = temp
        # return result