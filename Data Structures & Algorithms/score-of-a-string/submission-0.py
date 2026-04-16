class Solution:
    def scoreOfString(self, s: str) -> int:
        summ = 0
        i=0
        while i<len(s)-1:
            a = s[i]
            b = s[i+1]
            summ+=abs(ord(a)-ord(b))
            i+=1
        return summ