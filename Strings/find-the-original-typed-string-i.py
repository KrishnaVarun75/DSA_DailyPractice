class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        # result = 1 
        # i = 0
        # while i < len(word):
        #     count = 1
        #     while i + 1 < len(word) and word[i] == word[i + 1]:
        #         count += 1
        #         i += 1 
        #     if count > 1:
        #         result += count - 1       
        #     i += 1
        # return result
        result = 0
        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                result = result+1
        return result+1



        