class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        count = 0
        for c in s:
            if c=='(' and count >0:
                result = result+c
            if c == '(':
                count = count+1
            if c == ')' and count>1:
                result = result+c
            if c == ')':
                count = count-1
        return result
        