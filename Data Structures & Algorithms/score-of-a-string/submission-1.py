class Solution:
    def scoreOfString(self, s: str) -> int:
        summ = 0
        i=0
        while i<len(s)-1:
            summ+=abs(ord(s[i])-ord(s[i+1]))
            i+=1
        return summ